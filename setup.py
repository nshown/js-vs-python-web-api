#This setup file creates a sqlite database 
import sqlite3
conn = sqlite3.connect('sp_to_en_color.db')

cursor = conn.cursor()

table_name = "spanish_to_english"
sp_to_en_colors = [{"spanish_color": "rojo", "english_color":"red"},
                    {"spanish_color": "naranja", "english_color":"orange"},
                    {"spanish_color": "amarillo", "english_color":"yellow"},
                    {"spanish_color": "verde", "english_color":"green"},
                    {"spanish_color": "azul", "english_color":"blue"},
                    {"spanish_color": "marron", "english_color":"brown"},
                    {"spanish_color": "negro", "english_color":"black"},
                    {"spanish_color": "gris", "english_color":"grey"},
                    {"spanish_color": "blanco", "english_color":"white"},
                    {"spanish_color": "rosa", "english_color":"pink"}]

cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

sql_query = f'''CREATE TABLE {table_name}(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   SPANISH_COLOR        CHAR(50),
   ENGLISH_COLOR        CHAR(50)
);
'''

cursor.execute(sql_query)
conn.commit()
print("Table created successfully........")


for sp_to_en_color in sp_to_en_colors:
    cursor.execute(f'''INSERT INTO {table_name}(
    SPANISH_COLOR, ENGLISH_COLOR) VALUES 
    ('{sp_to_en_color["spanish_color"]}', '{sp_to_en_color["english_color"]}')''')

conn.commit()
print("Data added successfully........")

cursor.execute(f'''SELECT * from {table_name}''')

results = cursor.fetchall()
print(results)

conn.close()