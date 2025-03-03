import random
import os
import time
import requests

def show_credits():
    clear()
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
    
    [1] GERAR CC E CPF 💳
    [2] CHECKER CC 🔍
    [3] GERAR EMAIL TEMPORÁRIO 📧
    [4] CRÉDITOS ✨
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
    elif opcao == "7":
        show_credits()
    elif opcao == "00":
        clear()
        print("Saindo do sistema...")
        time.sleep(1)
        break
    else:
        print("\n❌ Opção inválida! Tente novamente.")
        time.sleep(1)
