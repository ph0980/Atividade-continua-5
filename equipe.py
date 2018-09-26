class Equipe():
    def __init__(self):
        self.integrantes = [ ]
    def adicionarIntegrante(self, nome):
        try:
            self.integrantes.append(nome)
            return True
        except:
            return False


