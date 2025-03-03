import random
import os
import time
import requests
import sys

def falling_letters(text, delay=0.05):
    """
    Função para exibir as letras caindo de cima para baixo no terminal.
    """
    for i in range(len(text)):
        sys.stdout.write(text[i])  # Escreve a letra atual
        sys.stdout.flush()  # Força a atualização da tela
        time.sleep(delay)  # Pausa entre as letras
    print()  # Pula para a próxima linha após o texto

def show_credits():
    clear()
    print("\n\n")
    falling_letters("""
    ─────────────────────────────────────
      🔥 PAINEL DE GERADORES - DedSec.py 🔥
      Criado por: DedSec.py
      Desenvolvido para iSH Shell / Termux
    ─────────────────────────────────────
    """)
    input("Pressione ENTER para voltar...")

def clear():
    os.system("clear")

def generate_cpf():
    cpf = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
    return cpf

def generate_cc():
    cc_number = random.randint(1000000000000000, 9999999999999999)
    expiration_month = random.randint(1, 12)
    expiration_year = random.randint(23, 30)
    cvv = random.randint(100, 999)
    return cc_number, expiration_month, expiration_year, cvv

def checker_cc(cc_number):
    print(f"\n🔍 Verificando o CC: {cc_number}")
    time.sleep(2)
    print("✅ CC válido! (Simulação)\n")

def generate_email():
    user = f"user{random.randint(1000, 9999)}"
    domain = "1secmail.com"
    return user, f"{user}@{domain}"

def check_inbox(user):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain=1secmail.com"
    response = requests.get(url)

    if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
        try:
            messages = response.json()
            if messages:
                print("\n📩 MENSAGENS RECEBIDAS 📩")
                for mail in messages:
                    print(f"\n🔹 De: {mail['from']}")
                    print(f"🔹 Assunto: {mail['subject']}")
                    print(f"🔹 ID: {mail['id']}")
            else:
                print("\n📭 Nenhuma mensagem encontrada!")
        except ValueError:
            print("\n❌ Erro ao processar a resposta da API.")
    else:
        print(f"\n❌ Erro ao acessar a API: {response.status_code}")

    input("\nPressione ENTER para voltar...")

def email_temp():
    clear()
    print("📧 GERADOR DE EMAIL TEMPORÁRIO 📧\n")
    
    user, email = generate_email()
    print(f"🔹 E-mail Gerado: {email}")

    while True:
        print("\n[1] Ver Caixa de Entrada 📩")
        print("[00] Voltar ❌")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            check_inbox(user)
        elif opcao == "00":
            break
        else:
            print("\n❌ Opção inválida!")

def generate_fake_data():
    """
    Função para gerar dados aleatórios (nome, idade, endereço, etc.).
    """
    first_names = ["João", "Maria", "Carlos", "Ana", "Pedro", "Carla", "Lucas", "Beatriz"]
    last_names = ["Silva", "Oliveira", "Santos", "Pereira", "Costa", "Almeida", "Souza", "Mendes"]
    streets = ["Rua 1", "Avenida Central", "Rua das Flores", "Rua Nova", "Avenida Brasil", "Rua dos Trilhos"]
    cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Fortaleza", "Salvador", "Curitiba"]
    states = ["SP", "RJ", "MG", "CE", "BA", "PR"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    age = random.randint(18, 80)
    street = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

    fake_data = {
        "Nome": f"{first_name} {last_name}",
        "Idade": age,
        "Endereço": f"{street}, {city} - {state}",
        "CEP": zip_code
    }

    return fake_data

def fake_data_generator():
    clear()
    print("💻 GERADOR DE DADOS FALSOS 💻")
    fake_data = generate_fake_data()
    for key, value in fake_data.items():
        print(f"🔹 {key}: {value}")
    input("\nPressione ENTER para voltar...")

while True:
    clear()
    falling_letters("""
    ██████╗ ██████╗  ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║
    ██████╔╝██████╔╝██║  ███╗█████╗  ██╔██╗ ██║
    ██╔═══╝ ██╔═══╝ ██║   ██║██╔══╝  ██║╚██╗██║
    ██║     ██║     ╚██████╔╝███████╗██║ ╚████║
    ╚═╝     ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    
    🔥 Painel desenvolvido por DedSec.py 🔥
    """)

    print("""
    [1] GERAR CC E CPF 💳
    [2] CHECKER CC 🔍
    [3] GERAR EMAIL TEMPORÁRIO 📧
    [4] CRÉDITOS ✨
    [5] GERADOR DE DADOS FALSOS 💻
    [00] SAIR ❌
    """)

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cc_number, expiration_month, expiration_year, cvv = generate_cc()
        cpf = generate_cpf()
        print(f"\n🔹 CC Gerado: {cc_number}")
        print(f"🔹 Validade: {expiration_month}/{expiration_year}")
        print(f"🔹 CVV: {cvv}")
        print(f"🔹 CPF: {cpf}\n")
        input("Pressione ENTER para voltar...")
    elif opcao == "2":
        cc_number = input("Digite o número do CC para verificação: ")
        checker_cc(cc_number)
    elif opcao == "3":
        email_temp()
    elif opcao == "4":
        show_credits()
    elif opcao == "5":
        fake_data_generator()
    elif opcao == "00":
        clear()
        print("Saindo do sistema...")
        time.sleep(1)
        break
    else:
        print("\n❌ Opção inválida! Tente novamente.")
        time.sleep(1)
