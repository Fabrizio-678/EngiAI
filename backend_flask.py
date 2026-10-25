from flask import Flask, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('EngiAI',
    read_only=True,
    preprocessors=[], # Al dejarlo vacío evitas que elimine los \n al procesar
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'No estoy seguro de esa mecánica todavía, pero recuerda: la fábrica debe crecer.',
        'maximum_similarity_threshold': 0.65
}])

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():
    datos = request.get_json()
    mensaje_usuario = datos.get("message", "")

    if not mensaje_usuario:
        return jsonify({"error": "Mensaje vacío"}), 400

    respuesta_bot = str(bot.get_response(mensaje_usuario))
    respuesta_bot = respuesta_bot.replace("[[NL]]", "\n")
    return jsonify({"response": respuesta_bot})

if __name__ == "__main__":
    app.run(port=5000, debug=True)