# Taimeris
### Problēmas apraksts:<br>
Lai veiktu precīzu laika atskaiti, lieto taimeri, kas noteiktā intervālā laiku skaita atpakaļ, līdz sasniedz 00:00:00.

### Nosacījumi:<br>
Dotajā failā *timer.py* ir funkcija *taimeris()*, kas parametru veidā saņem ievadītās stundas, minūtes un sekundes. Tavs uzdevums ir sastādīt ciklisku algoritmu, kas veic precīzu laika atskaiti un veic izdruku ekrānā reizi sekundē.<br>

Lai aizkavētu cikla izpildi, lieto *sleep(delayInSeconds)*

Lai panāktu pareizu laika attēlošanu izvadā, izmanto formatēšanu.
~~~py
h, m, s = 4, 8, 2
print(f"{h:02}:{m:02}:{s:02}")
# >>> 04:08:02
~~~


