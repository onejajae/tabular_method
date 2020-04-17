class Minterm(object):
  def __init__(self, num, var_count, x=0, sums=set()):
    self.num = num    # 실제 숫자
    self.x = x        # 소거된 숫자 
    self.var_count = var_count
    if sums == set():
      self.sums = {num}
    else:
      self.sums = sums

  def __str__(self):
    num = self.num
    x = self.x
    base = ""
    for i in range(self.var_count):
      if not x & 1:
        if num & 1:
          base = chr(96 + self.var_count-i) + base
        else:
          base = chr(96 + self.var_count-i) + "\'" + base
          
      num = num >> 1
      x = x >> 1
    
    return f'({self.sums}, ({base}))'

  def __and__(self, other):
    return self.num & other.num

  def __xor__(self, other):
    return self.num ^ other.num


def group_minterms(varCount, minterms):  # 1의 개수별로 그룹화
  group = {ones:set() for ones in range(varCount+1)}
  for minterm in minterms:
    ones = 0
    num = minterm.num
    for i in range(varCount):
      if num & 1 : ones += 1
      num = num >> 1
    group[ones].add(minterm)
  return group
