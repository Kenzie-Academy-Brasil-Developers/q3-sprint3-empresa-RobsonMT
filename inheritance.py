class Funcionario(object):

    funcao = "Funcionario"

    def __init__(self, nome:str, sobrenome:str, cpf:str, salario:int = 3000)-> None:
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
    def __init__(self, nome:str, cnpj:str)-> None:
        self.nome = " ".join(nome.strip().split()).title()
        self.cnpj = str(cnpj)
        self.contratados:list = []
        
    
    def contratar_funcionario(self, funcionario:"Funcionario" or "Gerente")-> str:
        if funcionario in self.contratados:
            return "Funcionário com esse CPF já foi contratado."

        nome_completo_contratado = funcionario.nome_completo.replace(' ', '.').lower()
        nome_da_empresa = self.nome.replace(' ', '').lower()

        funcionario.email = f"{nome_completo_contratado}@{nome_da_empresa}.com"

        self.contratados.append(funcionario)

        return "Funcionário contratado!"
        
    @staticmethod
    def adicionar_funcionario_para_gerente(gerente:"Gerente", funcionario:"Funcionario")-> bool or str:
        if not gerente.__class__ == Gerente or not funcionario.__class__ == Funcionario:
            return False

        if funcionario in gerente.funcionarios:
            return 'Funcionario já está na lista de funcionarios desse gerente.'

        gerente.funcionarios.append(funcionario)
        return 'Funcionário adicionado à lista do gerente!'
    
    def demissao(self, funcionario:"Funcionario" or "Gerente")-> str:
        self.contratados.remove(funcionario)

        if funcionario.__class__ is Gerente:
            return "Gerente demitido!"

        for contratado in self.contratados:
            if contratado.funcao == "Gerente":
                if funcionario in contratado.funcionarios:
                    contratado.funcionarios.remove(funcionario)

        return "Funcionário demitido!"
        
        
    @staticmethod
    def promocao(empresa:"Empresa", funcionario:"Funcionario")-> bool:
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

    def __getattribute__(self, item):
        return super(Empresa, self).__getattribute__(item)

    def __getattr__(self, item):
        return super(Empresa, self).__setattr__(item, "este atributo não existe na classe")


class Gerente(Funcionario):

    funcao = "Gerente"

    def __init__(self, nome:str, sobrenome:str, cpf:str)->None:
        super().__init__(nome, sobrenome, cpf, 8000)
        self.funcionarios: list = []

    def aumento_salarial(self, funcionario: "Funcionario", empresa : "Empresa")-> bool:
        if ( not funcionario.__class__ == Funcionario or not funcionario in self.funcionarios):
            return False

        aumento = int(funcionario.salario + (funcionario.salario * 0.10))

        if aumento > 8000:
            empresa.promocao(empresa, funcionario)

        else: 
            funcionario.salario = aumento

        return True
    
    def __repr__(self):
        return f"<Gerente: {self.nome_completo}>"

    def __str__(self):
        return f"<Gerente: {self.nome_completo}>"


