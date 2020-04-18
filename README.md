# Tabular Method: Quine-McCluskey Algorithm
2020 1st semester Digital Logic Design
## How to use
  > `$ python main.py`

## Example
1. Optimizing a 4 variables boolean function with don't cares
```
$ python main.py
Enter number of variables: 4
Enter Minterms: 1 2 5 6 7 8 9 10 14
Enter Don't cares: 3 12

All Prime Implicants
({2, 3, 6, 7}, (a'c))
({1, 9}, (b'c'd))
({8, 10, 12, 14}, (ad'))
({1, 3, 5, 7}, (a'd))
({8, 9}, (ab'c'))
({2, 10, 6, 14}, (cd'))

Minimized Prime Implicants
({1, 3, 5, 7}, (a'd))
({2, 10, 6, 14}, (cd'))
({8, 9}, (ab'c'))
```

2. Optimizing a 3 variables boolean function with no don't care
  > If you don't want to use "Don't cares", you just have to press the enter key.
```
$ python main.py
Enter number of variables: 3
Enter Minterms: 0 1 5 6 7
Enter Don't cares: 

All Prime Implicants
({0, 1}, (a'b'))
({1, 5}, (b'c))
({5, 7}, (ac))
({6, 7}, (ab))

Minimized Prime Implicants
({6, 7}, (ab))
({0, 1}, (a'b'))
({1, 5}, (b'c))
```

> **The PI's order is not guaranteed in every optimizing**

## About class Minterm
`Minterm` 클래스는 `num, x, var_count, sums` 속성을 가지고 있다.

1. `num` 속성은 해당 minterm이 가지고 있는 1의 위치 정보를 저장
2. `x` 속성은 해당 minterm이 가지고 있는 x의 위치 정보를 저장
3. `var_count` 속성은 해당 minterm의 변수 개수를 저장
4. `sums` 속성은 조합하고 있는 minterm의 집합
  >`num`과 `x`속성을 2진수로 변환해 보면 각각의 위치 정보를 바로 알 수 있다.

### 언제 조합되는가?
비교하는 두 implicant의 x 위치가 동일하고, 1과 0 차이가 딱 한 자리 수일때 조합할 수 있다.

> 0X01 (1,5):  `Minterm(num=0b0001, var_count=4, x=0b0100, sums={1,5})`
>
> 1X01 (9,13): `Minterm(num=0b1001, car_count=4, x=0b0100, sums={9,13})`

위 두 implicant는 X의 위치가 같고, 1비트 차이가 나기 때문에 조합할 수 있다.

x의 위치 정보는 `0b0100 == 0b0100` 으로 서로 같다.

`0b0001 ^ 0b1001 == 0b1000`이므로, 1이 하나만 나온다.

따라서 위 두 implicant를 조합하면 XX01이고 

1의 위치는 0b0001, x의 위치는 0b1100으로 표현할 수 있다.

> XX01 (1,5,9,13): `Minterm(num=0b0001, var_count=4, x=0b1100, sums={1,5,9,13})`

### 알고리즘 도출
위 과정을 다음과 같이 정리할 수 있다.
1. 각 implicant의 `x`속성이 같은지 확인
2. 각 implicant의 `num`속성을 XOR 연산
3. 2번 결과값을 한 칸씩 비트 시프트 하면서 1이 한번만 나오는 지 `var_count`번 확인

1번과 3번의 확인 과정이 모두 참이라면 조합할 수 있다.

조합할 때, 새로운 Minterm 인스턴스를 만드는데 새로운 인스턴스의 속성값은 다음과 같다.

1. `num`속성에는 기존 두 implicant의 `num`속성을 AND 연산한 값을 지정
2. `x` 속성에는 기존 두 implicant의 `num`속성을 XOR 연산한 값과 기존 `x`속성을 더한 값을 지정
3. `sums` 속성에는 기존 두 implicant의 합집합을 지정

## PI Chart 문제점
Petrick's Method가 적용되지 않았기 때문에 시간복잡도가 상당하다. 

따라서 non-essential prime implicant의 개수가 n일때, 최적해의 집합을 찾는 시간복잡도는 `O(2^n)`이다.