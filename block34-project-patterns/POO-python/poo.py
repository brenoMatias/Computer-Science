class Liquidificador:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__amperagem_atual_no_motor = 0

# O primeiro parâmetro, o self, representa a instância do objeto, ou seja, tem acesso ao objeto na memória. Com o método init, inicializamos os atributos do objeto apenas atribuindo um valor a cada nova chave.
# Exemplo: self.ligado = False.


#Os próximos parâmetros são os que permitem criar de forma customizada nosso objeto, como a cor: self._cor = cor.


#Agora podemos criar nossos primeiros liquidificadores:
liquidificador_azul = Liquidificador('Azul', 200, 127, 200)
liquidificador_vermelho = Liquidificador('Vermelho', 250, 220, 300)

# Perceba que é possível ter atributos que não precisam ser passados por parâmetros na chamada do construtor, por exemplo: os booleanos __ligado e __velocidade, pois o construtor vai iniciá-los sempre com um valor padrão, nestes casos, False e 0, respectivamente.

print(liquidificador_azul)
