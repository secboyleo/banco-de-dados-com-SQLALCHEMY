import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


#versao do sql alchemy utilizada
versao = sqlalchemy.__version__
print(versao)

usuario = 'root'
senha = ''
host = 'localhost'
porta = '3306'
nome_do_banco = 'familia'

#fazendo uma url para criar a conexão no engine
url = f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{nome_do_banco}'


#conectando ao banco de dados
engine = sqlalchemy.create_engine(url, echo=True) #o echo permite ver o codigo em SQL so executar o programa

base = declarative_base()
#fazendo o mapeamento do banco de dados
class User(base):
    #cria o nome da tabela
    __tablename__ = 'usuarios' #informacao obrogatoria
    
    #criacao da chave primaria e mais atrivutos
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))
    idade = Column(Integer) #nao devia colocar idade por ano que a pessoa tem, mas sim por data
    
    #funcao para mostrar o que esta no endereco de memoria na hora do print
    #importante passar os prametros corretos na hora do retuern
    def __repr__(self):
        return f"<User(nome={self.nome}, email={self.email}, idade={self.idade})>"
    

#(CREATE TABLE)criando a tabela no banco de dados (CUIDADO!!!! RODAR ISSO APENAS UMA VEZ PARA N CRIAR DUAS TABELAS IGUAIS)
base.metadata.create_all(engine) 

#criando instancias da classe
user = User(nome='Leoncio02', email='leonciomata@gmail.com', idade=50)

#criando uma sessão 
Sessao = sessionmaker(bind=engine)
sessao = Sessao()

#------------------------------------------------ADICIONADO OBJETOS (INSERT)----------------------------------------------------------------------------------
#adicionando uma instancia por vez
# sessao.add(user)
# sessao.commit() #se der apenas um add o comando não vai ser executado, é necessário dar um commit para realizar a inserção da instancia

#adicionando mais de uma instancia por vez
#sessao.add_all([
#   User(nome='Brunoro', email='brunoro@innon.br', idade=25),
#    User(nome='Joao gomes', email='gomes255@gmail.ciom', idade=23),
#    User(nome='Pedro', email='pedrope@gmail.com', idade=30)
#])

#sessao.commit()

#---------------------------------------------------CONSULTANDO OBJETOS (SELECT)--------------------------------------------------------------------------

#pegando um user por vez
# query_user = sessao.query(User).filter_by(nome='Joao gomes').first() #O .FIRST() PEGA A PRIMEIRA OCORRENCIA QUE APARECER
# print(query_user)

#pegando todos os user (instancia == linha da tabela)
# for instancia in sessao.query(User).order_by(User.id):
#     print(f'user {instancia.id}= {instancia.nome}')

#----------------------------------------------------MODIFICAR INSTANCIAS (UPDATE)------------------------------------------------------------------------
#carrega a instancia que quero alterar
# user = sessao.query(User).filter_by(email='leonciomata@gmail.com').first()

# #altera somente se o user existir (retorna true)
# if user:
#     user.nome = 'leonindas'
#     user.email = 'leonidas@gmail.com'
#     sessao.commit() #sempre dar um comit para salvar

#-------------------------------------------------DELETAR UMA INSTANCIA OU ALGO EM ESPECIFICO (DELETE)-------------------------------------------------------
# user = sessao.query(User).filter_by(nome='Brunoro').first()
# sessao.delete(user)
# sessao.commit()

#verificando se realmente foi apagado
# user = sessao.query(User).filter_by(nome='Brunoro').count()
# print(user)