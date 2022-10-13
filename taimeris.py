# --- uzvārds, klase ---

import sleep from time

# Laika atskaite
def atskaite(h, m, s):
  pass # TODO: Sastādi taimera algoritmu!

def ievads():
  # Ievada stundas, minūtes un sekundes
  h = int(input("Stundas: "))
  m = int(input("Minūtes: "))
  s = int(input("Sekundes: "))
  
  if dati_korekti(h, m, s) == True:
    atskaite(h, m, s)
  else:
    print("Kļūda!")
  
def dati_korekti(stundas, minutes, sekundes):
  
  # TODO: Sastādi datu validācijas algoritmu! 
  
  return # Atgriež True, ja dati korekti, citādi False


ievads()
