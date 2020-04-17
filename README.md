# Tabular Method: Quine-McCluskey Algorithm
2020 1st semester Digital Logic Design
## How to use
  > `$ python main.py`

## Example
1. Optimizing 4 variables boolean function with don't cares
```
$ python main.py
Enter number of variables: 4
Enter Minterms: 1 2 5 6 7 8 9 10 14
Enter Don't cares: 3 12
({8, 9}, (ab'c'))
({2, 3, 6, 7}, (a'c))
({8, 10, 12, 14}, (ad'))
({1, 3, 5, 7}, (a'd))
({1, 9}, (b'c'd))
({2, 10, 6, 14}, (cd'))
```

2. Optimizing 3 variables boolean function with no don't care
  > If you don't want to use "Don't cares", you just have to press the enter key.
```
Enter number of variables: 3
Enter Minterms: 0 1 5 6 7
Enter Don't cares: 
({0, 1}, (a'b'))
({1, 5}, (b'c))
({5, 7}, (ac))
({6, 7}, (ab))
```

> **The PI's order is not guaranteed in every optimizing**