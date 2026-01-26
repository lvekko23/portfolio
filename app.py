from flask import Flask, render_template

app = Flask(__name__)

# --- RUTA PRINCIPAL ---
@app.route('/')
def home():
    return render_template('index.html')

# --- ARRANQUE ---
if __name__ == '__main__':
    app.run(debug=True)