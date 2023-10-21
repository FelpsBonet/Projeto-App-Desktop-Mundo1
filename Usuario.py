from banco_de_dados import Usuarios

class Usuario:

    def setCPF (self, cpf):
        self.cpf = cpf
    
    def getCPF (self):
        return self.cpf
    
    def setCodigoSistema (self, codigo_sistema):
        self.codigo_sistema = codigo_sistema
    
    def getCodigoSistema (self):
        return self.codigo_sistema
    
    def setNomePerfil (self, nome_perfil):
        self.nome_perfil = nome_perfil
    
    def getNomePerfil (self):
        return self.nome_perfil