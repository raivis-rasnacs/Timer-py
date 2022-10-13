# --- uzvārds, klase ---

from time import sleep

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
  pass
  """
  TODO: Sastādi datu validācijas algoritmu! 
  Atgriež True, ja dati korekti, citādi False
  """

if __name__ == "__main__":
  ievads()
