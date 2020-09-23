

def test_requests_returns_404(client):
    assert client.get("/url_nao_existe").status_code == 404