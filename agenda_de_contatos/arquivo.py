import json
from contato import Contato

def salvar_contatos(agenda):
    dados = []
    for contato in agenda.contatos:
        dados.append({
            'nome': contato.nome,
            'telefone': contato.telefone,
            'email': contato.email
        })
    
    try:
        with open('contatos.txt', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def carregar_contatos(agenda):
    try:
        with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
        for item in dados:
            agenda.adicionar(item['nome'], item['telefone'], item['email'])
            
    except FileNotFoundError:
        print("Arquivo de contatos não encontrado. Iniciando agenda vazia.")
    except Exception as e:
        print(f"Erro ao carregar contatos: {e}")