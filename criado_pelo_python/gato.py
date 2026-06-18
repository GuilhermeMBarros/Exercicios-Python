class Gato:
    def __init__(self,raca: str,cor: str,tipo_pelo: str,idade: int,nome: str):
        """
        Docstring for __init__
        
        :param self: Comando que faz os atributos e métodos olharem para classe
        :param raca: Digite a raça do gato
        :type raca: str
        :param cor: Digite a cor do gato
        :type cor: str
        :param tipo_pelo: Digite o tipo de pelo(Sem pelo, Pelo longo, Pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idade do gato com um número inteiro
        :type idade: int
        :param nome: Digite o nome do gato
        :type nome: str
        """
        self.nome = nome
        self.idade = idade
        self.tipo_pelo = tipo_pelo
        self.cor = cor
        self.raca = raca

    def miar(self):
        print(f"O {self.nome} miou")

meu_gato = Gato("Angorá" , "Branco" , "Sem pelo" , 17 , "Pedro")
meu_gato.miar()