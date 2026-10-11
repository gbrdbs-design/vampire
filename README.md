# Vampire – iOS app prototípus

Kattintható HTML prototípus iPhone keretben, a Figma „Screens” oldal Home / For You és Profile / Empty képernyőiből, Dark/Light váltóval.

- `index.html` – önálló, böngészőben megnyitható prototípus (a képek base64-ben beágyazva)
- `src/vampire-proto.src.html` – forrás sablon `__IMG_név__` helyőrzőkkel
- `assets/` – a Figmából exportált fotók
- `src/build.py` – a sablonból és a képekből újraépíti az `index.html`-t

```sh
python3 src/build.py
```
