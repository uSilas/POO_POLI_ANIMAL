from animal import Animal

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def frente(self, num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'{self.nome} voou pra frente {num_desloc} bloco(s)')
    
    def tras(self, num_desloc):
        self.bloco = self.bloco - num_desloc
        print(f'{self.nome} voou pra trás {num_desloc} bloco(s)')
    
    def view_bloco(self):
        print(f'{self.nome} está no bloco: {self.bloco}')

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def frente(self, num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'{self.nome} correu para frente {num_desloc} bloco(s)')
    
    def tras(self, num_desloc):
        self.bloco = self.bloco - num_desloc
        print(f'{self.nome} correu para trás {num_desloc} bloco(s)')
    
    def view_bloco(self):
        print(f'{self.nome} está no bloco: {self.bloco}')

class Reptil(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def frente(self, num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'{self.nome} rastejou para frente {num_desloc} bloco(s)')
    
    def tras(self, num_desloc):
        self.bloco = self.bloco - num_desloc
        print(f'{self.nome} rastejou para trás {num_desloc} bloco(s)')
    
    def view_bloco(self):
        print(f'{self.nome} está no bloco: {self.bloco}')

class Anfibio(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def frente(self, num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'{self.nome} saltou para frente {num_desloc} bloco(s)')
    
    def tras(self, num_desloc):
        self.bloco = self.bloco - num_desloc
        print(f'{self.nome} saltou para trás {num_desloc} bloco(s)')
    
    def view_bloco(self):
        print(f'{self.nome} está no bloco: {self.bloco}')

class Peixe(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def frente(self, num_desloc):
        self.bloco = self.bloco + num_desloc
        print(f'{self.nome} nadou para frente {num_desloc} bloco(s)')
    
    def tras(self, num_desloc):
        self.bloco = self.bloco - num_desloc
        print(f'{self.nome} nadou para trás {num_desloc} bloco(s)')
    
    def view_bloco(self):
        print(f'{self.nome} está no bloco: {self.bloco}')