# SHADOWMERGE+ – Documentation Pipeline & Formats

## 1. Présentation

ShadowMerge+ est un moteur d’analyse comportementale appliquant une série de triggers sur des données de matchs pour générer des signaux structurés et un score de confiance.  
Le système est conçu pour être extensible (ML/REST/Realtime à venir) et exploite des logs structurés pour le monitoring.

---

## 2. Structure des fichiers

### 2.1 Fichier d’entrée – `match_data.json`
Ce fichier est généré avant l’analyse (pré-analyse) et déposé dans `outputs/match_data/`.

**Exemple :**
```json
{
  "match_id": "ABC123",
  "odds": [1.75, 2.10],
  "volumes": [12000, 8500],
  "players": ["Player A", "Player B"],
  "ratings": {"Player A": 7.2}
}
```
- `match_id` : identifiant unique du match
- `odds` : liste d’historiques des cotes
- `volumes` : volumes associés à chaque tick
- `players` : (optionnel) liste des joueurs impliqués
- `ratings` : (optionnel) notes ou indicateurs spécifiques

### 2.2 Fichier de sortie – `signal_output.json`
Ce fichier est généré après l’analyse et déposé dans `outputs/signals/`.

**Exemple :**
```json
{
  "match_id": "ABC123",
  "confidence_score": 0.87,
  "signals": [
    {
      "trigger": "FreezeTrigger",
      "status": true,
      "reason": "Cote figée à 1.75 malgré 82% de mises sur le favori"
    }
  ]
}
```
- `match_id` : identifiant du match (copié de l’entrée)
- `confidence_score` : score global de confiance (float ∈ [0,1])
- `signals` : liste détaillée des triggers déclenchés ou non  
  - `trigger` : nom du trigger
  - `status` : booléen (déclenché ou non)
  - `reason` : explication textuelle

---

## 3. Pipeline Technique

```mermaid
graph TD
A[main.py] --> B[SignalOrchestrator]
B --> C[match_data.json]
C --> D[ShadowSignalEngine]
D --> E[TriggerSet (x3)]
E --> F[signal_output.json]
```

- **main.py** : point d’entrée, déclenche le pipeline
- **SignalOrchestrator** : collecte les fichiers d’entrée, orchestre l’analyse et la génération des signaux
- **ShadowSignalEngine** : applique la logique métier
- **TriggerSet** : ensemble de triggers spécialisés (Freeze, Volatility, Betflow…)
- **signal_output.json** : fichier de résultat structuré

---

## 4. Logging Structuré

Tous les modules critiques exploitent un logger structuré (JSON) pour :
- Tracer l’exécution (début, fin, erreurs, déclenchement de triggers…)
- Faciliter l’agrégation/monitoring (ELK, Datadog…)
- Ajouter des champs métiers à la volée (match_id, trigger, etc.)

**Exemple de log :**
```json
{
  "level": "INFO",
  "logger": "signal_engine.shadow_signal_engine",
  "message": "Analyse d'un match",
  "time": "2025-06-12 14:41:18,123",
  "match_id": "ABC123"
}
```

---

## 5. Extensions prévues

| Module       | Fonction                          | Statut       |
| ------------ | -------------------------------- | ------------ |
| MLClassifier | Prédiction automatisée du risque  | 🔜 v2         |
| API FastAPI  | Exposer les signaux en REST       | 🔜 optionnel  |
| WebSocket    | Push temps réel vers dashboard    | 🔜 optionnel  |

---

## 6. Checklist de conformité

- [x] Les fichiers produits respectent la structure ci-dessus
- [x] Les logs sont structurés et enrichis
- [x] Le pipeline fonctionne main → signal_output.json
- [x] Les triggers sont traçables individuellement dans les logs
- [x] (À faire) : tests d’intégration pipeline & validation de format

---

**Contact : 237arcan@gmail.com  – © 2025**
