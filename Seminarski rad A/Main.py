import random


class Matrica_klasa:
    
    
    # Konstruktor 
    def __init__(self, dim) :
        self.dim = dim 
        self.poc_br = poc_br = random.randint(0,dim-1)
        self.kraj_br = [0 for x in range(dim)]
        self.br_koraka_red = [0 for x in range(dim)]
        self.br_koraka = [[0 for x in range(dim)] for y in range(dim)]
        self.znak_reda = [0 for x in range(dim)]
        self.br_kolone_red = [0 for x in range(dim)]
# Funkcija za generisanje Putica
        def genMatricu(self):
            def znakM():
                broj_za_znak = random.randint(0,1)
                return broj_za_znak
            def random_br(x,y):
                random_br = random.randint(x,y)
                return random_br
            
            matrica = [[0 for x in range (self.dim)]for y in range(self.dim)]
            poc_br = self.poc_br
            br_kolone = 0
            
            for x in range (0,self.dim):
                k = random_br(0,self.dim-1)
                znak = znakM()
                self.znak_reda[x] = znak
                self.br_koraka_red[x] = k
                if x == 0:
                    if znak == 0 :
                        if poc_br + k >= self.dim -1:
                            k = self.dim-1 -poc_br
                            br_kolone = self.dim-1
                            
                        else : 
                            br_kolone = poc_br + k
                    else : 
                        if poc_br - k <= 0:
                            k = poc_br
                            br_kolone = 0
                            
                        else : 
                            br_kolone = poc_br - k
                    self.br_kolone_red[x] = br_kolone
                    
                else:
                    if znak == 1 :
                        if br_kolone - k <= 0:
                            k = br_kolone 
                            br_kolone = 0
                            
                        else : 
                            br_kolone = br_kolone -k
                            
                    else :
                        if br_kolone + k >= self.dim -1:
                            k = self.dim-1 - br_kolone
                            br_kolone = self.dim-1
                        else : 
                            br_kolone = br_kolone + k
                    self.br_kolone_red[x] = br_kolone
                            
                self.kraj_br[x] = br_kolone   
                     
                for y in range (0, self.dim): 
                     
                    if znak == 0:
                        if y<= br_kolone and y>= br_kolone - k:
                            matrica[x][y] = 1
                        else: 
                            matrica[x][y] = 0
                    else : 
                        if y >=br_kolone and y<= br_kolone +k :
                            matrica[x][y] = 1
                        else : 
                            matrica[x][y] = 0
                    if znak == 0 :
                        self.br_koraka[x][y] = -matrica[x][y]
                    else :
                        self.br_koraka[x][y] = matrica[x][y]
                    
                   
                           
            return matrica 
    
         # Funkcija za generisanje Resenja putica
        def genResenje(matrica):    
            resenje = matrica
            for x in range(self.dim):
                
                for y in range(self.dim):
                    
                    # Ako je pocetak putica postavi [x][y] "S" - start
                    if x == 0 and y == self.poc_br: 
                        resenje[x][y]  = "s"
                    
                    # Ako je kraj putica postavi [x][y] "E" - end
                    if x == self.dim-1 and y == self.kraj_br[x]: 
                        resenje[x][y]  = "E"
                    
                    # Ako se prebacuje na drugi red i ako nije pocetak i kraj napisi "|"
                    if self.br_kolone_red[x] == y and \
                    resenje[x][y] != "S" and resenje[x][y] != "E":
                        resenje[x][y] = "s"   
                        
                        
                        
                        
                    # Ako se krece na desno napisi "d"
                    elif self.br_koraka[x][y] == -1 and resenje[x][y] != "E":
                        resenje[x][y] = "d"
                        
                        
                    # Ako se krece na levo napisi "a" 
                    elif self.br_koraka[x][y] == 1 and resenje[x][y] != "E":
                        if y == self.kraj_br[x]:
                            resenje[x][y] = "a"
                        else :
                            resenje[x][y] = "a"
                    elif x == self.dim-1 and y == self.kraj_br[x]: 
                        resenje[x][y] = " "
                    elif x == 0 and self.br_koraka[x][y] == 0 and y == self.poc_br:
                        resenje[x][y] = "s"
                    
                    
                        
                    # Ako je 0 ili "S" ili "E" samo prepisi
                    else : 
                        resenje[x][y] = 0
                    
                       
            
            
            return resenje
        
        self.matrica = genMatricu(self)
        self.resenje = genResenje([[0 for x in range(self.dim)]for y in range(self.dim)])   

