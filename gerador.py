import random
import os
import time
import requests
import sys

def show_credits():
    clear()
    print("\n\n")
    print("""
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

    if response.status_code == 200:
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
    first_names = ["João", "Maria", "Carlos", "Ana", "Pedro", "Carla", "Lucas", "Beatriz"]
    last_names = ["Silva", "Oliveira", "Santos", "Pereira", "Costa", "Almeida", "Souza", "Mendes"]
    streets = ["Rua 1", "Avenida Central", "Rua das Flores", "Rua Nova", "Avenida Brasil", "Rua dos Trilhos"]
    cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Fortaleza", "Salvador", "Curitiba"]
    states = ["SP", "RJ", "MG", "CE", "BA", "PR"]
    emails = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com"]
    phones = ["9" + str(random.randint(100000000, 999999999))]
    rg_numbers = [random.randint(100000000, 999999999)]
    
    # Gerar dados
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    cpf = generate_cpf()
    address = f"{random.choice(streets)}, {random.randint(1, 100)} - {random.choice(cities)} - {random.choice(states)}"
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(emails)}"
    phone = random.choice(phones)
    rg = random.choice(rg_numbers)
    dob = f"{random.randint(1, 31):02d}/{random.randint(1, 12):02d}/{random.randint(1980, 2000)}"
    gender = random.choice(["Masculino", "Feminino", "Outro"])

    fake_data = {
        "Nome": full_name,
        "CPF": cpf,
        "Endereço": address,
        "Email": email,
        "Telefone": phone,
        "Data de Nascimento": dob,
        "RG": rg,
        "Sexo": gender
    }

    return fake_data

def fake_data_generator():
    clear()
    print("💻 GERADOR DE DADOS FALSOS 💻")
    fake_data = generate_fake_data()
    for key, value in fake_data.items():
        print(f"🔹 {key}: {value}")
    input("\nPressione ENTER para voltar...")

def bin_lookup():
    clear()
    print("🔎 BIN LOOKUP 🔎\n")
    bin_number = input("Digite os 6 primeiros números do cartão (BIN): ")
    url = f"https://lookup.binlist.net/{bin_number}"
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if "bank" in data:
            print(f"\n🔹 Banco: {data['bank']['name']}")
            print(f"🔹 Tipo de Cartão: {data['type']}")
            print(f"🔹 Marca: {data['brand']}")
            print(f"🔹 País: {data['country']['name']}")
        else:
            print("\n❌ BIN não encontrado ou inválido.")
    except Exception as e:
        print(f"\n❌ Erro ao acessar a API: {str(e)}")

    input("\nPressione ENTER para voltar...")

while True:
    clear()
    print("""
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
    [4] BIN LOOKUP 🔎
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
        bin_lookup()
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
