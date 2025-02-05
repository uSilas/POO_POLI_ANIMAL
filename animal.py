class Animal():
    def __init__(self,nome):
        self.bloco = 0
        self.nome = nome
        
    def frente(self,num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'Você se movimentou pra frente {num_desloc} bloco(s)')
    def tras(self,num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'Você se movimentou pra trás {num_desloc} um bloco')
    def view_bloco(self):
        print(f'voce está no bloco: ', self.bloco)

        
            