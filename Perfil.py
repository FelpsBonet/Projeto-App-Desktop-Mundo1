#ArquivoPerfisDeAcesso

class Perfil:

    def __init__(self, codigo_sistema, nome_perfil, descricao):
        self.codigo_sistema = codigo_sistema
        self.nome_perfil = nome_perfil
        self.descricao = descricao

    def setCodigoSistema (self, codigo_sistema):
        self.codigo_sistema = codigo_sistema
    
    def getCodigoSistema (self):
        return self.codigo_sistema
    
    def setNomePerfil (self, nome_perfil):
        self.nome_perfil = nome_perfil
    
    def getNomePerfil (self):
        return self.nome_perfil
    
    def setDescricao (self, descricao):
        self.descricao = descricao
    
    def getDescricao (self):
        return self.descricao
    