from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()
    nova_tarefa = {
       "id": len(tarefas) + 1,
       "titulo": dados["titulo"],
       "descricao": dados.get("descricao", ""),
       "status": "pendente",
       "prioridade": dados.get("prioridade", "Média")  # valor padrão
}
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            dados = request.get_json()
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["descricao"] = dados.get("descricao", tarefa["descricao"])
            tarefa["status"] = dados.get("status", tarefa["status"])
            tarefa["prioridade"] = dados.get("prioridade", tarefa["prioridade"])
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def remover_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida com sucesso"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
