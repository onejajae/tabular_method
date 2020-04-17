from minterm import Minterm
from quine_mccluskey import QM

if __name__ == "__main__":
  varCount = int(input('Enter number of variables: '))
  minterms = [Minterm(int(m), varCount) for m in input('Enter Minterms: ').split()]
  dontcares = [Minterm(int(m), varCount) for m in input('Enter Don\'t cares: ').split()]

  tabular = QM(varCount, minterms, dontcares)
  optimized_prime_implicants = tabular.optimize()
  
  for key, value in optimized_prime_implicants.items():
    for j in value:
      print(j)