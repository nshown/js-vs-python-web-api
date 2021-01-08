from flask import Flask, jsonify
import sqlite3
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am a Python Flask Web API server and I will serve you data!"


@app.route("/simple-json")
def json_from_dict():
    english_to_spanish_dict = [{"spanish_color": "rojo", "english_color":"red"},
                    {"spanish_color": "amarillo", "english_color":"yellow"},
                    {"spanish_color": "verde", "english_color":"green"},
                    {"spanish_color": "azul", "english_color":"blue"},
                    {"spanish_color": "rosa", "english_color":"pink"}]
    return jsonify(english_to_spanish_dict)


@app.route("/sqlite-json")
def json_from_sqlite():
    table_name = "spanish_to_english"
    conn = sqlite3.connect('sp_to_en_color.db')

    cursor = conn.cursor()

    cursor.execute(f'''SELECT SPANISH_COLOR, ENGLISH_COLOR from {table_name}''')

    results = cursor.fetchall()
    result_dicts = [ {"spanish_color": result[0], "english_color": result[1]} for result in results]

    conn.close()

    return jsonify(result_dicts)


@app.route("/paused-json")
def json_from_paused_dict():
    # Wait for 3 seconds
    time.sleep(3)

    english_to_spanish_dict = [{"spanish_color": "rojo", "english_color":"red"},
                    {"spanish_color": "amarillo", "english_color":"yellow"},
                    {"spanish_color": "verde", "english_color":"green"},
                    {"spanish_color": "azul", "english_color":"blue"},
                    {"spanish_color": "rosa", "english_color":"pink"}]
    return jsonify(english_to_spanish_dict)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
