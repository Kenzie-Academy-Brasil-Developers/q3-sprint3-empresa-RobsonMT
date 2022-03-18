# Desenvolva todas as suas classes aqui


from ctypes import Union


class Funcionario(object):
    def __init__(
        self, nome: str, sobrenome: str, cpf: str, salario: int = 3000
    ) -> None:
        self.nome = nome.strip().capitalize()
        self.sobrenome = " ".join(sobrenome.split()).title()
        self.cpf = cpf
        self.salario = salario
        self.nome_completo: str = f"{self.nome} {self.sobrenome}"

    @staticmethod
    def funcao():
        return "Funcionario"

    def __repr__(self):
        return "<%s: %s>" % ("Funcionario", self.nome_completo)

    def __str__(self):
        return "<%s: %s>" % ("Funcionario", self.nome_completo)


#


class Empresa(object):
    def __init__(self, nome: str, cnpj: str, contratados: list = list()) -> None:
        self.nome = " ".join(nome.split()).title()
        self.cnpj = cnpj
        self.contratados = contratados

    def __repr__(self):
        return "<%s: %s>" % ("Empresa", self.nome)

    def __str__(self):
        return "<%s: %s>" % ("Empresa", self.nome)

    def __getattribute__(self, item):
        # print("__getattribute__", item)
        return super(Empresa, self).__getattribute__(item)

    def __getattr__(self, item):
        # print("__getattr__ ", item)
        return super(Empresa, self).__setattr__(item, "none")


# print("")
# uma_empresa = Empresa("  uma     Empresa  qualquer  ", 12345678910124)
# print(uma_empresa.__dict__)
# print(uma_empresa)


class Gerente(Funcionario):
    def __init__(
        self,
        nome: str,
        sobrenome: str,
        cpf: str,
        salario: int = 8000,
        funcionarios: list = list(),
    ) -> None:
        super().__init__(nome, sobrenome, cpf, salario)
        self.funcionarios = funcionarios

    @staticmethod
    def funcao():
        return "Gerente"

    def __repr__(self):
        return "<%s: %s>" % ("Gerente", self.nome)

    def __str__(self):
        return "<%s: %s>" % ("Gerente", self.nome)


# jose = Gerente("jose", "francisco   pereira", 11122233344)
# print(jose.__dict__)
# print(jose)

# /////////////////////////////////////////////////////////////
# empresa = Empresa("Empresa LTDA", "11223344556677")
# funcionario = Funcionario("Roberto", "Santiago", "11122233344")

# resposta = empresa.contratar_funcionario(funcionario)
