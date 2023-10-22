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
            codigo = row['Código do sistema']
            nome = row['Nome do sistema']
            sistema = Sistema(codigo, nome)
            sistemas.append(sistema)
        return sistemas
#criar def para controlador das demais tabelas.
if __name__ == "__main__":
    sistemas = Controlador.controlador_sistemas(ArquivoSistemas)
    for sistema in sistemas:
        print(sistema.getCodigoSistema(), sistema.getNomeSistema())

   