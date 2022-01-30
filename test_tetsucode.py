def test_tetsucabrafunction():
  assert tetsucabrafunction('TETSUCABRA') == "TETSUCABRA!"
  assert tetsucabrafunction('NOTTETSU') == ":("
  assert tetsucabrafunction('e') == ":("
  assert tetsucabrafunction('E') == ":("
