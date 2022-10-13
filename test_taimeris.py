from taimeris import dati_korekti
  
def test_neg_h():
  assert dati_korekti(-4, 0, 0) is False
  
def test_neg_m():
  assert dati_korekti(0, -2, 0) is False
  
def test_neg_s():
  assert dati_korekti(0, 0, -6) is False
  
def test_invalid_h():
  assert dati_korekti(27, 0, 0) is False
  
def test_invalid_m():
  assert dati_korekti(0, 63, 0) is False
  
def test_invalid_s():
  assert dati_korekti(0, 0, 70) is False
  
def test_valid_time():
  assert dati_korekti(2, 45, 13) is True
