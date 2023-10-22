#CLASSE DE ITERAÇÃO SOBRE OS DATAFRAMES, UMA FUNÇÃO PARA CADA.
#RETORNA EM LISTAS OS DADOS DE CADA CLASSE E ARQUIVO.

from Banco_de_dados import *
from Matriz import *
from Perfil import *
from Sistema import *
from Usuario import *

class Controlador:

    def controlador_sistemas (self):
        sistemas_df = ArquivoSistemas
        sistemas = []
        for _, row in sistemas_df.iterrows():
            codigo = row ['Código do sistema']
            nome = row ['Nome do sistema']
            sistema = Sistema (codigo, nome)
            sistemas.append (sistema)
        return sistemas
    
    def controlador_matriz (self):
        matriz_df = ArquivoMatrizSoD
        matrizes = []
        for _, row in matriz_df.iterrows():
            sistema1 = row ['Sistema 1']
            perfil1 = row ['Perfil 1']
            sistema2 = row ['Sistema 2']
            perfil2 = row ['Perfil 2']
            matriz = Matriz (sistema1, perfil1, sistema2, perfil2)
            matrizes.append (matriz)
        return matrizes
    
    def controlador_perfil (self):
        perfil_df = ArquivoPerfisDeAcesso
        perfis = []
        for _, row in perfil_df.iterrows():
            codigo = row ['Código do sistema']
            nome = row ['Nome do perfil']
            descricao = row ['Descrição']
            perfil = Perfil (codigo, nome, descricao)
            perfis.append (perfil)
        return perfis
    
    def controlador_usuario (self):
        usuario_df = ArquivoUsuarios
        usuarios = []
        for _, row in usuario_df.iterrows():
            cpf = row ['CPF']
            codigo = row ['Código do sistema']
            nome = row ['Nome do perfil']
            usuario = Usuario (cpf, codigo, nome)
            usuarios.append (usuario)
        return usuarios

#LOGO ABAIXO TEMOS TESTES PARA IMPRESSÃO DOS DADOS DOS ARQUIVOS USANDO AS FUNÇÕES DO CONTROLADOR.
#PARA TESTAR RETIRE AS "#" DAS LINHAS "if" ÁTE "print".

#TESTE PRINT PELO ÍNDICE:
#if __name__ == "__main__":
#    matriz = Controlador.controlador_matriz (ArquivoMatrizSoD)
#    print (matriz[0])

#TESTE PRINT PARA SISTEMAS:
#if __name__ == "__main__":
#    sistemas = Controlador.controlador_sistemas (ArquivoSistemas)
#    for sistema in sistemas:
#        print (sistema.getCodigoSistema(), sistema.getNomeSistema())

#TESTE PRINT PARA MATRIZ SOD:
#if __name__ == "__main__":
#    matrizsod = Controlador.controlador_matriz (ArquivoMatrizSoD)
#    for matriz in matrizsod:
#        print (matriz.getSistema1(), matriz.getPerfil1(), matriz.getSistema2(), matriz.getPerfil2())

#TESTE PRINT PARA PERFIS DE ACESSO:
#if __name__ == "__main__":
#    perfis = Controlador.controlador_perfil (ArquivoPerfisDeAcesso)
#    for perfil in perfis:
#        print (perfil.getCodigoSistema(), perfil.getNomePerfil(), perfil.getDescricao())

#TESTE PRINT PARA USUÁRIOS:
#if __name__ == "__main__":
#    usuarios = Controlador.controlador_usuario (ArquivoUsuarios)
#    for usuario in usuarios:
#        print (usuario.getCPF(), usuario.getCodigoSistema(), usuario.getNomePerfil())
