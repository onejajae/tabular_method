import copy
from itertools import combinations
from minterm import Minterm, group_minterms


class QM:
  def __init__(self, var_count, minterms, dontcares=[]):
    self.var_count = var_count
    self.minterms = minterms
    self.group = group_minterms(var_count, minterms+dontcares)

  def __check(self, x):     # 차이나는 부분이 딱 1개인지 검사
    ones = 0
    num = x
    for i in range(self.var_count):
      if num & 1: 
        ones += 1
      if ones > 1:
        return False
      num = num >> 1
    if ones:
      return True
    else:
      return False
  
  def __compare(self, left, right):   # 0,1 비교 및 x 동일 비교
    if self.__check(left ^ right) and left.x == right.x:
      return True   # 각 자릿수에서 다른 부분 딱 1개일때, x부분 동일할때
    else:
      return False

  def __optimize(self, varCount, group):
    next_group = {ones:set() for ones in range(varCount)}
    
    count = 0
    used_rights = set()
    used_lefts = set()

    for i in range(varCount):     # 1의 개수 0부터 반복 -> 1이 변수만큼 있는경우는 포함하지 않음
      for left in group[i]:       # prime implicant 선택
        for right in group[i+1]:  # 위에서 선택한 것보다 1이 1개 더 많은 것 선택
          x = left ^ right        # 서로 차이나는 부분 선택
          if self.__compare(left, right): 
            new_term = Minterm(left & right, self.var_count, x+left.x, left.sums | right.sums)
            flag = True
            for pi in next_group[i]:    # 중복 탐색
              if pi.sums-new_term.sums == set(): 
                flag=False
                break
            if flag:                    # 중복이 없어야 추가
              next_group[i].add(new_term)
            used_lefts.add(left)        
            used_rights.add(right)
            count += 1
      for used_left in used_lefts:      # 사용한 pi 삭제
        group[i].remove(used_left)
      used_lefts = used_rights
      used_rights = set()
    else:                               # 마지막 pi 삭제
      for used_left in used_lefts:
        group[varCount].remove(used_left)

    if count == 0:      # 종료조건
      return group
    else:               # 재귀호출
      for ones, minterms in self.__optimize(varCount-1, next_group).items():
        for minterm in minterms:
          group[ones].add(minterm)
      return group
  
  def optimize(self):
    group = copy.deepcopy(self.group)
    return self.__optimize(self.var_count, group)

  def minimize(self):
    minterms = set(num.num for num in self.minterms)
    group = copy.deepcopy(self.group)
    pi_list = [pi for key, value in self.__optimize(self.var_count, group).items() for pi in value]

    result = set()

    # epi 탐색
    for minterm in minterms:
      count = 0
      epi = None
      for pi in pi_list:
        if minterm in pi.sums:
          count += 1
          if count > 1: break
          epi = pi
      if count == 1:
        result.add(epi)
    

    # epi 배제 및 epi가 포함하는 minterm 제거
    for epi in result:
      for minterm in epi.sums:
        if minterm in minterms:
          minterms.remove(minterm)
      pi_list.remove(epi)

    # 포함하는 minterm 개수의 내림차순 정렬
    pi_list.sort(key=lambda x: len(x.sums), reverse=True)

    # pi의 모든 조합 탐색 (petrick's algoritm 미적용)
    for pi_num in range(1,len(pi_list)+1):
      for combi in combinations(pi_list, pi_num):
        cover = set()
        used = []
        for pi in combi:
          cover |= pi.sums
          used.append(pi)
        if cover >= minterms:
          # minterm을 모두 포함하면 바로 탐색 종료
          return list(result)+used

    return list(result)

      

if __name__ == "__main__":

  # for test
  varCount = 4
  minterms = [
    Minterm(0, varCount),
    Minterm(2, varCount),
    Minterm(5, varCount),
    Minterm(6, varCount),
    Minterm(7, varCount),
    Minterm(8, varCount),
    Minterm(9, varCount),
    Minterm(13, varCount)
  ]
  dontcares = [
    Minterm(1, varCount),
    Minterm(12, varCount),
    Minterm(15, varCount)
  ]

  tabular = QM(4, minterms, dontcares)

  for key, value in tabular.optimize().items():
    for j in value:
      print(j)
  for i in tabular.minimize():
    print(i)
 
  print()
  varCount = 4
  minterms = [
    Minterm(0, varCount),
    Minterm(4, varCount),
    Minterm(8, varCount),
    Minterm(10, varCount),
    Minterm(11, varCount),
    Minterm(12, varCount),
    Minterm(13, varCount),
    Minterm(15, varCount)
  ]
  tabular2 = QM(4, minterms)


  for i in tabular2.minimize():
    print(i)
