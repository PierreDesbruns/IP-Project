# IP-Project : Détection des zones à risques d'incendies

Ce projet a pour but de déterminer, sur la base de critère météorologiques, les zones géographiques où des incendies risquent de se former.

Auteurs : Agate Comello et Pierre Desbruns.

Langage utilisé : Python.

## Librairies nécessaires

- OpenCV : installer avec `pip install opencv-python`
- Numpy : installer avec `pip install numpy`

## Description des fichiers et répertoires

- `main.py` : entrée du programme ; exécuter ce script pour lancer le programme.
- `bitwise.py` : fichier de fonctions d'opérations bit à bit sur des images.
- `humidite_relative.py` : fichier de fonction qui retourne le masque d'humidité relative.
- `humidite_relative.py` : fichier de fonction qui retourne le masque d'humidité relative.
- `humidite_sol.py` : fichier de fonction qui retourne le masque d'humidité du sol.
- `precipitation.py` : fichier de fonction qui retourne le masque des précipitations.
- `precipitation_nuage.py` : fichier de fonction qui retourne le masque des précipitations et des nuages.
- `temperature.py` : fichier de fonction qui retourne le masque de température.
- `data/` : dossier contenant les différentes cartes classées par jour d'observation.