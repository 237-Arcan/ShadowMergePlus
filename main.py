import argparse
import logging
import yaml

from core.shadow_odds import ShadowOddsEngine
from core.arcanx import ArcanXEngine
from core.sentinel_live import ArcanSentinelLive
from core.pocs import ArcanPOCS
from core.khawatim import Khawatim
from utils.helpers import InsightManager, TriggerSet, PredictionEvaluator

from orchestrator.batch_orchestrator import BatchDataOrchestrator

# 👇 Importe le moteur d'analyse comportementale
from signal_engine.shadow_signal_engine import ShadowSignalEngine

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("ShadowMerge+")

def load_settings(config_path="config/settings.yaml"):
    with open(config_path, 'r') as file:
        settings = yaml.safe_load(file)
    logger.info("Configurations chargées avec succès.")
    return settings

def initialize_modules(settings):
    modules = {}
    if settings['enable_modules']['shadow_odds']:
        modules['shadow_odds'] = ShadowOddsEngine(settings)
        logger.info("Module ShadowOdds activé.")
    if settings['enable_modules']['arcanx']:
        modules['arcanx'] = ArcanXEngine(settings)
        logger.info("Module ArcanX activé.")
    if settings['enable_modules']['sentinel_live']:
        modules['sentinel'] = ArcanSentinelLive(settings)
        logger.info("Module ArcanSentinel-live activé.")
    if settings['enable_modules']['arcanpocs']:
        modules['pocs'] = ArcanPOCS(settings)
        logger.info("Module ArcanPOCS activé.")
    if settings['enable_modules']['khawatim']:
        modules['khawatim'] = Khawatim(settings)
        logger.info("Module Khawatim activé.")
    return modules

def main():
    parser = argparse.ArgumentParser(description="ShadowMerge+ | Système hybride de prédiction avancée.")
    parser.add_argument('--match_ids', nargs='+', help="Liste des IDs de matchs à analyser", required=True)
    parser.add_argument('--live', action='store_true', help="Activer le mode live pour ArcanSentinel")
    args = parser.parse_args()

    settings = load_settings()
    modules = initialize_modules(settings)

    logger.info("Démarrage de l'analyse pour les matchs: %s", args.match_ids)

    # ✅ Collecte centralisée des données via BatchDataOrchestrator
    batch_orchestrator = BatchDataOrchestrator()
    all_matches_data = batch_orchestrator.collect_all_for_matches(args.match_ids)
    logger.info(f"[Orchestrator] Données agrégées : {all_matches_data}")

    # 👇 Analyse comportementale automatisée avec ShadowSignalEngine
    signal_engine = ShadowSignalEngine()
    for match_id, match_data in all_matches_data.items():
        if "error" in match_data:
            logger.error(f"Erreur lors de la collecte des données pour le match {match_id}: {match_data['error']}")
            continue

        signal_result = signal_engine.analyze(match_data)
        logger.info(f"[Signals] Résultat pour {match_id}: {signal_result}")

        # (Optionnel) : sauvegarder le signal_output.json pour chaque match
        import os, json
        output_dir = "outputs/signals/"
        os.makedirs(output_dir, exist_ok=True)
        with open(f"{output_dir}signal_{match_id}.json", "w") as f:
            json.dump(signal_result, f, indent=2, ensure_ascii=False)

    # ... (reste du pipeline : modules métiers, fusion, etc.)

if __name__ == '__main__':
    main()
