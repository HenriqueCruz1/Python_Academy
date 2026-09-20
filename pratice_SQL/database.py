
import psycopg

conexao = psycopg.connect(
    "host=localhost dbname=exercicio_sql user=postgres password=??"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

print(clientes)