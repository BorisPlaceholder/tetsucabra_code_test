import tetsucode
def test_tetsucabrafunction():
  assert tetsucode.tetsucabrafunction('TETSUCABRA') == "TETSUCABRA!"
  assert tetsucode.tetsucabrafunction('NOTTETSU') == ":("
  assert tetsucode.tetsucabrafunction('e') == ":("
  assert tetsucode.tetsucabrafunction('E') == ":("
