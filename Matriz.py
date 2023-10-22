#ArquivoMatrizSoD

class Matriz:

    def __init__(self, sistema_1, perfil_1, sistema_2, perfil_2):
        self.sistema_1 = sistema_1
        self.perfil_1 = perfil_1
        self.sistema_2 = sistema_2
        self.perfil_2 = perfil_2

    def setSistema1 (self, sistema_1):
        self.sistema1 = sistema_1
    
    def getSistema1 (self):
        return self.sistema_1

    def setPerfil1 (self, perfil_1):
        self.perfil1 = perfil_1

    def getPerfil1 (self):
        return self.perfil_1
    
    def setSistema2 (self, sistema_2):
        self.sistema1 = sistema_2
    
    def getSistema2 (self):
        return self.sistema_2

    def setPerfil2 (self, perfil_2):
        self.perfil2 = perfil_2

    def getPerfil2 (self):
        return self.perfil_2
   