from src.app import app

def test_listar_tarefas():
    cliente = app.test_client()
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200