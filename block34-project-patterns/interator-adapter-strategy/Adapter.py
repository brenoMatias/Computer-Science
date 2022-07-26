# Ao analisar os códigos do sistema, já deparamos com um exemplo de classe que analisa o relatório e realiza um cálculo de média. Nota-se que o método average() espera que o retorno de load_data() contenha estruturas dict.

class ReportAnalyzer:
    def __init__(self, loader):
        self.loader = loader

    def average(self):
        # este é um dos métodos que espera uma lista de dicionários
        data = self.loader.load_data()
        # aqui ela soma o valor na chave final_price em cada item da lista
        total = sum(order['final_price'] for order in data)
        return total / len(data)


# Pelo que foi comentado na reunião, a nova ferramenta (gerenciator3000) não retorna uma estrutura com dicionários, o que é comprovado ao realizar os print de seu retorno:
# Código exemplo para simular a API Gerenciator3000
class ReportLoader:
    def __init__(self):
        self.headers = ["id", "date", "final_price"]
        self.rows = [
            [1337, "2020-11-20", 2350.5],
            [1338, "2020-11-21", 4800.5],
        ]

loader = ReportLoader()
print(loader.headers)  # ['id', 'date', ..., 'final_price']
print(loader.rows[0])  # [1337, '2020-11-20', ..., 2350.5]


# SOLUÇÃO
# O time decidiu fazer uma classe responsável por "traduzir" esses dados do formato da ferramenta para o formato do sistema utilizado pela companhia
# essa classe poderá ser acoplada na ferramenta de relatórios

class G3000LoaderAdapter:
    # aqui o loader é uma instancia do gerenciator3000.ReportLoader original
    def __init__(self, loader):
        self.loader = loader

    def load_data(self):

        # Em python, o zip() junta uma lista de chaves em uma lista de valores
        # e permite criar dicionário! Por exemplo:
        # dict(zip(['nome', 'idade'], ['Juliana', 27]))
        # {'nome': 'Juliana', 'idade': 27}

        data = []
        for row in self.loader.rows:
            data.append(dict(zip(self.loader.headers, row)))
        return data


g3000_loader = ReportLoader()
loader = G3000LoaderAdapter(g3000_loader)
# o analyzer do nosso sistema recebe o adaptador como qualquer outro loader
analyzer = ReportAnalyzer(loader)
analyzer.average()  # Agora funcionará