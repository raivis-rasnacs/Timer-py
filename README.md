# Taimeris
### Problēmas apraksts:<br>
Lai veiktu precīzu laika atskaiti, lieto taimeri, kas noteiktā intervālā laiku skaita atpakaļ, kamēr sasniedz 00:00:00.

### Specifikācija:<br>
Dotajā failā *taimeris.py* ir dotas funkcijas:
* ievads() - prasa ievadīt stundas, minūtes un sekundes 
* dati_korekti() - pārbauda ievaddatus
  * ja stundas nav intervālā no 0 līdz 23 (ieskaitot), atgriež False
  * ja minūtes vai sekundes nav intervālā no 0 līdz 59 (ieskaitot), atgriež False
  * citādi atgriež True
* atskaite() - izdrukā laika atskaiti pareizā formātā

### Nosacījumi:<br>
Tavs uzdevums ir 
* sastādīt algoritmu, kas pārbauda ievaddatu pareizību
* sastādīt ciklisku algoritmu, kas veic precīzu laika atskaiti un veic izdruku ekrānā reizi sekundē.<br>

Lai aizkavētu cikla izpildi, lieto *sleep(delayInSeconds)*

Lai panāktu pareizu laika attēlošanu izvadā, izmanto formatēšanu.
~~~py
h, m, s = 4, 8, 2
print(f"{h:02}:{m:02}:{s:02}")
# >>> 04:08:02
~~~

### Testpiemēri:<br>
Ieskaties failā *test_taimeris.py*


