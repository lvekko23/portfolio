from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# ---  CLAVE API ---
API_KEY = "AIzaSyCJb_loDx_uCgKcRmS5o5Eh7G7frKv5Ibo"

# Configuramos la IA
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-flash-latest')
    print("✅ IA Configurada correctamente")
except Exception as e:
    print(f"❌ Error al configurar la IA: {e}")

# --- CONTEXTO DEL ROBOT ---
CONTEXTO = """
Sos "ValenBot", el asistente virtual del portfolio de Valentino Ciancio.
Tu objetivo es vender sus servicios de Desarrollo Web.
Respondé corto, canchero y profesional.

Datos de Valentino:
- Desarrollador Full Stack (Python, Flask, HTML, CSS).
- Vive en Luján, Buenos Aires.
- Creó los sistemas de Indumar S.A. y SGA Fumigaciones.
- Hace webs rápidas y sin abonos mensuales.
- Contacto: WhatsApp +54 9 2323 357985.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"response": "No entendí, ¿me repetís?"})

    try:
        # Iniciamos chat
        chat_session = model.start_chat(history=[])
        prompt = f"{CONTEXTO}\n\nUsuario: {user_message}\nValenBot:"
        
        response = chat_session.send_message(prompt)
        return jsonify({"response": response.text})
    
    except Exception as e:
        
        print(f"\n⚠️ ERROR DE IA: {e}\n") 
        return jsonify({"response": "Uy, me maríe. Escribile a Valen al WhatsApp mejor."})

if __name__ == '__main__':
    app.run(debug=True)