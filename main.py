import argparse
import logging
import yaml

from core.shadow_odds import ShadowOddsEngine
from core.arcanx import ArcanXEngine
from core.sentinel_live import ArcanSentinelLive
from core.pocs import ArcanPOCS
from core.khawatim import Khawatim
from utils.helpers import InsightManager, TriggerSet, PredictionEvaluator

# ✅ Import du DataOrchestrator
from orchestrator.data_orchestrator import DataOrchestrator

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
    parser.add_argument('--match_id', type=str, help="ID du match à analyser", required=True)
    parser.add_argument('--live', action='store_true', help="Activer le mode live pour ArcanSentinel")
    args = parser.parse_args()

    settings = load_settings()

    modules = initialize_modules(settings)

    logger.info("Démarrage de l'analyse pour le match: %s", args.match_id)

    # ✅ Collecte centralisée des données via DataOrchestrator
    orchestrator = DataOrchestrator()
    all_data = orchestrator.collect_match_data(args.match_id)
    logger.info(f"[Orchestrator] Données agrégées pour {args.match_id} : {all_data}")

    # Tu peux maintenant extraire des données agrégées pour chaque module, par exemple :
    bet365_data = all_data.get("bet365", {})
    whoscored_data = all_data.get("whoscored", {})
    # ... etc.

    # Si tu utilises toujours InsightManager/TriggerSet, tu peux les alimenter avec ces données ou continuer comme avant
    insights = InsightManager.collect(args.match_id)
    triggers = TriggerSet.generate(args.match_id)

    predictions = []

    if 'shadow_odds' in modules:
        predictions.append(modules['shadow_odds'].predict(args.match_id, insights, triggers))

    if 'arcanx' in modules:
        predictions.append(modules['arcanx'].predict(args.match_id, insights))

    if 'sentinel' in modules and args.live:
        predictions.append(modules['sentinel'].monitor_live(args.match_id))

    if 'pocs' in modules:
        predictions.append(modules['pocs'].generate_meta_prediction(args.match_id))

    if 'khawatim' in modules:
        predictions.append(modules['khawatim'].invoke(args.match_id))

    logger.info("Évaluation et fusion des prédictions...")
    fusion_result = PredictionEvaluator.fuse(predictions)
    logger.info("Résultat final : %s", fusion_result)

if __name__ == '__main__':
    main()