# Funkcija za "Graficko" prikazivanje generisanog putica
def printMatricu(Matrica_klasa): 
    for x in range(Matrica_klasa.dim):
        
        print("--",end = ' ')
    print()
    for x in range(Matrica_klasa.dim):
        print(x+1, end = '  ')   
    print()
    for x in range(Matrica_klasa.dim):
        
        print("--",end = ' ')
    print("\n")
    for x in range(Matrica_klasa.dim):
        
        for y in range(Matrica_klasa.dim):
            
            # Ako je pocetak putica postavi [x][y] "S" - start
            if x == 0 and y == Matrica_klasa.poc_br: 
                Matrica_klasa.matrica[x][y]  = "S"
            
            # Ako je kraj putica postavi [x][y] "E" - end
            if x == Matrica_klasa.dim-1 and y == Matrica_klasa.kraj_br[x]: 
                Matrica_klasa.matrica[x][y]  = "E"
            
            # Ako se prebacuje na drugi red i ako nije pocetak i kraj napisi "|"
            if Matrica_klasa.br_kolone_red[x] == y and \
            Matrica_klasa.matrica[x][y] != "S" and Matrica_klasa.matrica[x][y] != "E":
                Matrica_klasa.matrica[x][y] = "|"   
                print(Matrica_klasa.matrica[x][y], end= '  ')
                
                
                
            # Ako se krece na desno napisi "->"
            elif Matrica_klasa.br_koraka[x][y] == -1 and \
            (Matrica_klasa.matrica[x][y] != "S" and Matrica_klasa.matrica[x][y] != "E"):
                Matrica_klasa.matrica[x][y] = "->"
                print(Matrica_klasa.matrica[x][y],  end =' ')
                
            # Ako se krece na levo napisi "<-" 
            elif Matrica_klasa.br_koraka[x][y] == 1 and \
            (Matrica_klasa.matrica[x][y] != "S" and Matrica_klasa.matrica[x][y] != "E"):
                if y == Matrica_klasa.kraj_br[x]:
                    Matrica_klasa.matrica[x][y] = "<- "
                else :
                    Matrica_klasa.matrica[x][y] = "<-"
                print(Matrica_klasa.matrica[x][y],  end =' ')
            
            
                
            # Ako je 0 ili "S" ili "E" samo prepisi
            else : 
               
                print(Matrica_klasa.matrica[x][y],  end ='  ')
            
        #Debug za br koraka u redu 
        #print("\t broj koraka u redu je :  ", Matrica_klasa.br_koraka[x][y], end = ' ')
        print()
        if x < Matrica_klasa.dim - 1:
            for z in range(Matrica_klasa.br_kolone_red[x]):
                print('   ', end = '' )
            print("v")
        
    print("\n")      
    for x in range(Matrica_klasa.dim):
        print("--",end = ' ')
    print()
    
    #Vrati pocetnu matricu 
    for x in range(Matrica_klasa.dim):
        for y in range(Matrica_klasa.dim):
            if Matrica_klasa.br_koraka[x][y] != 0:
                Matrica_klasa.matrica[x][y] = 1
def printMatricuresenje(Matrica_klasa):
    for x in range(Matrica_klasa.dim):
        print(Matrica_klasa.resenje[x])
def unesi_dim_matrice():
    print("Unesi Zeljenu dimenziju matrice: ")
    
    k = eval(input())
    mat = Matrica_klasa(k)
    return mat
mleko = unesi_dim_matrice()
printMatricu(mleko)
printMatricuresenje(mleko)



