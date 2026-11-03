# TP2 – Supervision des machines d’un atelier

## Présentation

Ce projet a été réalisé dans le cadre du TP2 de Python à l'ENSAM, année universitaire 2026–2027.

L'objectif est de développer une application Python permettant de superviser les machines d'un atelier industriel à partir de fichiers JSON, CSV et LOG.

## Fonctionnalités

- Chargement des machines depuis un fichier JSON.
- Lecture et validation des relevés depuis un fichier CSV.
- Gestion des exceptions et des lignes invalides.
- Calcul des moyennes de température et de vibration.
- Détection des alertes selon les seuils de chaque machine.
- Classement des machines selon le nombre d'alertes.
- Identification des machines silencieuses.
- Lecture des événements avec les expressions régulières et les générateurs.
- Calcul du temps d'arrêt des machines.
- Génération d'un rapport JSON et d'un fichier CSV des rejets.

## Technologies utilisées

- Python 3
- JSON et CSV
- Regex
- Générateurs
- Gestion des exceptions
- Pytest
- Git et GitHub

## Exécution

Lancer le programme :

```bash
python main.py
```

## Tests

Exécuter tous les tests :

```bash
pytest -q
```

**Résultat obtenu : 54 tests réussis.**

## Structure du projet

- `atelier.py` : fonctions de traitement et d'analyse.
- `exceptions.py` : exceptions personnalisées.
- `main.py` : programme principal.
- `donnees/` : fichiers de données.
- `tests/` : tests automatisés.
- `sorties/` : rapports générés automatiquement (non versionnés).
