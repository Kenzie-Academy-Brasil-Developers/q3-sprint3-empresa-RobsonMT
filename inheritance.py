# mock = [
#     {
#         "nome": "Roberto",
#         "sobrenome": "Santiago",
#         "cpf": "123",
#         "salario": 3000,
#         "nome_completo": "Roberto Santiago",
#     },
#     {
#         "nome": "Robson",
#         "sobrenome": "Martins",
#         "cpf": "555",
#         "salario": 2000,
#         "nome_completo": "Robson Martins",
#     },
# ]


class Funcionario(object):

    funcao = "Funcionario"

    def __init__(
        self, nome: str, sobrenome: str, cpf: str, salario: int = 3000
    ) -> None:
        self.nome = nome.strip().capitalize()
        self.sobrenome = " ".join(sobrenome.split()).title()
        self.cpf = cpf
        self.salario = salario
        self.nome_completo: str = f"{self.nome} {self.sobrenome}"

    def __repr__(self):
        return f"<Funcionario: {self.nome_completo}>"

    def __str__(self):
        return f"<Funcionario: {self.nome_completo}>"


class Empresa(object):
    def __init__(self, nome: str, cnpj: str) -> None:
        self.nome = " ".join(nome.strip().split()).title()
        self.cnpj = str(cnpj)
        self.contratados = list()
        
    
    def contratar_funcionario(self, funcionario) -> str:
        if funcionario in self.contratados:
            return "Funcionário com esse CPF já foi contratado."

        nome_completo_contratado = funcionario.nome_completo.replace(' ', '.').lower()
        nome_da_empresa = self.nome.replace(' ', '').lower()

        funcionario.email = f"{nome_completo_contratado}@{nome_da_empresa}.com"

        self.contratados.append(funcionario)

        return "Funcionário contratado!"
        
    @staticmethod
    def adicionar_funcionario_para_gerente(gerente, funcionario):
        if not type(gerente) == Gerente or not type(funcionario) == Funcionario:
            return False

        if funcionario in gerente.funcionarios:
            return 'Funcionario já está na lista de funcionarios desse gerente.'

        gerente.funcionarios.append(funcionario)
        return 'Funcionário adicionado à lista do gerente!'
    
    def demissao(self, funcionario):
        self.contratados.remove(funcionario)

        if type(funcionario) is Gerente:
            return "Gerente demitido!"

        for x in self.contratados:
            if x.funcao == "Gerente":
                if funcionario in x.funcionarios:
                    x.funcionarios.remove(funcionario)

        return "Funcionário demitido!"
        
        
    @staticmethod
    def promocao(empresa, funcionario):
        if funcionario.__class__ != Funcionario or funcionario not in empresa.contratados:
            return False

        empresa.contratados.remove(funcionario)
        
        funcionario_promovido = Gerente(funcionario.nome, funcionario.sobrenome, funcionario.cpf)
        empresa.contratar_funcionario(funcionario_promovido)

        return True

    def __str__(self):
        return f'<Empresa: {self.nome}>'

    def __repr__(self):
        return f'<Empresa: {self.nome}>'


class Gerente(Funcionario):

    funcao = "Gerente"

    def __init__(
        self,
        nome: str,
        sobrenome: str,
        cpf: str,
    ) -> None:
        super().__init__(nome, sobrenome, cpf, 8000)
        self.funcionarios = list()

    def aumento_salarial(self, funcionario, empresa):
        if (
            not funcionario.__class__ is Funcionario
            or not funcionario in self.funcionarios
        ):
            return False
        aumento = int(funcionario.salario + (funcionario.salario / 10))

        if aumento > 8000:
            empresa.promocao(empresa, funcionario)

        else:
            funcionario.salario = aumento

        return True


