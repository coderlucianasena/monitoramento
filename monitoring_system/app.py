from flask import Flask, render_template, jsonify
import paramiko
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

hostname = '192.168.2.51'
caminho_chave_privada = '/caminho/para/sua/chave_privada.pem' 

def inserir_dados_no_banco(cpu, disk, memory):
    try:
        db_connection = sqlite3.connect('monitoring.db')
        db_cursor = db_connection.cursor()

        db_cursor.execute("INSERT INTO cpu (usage, timestamp) VALUES (?, ?)", (cpu, datetime.now()))
        db_cursor.execute("INSERT INTO disco (usage, timestamp) VALUES (?, ?)", (disk, datetime.now()))
        db_cursor.execute("INSERT INTO memoria (usage, timestamp) VALUES (?, ?)", (memory, datetime.now()))

        db_connection.commit()
        db_connection.close()
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados', methods=['GET'])
def dados():
    try:

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_key = paramiko.RSAKey(filename=caminho_chave_privada)

        ssh_client.connect(hostname, pkey=ssh_key)

        comando_cpu = 'top -n 1 | grep "Cpu(s)" | awk \'{print $2}\''
        comando_disco = 'df -h / | tail -n 1 | awk \'{print $5}\''
        comando_memoria = 'free -m | grep "Mem:" | awk \'{print $3/$2 * 100}\''

        stdin, stdout, stderr = ssh_client.exec_command(comando_cpu)
        output_cpu = int(stdout.read().decode('utf-8'))

        stdin, stdout, stderr = ssh_client.exec_command(comando_disco)
        output_disco = int(stdout.read().decode('utf-8'))

        stdin, stdout, stderr = ssh_client.exec_command(comando_memoria)
        output_memoria = int(stdout.read().decode('utf-8'))

        inserir_dados_no_banco(output_cpu, output_disco, output_memoria)

        ssh_client.close()

        return jsonify({'cpu': output_cpu, 'disk': output_disco, 'memory': output_memoria})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
