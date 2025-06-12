import argparse
import logging
import yaml
import os

from core.shadow_odds import ShadowOddsEngine
from core.arcanx import ArcanXEngine
from core.sentinel_live import ArcanSentinelLive
from core.pocs import ArcanPOCS
from core.khawatim import Khawatim
from utils.helpers import InsightManager, TriggerSet, PredictionEvaluator

# ✅ Import du hub d'intégration et des modules Orchestrator/FusionEngine
from data_integration.data_integration_hub import DataIntegrationHub
from data_integration.orchestrator import DataOrchestrator
from data_integration.fusion_engine import FusionEngine

# Initialisation du logger
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

    # ✅ Initialisation du DataIntegrationHub
    data_hub = DataIntegrationHub()
    if hasattr(data_hub, "get_available_adapters"):
        available_sources = data_hub.get_available_adapters()
        logger.info(f"Sources de données disponibles : {available_sources}")

    modules = initialize_modules(settings)

    logger.info("Démarrage de l'analyse pour le match: %s", args.match_id)

    insights = InsightManager.collect(args.match_id)
    triggers = TriggerSet.generate(args.match_id)

    # ✅ Exemple de récupération via un adaptateur (OpenAPI)
    if hasattr(data_hub, "fetch_data"):
        openapi_matches = data_hub.fetch_data('openapi', args.match_id)
        if openapi_matches:
            logger.info(f"[DataHub] Données OpenAPI reçues pour {args.match_id}")
    else:
        openapi_matches = None

    # ✅ Exemple d'intégration DataOrchestrator
    orchestrator = DataOrchestrator()
    try:
        orchestrator_result = orchestrator.fuse(source="bet365", match_id=args.match_id)
        logger.info(f"[Orchestrator] Données Bet365 reçues : {orchestrator_result}")
    except Exception as e:
        logger.warning(f"[Orchestrator] Impossible de récupérer Bet365 : {e}")

    # ✅ Exemple d'intégration FusionEngine (multi-sources)
    fusion_engine = FusionEngine()
    try:
        fusion_result_multi = fusion_engine.fuse_all(match_id=args.match_id, sources=["bet365", "soccerdata", "whoscored"])
        logger.info(f"[FusionEngine] Fusion multi-source : {fusion_result_multi}")
    except Exception as e:
        logger.warning(f"[FusionEngine] Impossible de fusionner les sources : {e}")

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
