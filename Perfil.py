from Banco_de_dados import PerfisDeAcesso

class Perfil:

    def __init__(self):
        pass

    def setCodigoSistema (self, codigo_sistema):
        self.codigo_sistema = codigo_sistema
    
    def getCodigoSistema (self):
        return self.codigo_sistema
    
    def setNomePerfil (self, nome_perfil):
        self.nome_perfil = nome_perfil
    
    def getNomePerfil (self):
        return self.nome_perfil
    
    def setDescrição (self, descrição):
        self.descrição = descrição
    
    def getDescrição (self):
        return self.descrição
    