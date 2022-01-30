import main
def test_tetsucabrafunction():
  assert main.tetsucabrafunction('TETSUCABRA') == "TETSUCABRA!"
  assert main.tetsucabrafunction('NOTTETSU') == ":("
  assert main.tetsucabrafunction('e') == ":("
  assert main.tetsucabrafunction('E') == ":("
