from contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
    
    def listar(self):
        if not self.contatos:
            print("Agenda vazia!")
            return
        
        print("\n=== LISTA DE CONTATOS ===")
        for i, contato in enumerate(self.contatos, 1):
            print(f"{i}. {contato}")
    
    def buscar(self, termo):
        encontrados = []
        termo = termo.lower()
        
        for contato in self.contatos:
            if (termo in contato.nome.lower() or 
                termo in contato.telefone or 
                termo in contato.email.lower()):
                encontrados.append(contato)
        
        if encontrados:
            print(f"\n=== RESULTADOS DA BUSCA ===")
            for i, contato in enumerate(encontrados, 1):
                print(f"{i}. {contato}")
        else:
            print("Nenhum contato encontrado!")
    
    def remover(self, indice):
        if 0 <= indice < len(self.contatos):
            contato_removido = self.contatos.pop(indice)
            print(f"Contato '{contato_removido.nome}' removido com sucesso!")
        else:
            print("Índice inválido!")
    
    def editar(self, indice):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos[indice]
            print(f"Editando: {contato}")
            
            novo_nome = input(f"Novo nome (atual: {contato.nome}): ") or contato.nome
            novo_telefone = input(f"Novo telefone (atual: {contato.telefone}): ") or contato.telefone
            novo_email = input(f"Novo email (atual: {contato.email}): ") or contato.email
            
            contato.nome = novo_nome
            contato.telefone = novo_telefone
            contato.email = novo_email
            
            print("Contato editado com sucesso!")
        else:
            print("Índice inválido!")