

def test_requests_retorna_404(client):
    assert client.get("/url_nao_existe").status_code == 404

def test_config_foi_carregada(config):
    assert config["DEBUG"] is False

