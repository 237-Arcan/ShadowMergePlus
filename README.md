# ShadowMerge+

**ShadowMerge+** est une plateforme hybride d’analyse, de prédiction et de fusion d’insights pour le sport, combinant modèles statistiques, signaux comportementaux et modules experts.

---

## 🚩 Fonctionnalités principales

- Analyse des cotes et signaux de marché (ShadowOdds)
- Moteur expert ArcanX (historique, pattern mining, chrono-echo)
- Intégration de modules live (Sentinel)
- Fusion et arbitrage de prédictions via logiques hybrides
- Plug & play pour modules d’insights additionnels

---

## 📂 Structure du dépôt

```
core/
  shadowodds/       # Analyse des cotes, triggers, validation
  arcanx/           # Moteur expert historique/chrono
  arcanpocs/        # Proof of concept, signaux faibles
  khawatim/         # Analyse finale, scoring
  shared/           # Config, log, helpers, data_loader, constantes
tests/              # Tests unitaires par module
datasets/           # Jeux de données d’exemple (csv, yaml, json)
.github/workflows/  # CI/CD (tests, lint, coverage)
docs/               # Documentation détaillée, schémas
main.py             # Orchestrateur principal
train.py            # Entraînement/chargement initial
requirements.txt    # Dépendances Python
launch.sh           # Script de lancement (optionnel)
```

---

## 🏗️ Schéma d’architecture (PlantUML)

```plantuml
@startuml
actor Utilisateur

Utilisateur -> main.py : lance une analyse ou prédiction

main.py -> shared.config : charge la config
main.py -> shared.logger : initialise le logger
main.py -> shadowodds/ : active ShadowOddsEngine
main.py -> arcanx/ : active ArcanXEngine
main.py -> arcanpocs/ : active ArcanPOCS
main.py -> khawatim/ : active Khawatim
main.py -> shared.data_loader : charge les datasets

shadowodds/ -> datasets/ : lit odds_history.csv, patterns
arcanx/ -> datasets/ : lit historiques, patterns

main.py -> shared.helpers : normalisation, fusion, triggers

main.py -> Utilisateur : affiche résultats, logs, alertes

@enduml
```

---

## 🚀 Lancement rapide

```bash
git clone https://github.com/237-Arcan/ShadowMergePlus.git
cd ShadowMergePlus
pip install -r requirements.txt
python main.py --match_id 12345
```

---

## 🧪 Tests unitaires

```bash
pytest
# ou
python -m unittest discover tests
```

---

## 🛠️ Modules principaux

- **ShadowOddsEngine** : Analyse comportementale des marchés de cotes
- **ArcanXEngine** : Exploitation des historiques et patterns
- **ArcanPOCS** : Signaux faibles et filtrage
- **Khawatim** : Scoring final, validation multi-sources
- **Sentinel** : Intégration live (websocket, scraping)

---

## 📚 Documentation

Voir le dossier [docs/](./docs/) ou le Wiki GitHub pour :
- Vue d’ensemble détaillée
- Diagrammes d’architecture
- Exemples d’utilisation avancés
- Logique de fusion et triggers

---

## 📦 CI/CD & Qualité

- Tests automatisés via GitHub Actions [.github/workflows/test.yml]
- Couverture de code avec Codecov ou Coveralls
- Badges à venir sur ce README

---

## 👥 Contribuer

1. Fork, clone et crée une branche.
2. Ajoute tes modifications + tests unitaires.
3. Ouvre une Pull Request.

---

## 📜 Licence

[MIT License](LICENSE)

---

**ShadowMerge+** © 2025 237-Arcan.  
Contact, suggestions et contributions bienvenus !
