# Classe para armazenar os dados do novo usuário
# Class to save the new user informations
class DadosCadastrados: 
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.personagem = ""

# Classe para a lista de personagens disponíveis
# Class about the list of characters available
class ListaPersonagem:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

# Uma função para escolher/criar o seu personagem
# A function to choose/create your character

def CriarPersonagem(p1, p2, p3, p4, Personagem, FinalizarEscolha):
        print("""
        p1 - Mago Vermelho
        p2 - Cavaleiro do Submundo
        p3 - Fada de Luz
        p4 - Arqueira Gelada
        """)
        Personagem = input("Sua escolha: ")
        if Personagem == 'p1':
            Personagem = Personagens.p1
            print("Você escolheu o MAGO VERMELHO!")
            FinalizarEscolha = input("""Confirma o personagem escolhido? 
        sim
        não
        insira:""")
            if FinalizarEscolha == 'sim':
                Dados_Usuario1.personagem = Personagem
                print("Seu personagem agora é o {}".format(Personagens.p1))

        if Personagem == 'p2':
            Personagem = Personagens.p2
            print("Você escolheu o CAVALEIRO DO SUBMUNDO!")
            FinalizarEscolha = input("""Confirma o personagem escolhido?
                                    sim
                                    não
                                    insira: 
                                    """)
            if FinalizarEscolha == 'sim':
                Dados_Usuario1.personagem = Personagem
                print("Seu personagem agora é o {}".format(Personagens.p2))
                
                


        if Personagem == 'p3':
            Personagem = Personagens.p3
            print("Você escolheu o FADA DE LUZ!!")
            FinalizarEscolha = input("""Confirma o personagem escolhido?
                                    sim
                                    não
                                    insira: 
                                    """)
            if FinalizarEscolha == 'sim':
                Dados_Usuario1.personagem = Personagem
                print("Seu personagem agora é o {}".format(Personagens.p3))


        if Personagem == 'p4':
            Personagem = Personagens.p4
            print("Você escolheu o ARQUEIRA GELADA!")
            FinalizarEscolha = input("""Confirma o personagem escolhido?
                            sim
                            não
                            insira: """)
            if FinalizarEscolha == 'sim':
                Dados_Usuario1.personagem = Personagem
                print("Seu personagem agora é o {}".format(Personagens.p4))


# Parâmetros para a classe de lista dos personagens
# Parameters about the list of characters class
p1 = 'Mago Vermelho'
p2 = 'Cavaleiro do Submundo'
p3 = 'Fada de Luz'
p4 = 'Arqueira Gelada'
Personagem = ""
FinalizarEscolha = ""

# Solicitar as informações para cadastro do usuário
# Asking the user his informations
print("""
Seja bem-vindo ao SkrymForest - RPG
INICIE O SEU CADASTRO ABAIXO!!
""")
nome = str(input("Nome: "))
idade = int(input("Idade: "))
email = str(input("Email: "))
telefone = int(input("Telefone: "))

# Criando um novo usuario baseado nas informações passadas pelo novo usuario
# Creating a new user based on the informations he types
Dados_Usuario1 = DadosCadastrados(nome, idade, email, telefone)

# Parametros para a função construtora dentro da classe ListaPersonagem
# Parameters for the constructor function inside ListaPersonagem(list of characters) class
Personagens = ListaPersonagem(p1,p2,p3,p4)


# Checando se o usuário cadastrado tem mais ou menos de 18 para jogar
# Checking if the user has more or less than 18 to play 
if Dados_Usuario1.idade < 18:
    print("Apenas para maiores de 18 :/")
elif Dados_Usuario1.idade >= 18:
    print("""
          Seja bem-vindo!!
          ESCOLHA SEU PERSONAGEM:
          """)
    CriarPersonagem(p1,p2,p3,p4,Personagem,FinalizarEscolha)

    







        