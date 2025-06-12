from orchestrator.batch_orchestrator import BatchDataOrchestrator

def test_collect_all_for_matches():
    batch = BatchDataOrchestrator()
    match_ids = ["test1", "test2"]
    result = batch.collect_all_for_matches(match_ids)

    assert isinstance(result, dict)
    assert len(result) == len(match_ids)

    for match_id, data in result.items():
        assert isinstance(data, dict)
