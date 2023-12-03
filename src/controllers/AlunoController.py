from models.AlunoModel import AlunoModel
from datetime import datetime

class AlunoController:
    def __init__(self):
        self.__cpf = ''
        self.__nome = ''
        self.__data_de_nascimento = ''
        self.__email = ''
        self.__endereco = {'cep': '',
                           'logradouro': '',
                           'bairro': '',
                           'localidade': '',
                           'uf': ''}

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        hoje = datetime.today()
        idade = hoje.year - self.__data_de_nascimento.year - ((hoje.month, hoje.day) < (self.__data_de_nascimento.month, self.__data_de_nascimento.day))
        return idade

    def get_email(self):
        return self.__email

    def get_endereco(self):
        return f"{self.__endereco['logradouro']}, {self.__endereco['bairro']}, {self.__endereco['localidade']}-{self.__endereco['uf']}"

    def set_cpf(self, cpf):
        cpf_tratado = ''.join(caractere for caractere in cpf if caractere.isdigit())
        lista_de_cpfs = AlunoModel.get_all_cpf()
        if cpf_tratado in lista_de_cpfs:
            return ['err', 'CPF em uso!']
        if len(cpf_tratado) == 11:
            self.__cpf = cpf_tratado
            return ['msg', 'Ok!']
        else:
            return ['err', 'CPF Invalido!']

    def set_nome(self, nome):
        self.__nome = nome
        return ['msg', 'Nome salvo com sucesso!']

    def set_data_de_nascimento(self, ano, mes, dia):
        try:
            self.__data_de_nascimento = datetime(ano, mes, dia)
            return ['msg', 'Data de nascimento salva com sucesso!']
        except ValueError:
            return ['err', 'Data de nascimento inválida!']

    def load(self, cpf):
        try:
            aluno = self.ac.get_by_cpf(cpf)
            self.__cpf = aluno.get_cpf()
            self.__nome = aluno.get_nome()
            self.__data_de_nascimento = aluno.get_data_de_nascimento()
            self.__email = aluno.get_email()
            self.__endereco = aluno.get_endereco()
            return ['msg', 'Aluno carregado com sucesso!']
        except Exception as e:
            return ['err', f'Erro ao carregar aluno: {str(e)}']

    def set_email(self, email):
        self.__email = email
        return ['msg', 'Email salvo com sucesso!']

    def set_endereco(self, cep, logradouro, bairro, localidade, uf):
        self.__endereco['cep'] = cep
        self.__endereco['logradouro'] = logradouro
        self.__endereco['bairro'] = bairro
        self.__endereco['localidade'] = localidade
        self.__endereco['uf'] = uf
        return ['msg', 'Endereço salvo com sucesso!']
    
    def registrar(self):
        try:
            # Substitua AlunoModel pelo nome correto da classe/modelo do aluno
            AlunoModel.save(self.__cpf, self.__nome, self.__data_de_nascimento, self.__email, self.__endereco)
            return ['msg', 'Aluno registrado com sucesso!']
        except Exception as e:
            return ['err', f'Erro ao registrar aluno: {str(e)}']

    def atualizar(self):
        try:
            # Substitua AlunoModel pelo nome correto da classe/modelo do aluno
            AlunoModel.update(self.__cpf, self.__nome, self.__data_de_nascimento, self.__email, self.__endereco)
            return ['msg', 'Aluno atualizado com sucesso!']
        except Exception as e:
            return ['err', f'Erro ao atualizar aluno: {str(e)}']

    def salvar(self):
        try:
            # Substitua AlunoModel pelo nome correto da classe/modelo do aluno
            AlunoModel.save(self.__cpf, self.__nome, self.__data_de_nascimento, self.__email, self.__endereco)
            return ['msg', 'Aluno salvo com sucesso!']
        except Exception as e:
            return ['err', f'Erro ao salvar aluno: {str(e)}']
