def test_capital_india(llm_client):
    assert llm_client.ask("Capital of India") == "New Delhi"


def test_capital_france(llm_client):
    assert llm_client.ask("Capital of France") == "Paris"
