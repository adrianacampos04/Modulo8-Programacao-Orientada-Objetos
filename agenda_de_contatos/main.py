from agenda import Agenda
from arquivo import salvar_contatos, carregar_contatos

def menu():
    print("\n" + "="*40)
    print("    📱 AGENDA DE CONTATOS 📱")
    print("="*40)
    print("1. 📝 Adicionar contato")
    print("2. 📋 Listar contatos")
    print("3. 🔍 Buscar contato")
    print("4. ✏️  Editar contato")
    print("5. 🗑️  Remover contato")
    print("6. 🚪 Sair")
    print("="*40)

def main():
    # Criar instância da agenda
    agenda = Agenda()
    
    # Carregar contatos salvos
    carregar_contatos(agenda)
    print("Agenda carregada com sucesso!")
    
    while True:
        menu()
        opcao = input("👉 Escolha uma opção: ")
        
        if opcao == "1":
            print("\n📝 ADICIONAR NOVO CONTATO")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            
            if nome and telefone:  # Validação básica
                agenda.adicionar(nome, telefone, email)
                salvar_contatos(agenda)
                print("✅ Contato adicionado com sucesso!")
            else:
                print("❌ Nome e telefone são obrigatórios!")
        
        elif opcao == "2":
            agenda.listar()
        
        elif opcao == "3":
            termo = input("🔍 Digite nome, telefone ou email para buscar: ")
            if termo:
                agenda.buscar(termo)
            else:
                print("❌ Digite algo para buscar!")
        
        elif opcao == "4":
            agenda.listar()
            if agenda.contatos:
                try:
                    indice = int(input("Digite o número do contato para editar: ")) - 1
                    agenda.editar(indice)
                    salvar_contatos(agenda)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
        
        elif opcao == "5":
            agenda.listar()
            if agenda.contatos:
                try:
                    indice = int(input("Digite o número do contato para remover: ")) - 1
                    agenda.remover(indice)
                    salvar_contatos(agenda)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
        
        elif opcao == "6":
            print("👋 Saindo... Até logo!")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()