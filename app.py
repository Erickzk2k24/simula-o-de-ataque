from flask import Flask, render_template, request, Response
import os
import time
from threading import Thread
from ransomware.ransoware import simulate_ransomware

app = Flask(__name__)

# Função para simular o ransomware e retornar resultados progressivos
def simulate_ransomware_progress(directory):
    system_info = simulate_ransomware(directory)

    # Simula o progresso do ataque, enviando atualizações a cada passo
    for i in range(5):
        time.sleep(1)  # Simula o tempo de execução do ataque
        yield f"data: Progresso: Etapa {i + 1} completada...\n\n"

    # Após terminar, envia o relatório completo
    yield f"data: Simulação concluída. {system_info}\n\n"

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota que envia as atualizações do progresso via SSE
@app.route('/simulate', methods=['POST'])
def simulate():
    directory = request.form['directory']

    # Retorna uma resposta SSE (Server-Sent Events) para o frontend
    return Response(simulate_ransomware_progress(directory), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    # O parâmetro 'threaded=True' permite que o Flask trate várias requisições simultaneamente
    # Isso é útil para simular o ransomware em múltiplos diretórios ao mesmo tempo, se necessário.      
# Lembre-se de que este código é apenas para fins educacionais e não deve ser usado para atividades maliciosas.
# O uso de ransomware é ilegal e antiético. Sempre obtenha permissão antes de testar qualquer software em sistemas que não sejam seus.
# Este código é uma simulação e não deve ser usado para fins maliciosos. Use com responsabilidade.