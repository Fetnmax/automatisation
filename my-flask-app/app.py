from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon application Flask déployée par Jenkins !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)