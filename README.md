# O que é Programação Orientada a Objetos? 

# DEFINIÇÂO:

POO é um paradigma de programação que organiza o código em "objetos", que são instâncias de "classes".
Foca na criação de objetos que contêm dados (atributos) e comportamentos (métodos).
Os principais pilares da POO são:

- Abstração – Simplificar a representação do mundo real.
- Encapsulamento – Proteger os dados e expor apenas o necessário.
- Herança – Reutilizar e estender o comportamento de classes.
- Polimorfismo – Tratar objetos de diferentes classes de forma uniforme.

➡️ Vantagens:

✅ Reutilização de código.
✅ Maior organização e modularidade.
✅ Facilidade de manutenção e escalabilidade.

# Classes e Objetos:

- Uma classe é um modelo (ou blueprint) para criar objetos.
- Define os atributos (dados) e métodos (comportamentos).

EXEMPLO PRÁTICO:

python

CopyEdit
class Carro:
     def _ _init_ _(self, marca, modelo):
           self.marca = marca
           self.modelo = modelo

     def exibir_info(self):
            return f"{self.marca} {self.modelo}"

# Objeto:

-Um objeto é uma instância de uma classe.
-Os atributos e métodos definidos na classe ficam disponíveis no objeto.

Exemplo:
python

CopyEdit
meu_carro = Carro("Toyota", "Corolla")
 print(meu_carro.exibir_info()) # Saída: Toyota Corolla

# Método _ _init_ _ e Atributos

Método _ _init_ _

- O método _ _init_ _ é o construtor da classe.
- É chamado automaticamente quando um objeto é criado.
- Define os valores iniciais dos atributos do objeto.

# Atributos:

- Os atributos pertencem a um objeto e armazenam valores associados a ele.
- São acessados com self.

