from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='database',
                            database='WPAGE',
                            user='test',
                            password='toto', port='9000')
    return conn

@app.route('/')
def index():
    connection = get_db_connection()
    # Création du curseur
    cursor = connection.cursor()
    # Récupération des éléments html en bd
    html_elms = cursor.fetchall()
    # Fermeture du curseur et de la connection
    cursor.close()
    connection.close()
    
    return render_template('index.html', data=html_elms)

app.run(host='0.0.0.0', port=8000)