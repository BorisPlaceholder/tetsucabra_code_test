def tetsucabrafunction(tetsutest):
  tetsutestvar=0
  while tetsutestvar==0:
    print("TETSUCABRA?")
    tetsutest=input()
    if tetsutest.lower()=="tetsucabra":
      print("TETSUCABRA!")
      tetsutestvar=1
    else:
      print(":(")

import main
def test_tetsucabrafunction():
  assert main.tetsucabrafunction('TETSUCABRA')
  assert main.tetsucabrafunction('NOTTETSU')
  assert main.tetsucabrafunction('e')
  assert main.tetsucabrafunction('E')
