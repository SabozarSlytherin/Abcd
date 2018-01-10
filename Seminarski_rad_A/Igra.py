import random
import time
import os 

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
            
        # Dodavanje strelice na dole kad se prelazi u drugi red da ne bude samo " | "
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
        
def print_ukras(n, style): # Ukrasi
    for x in range(0,n):
        if style == 1:
            print("-- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- --")
        elif style == 2:
            print("== === == === == === == === == === == === == === == === == === == === == === == === ==")
        elif style == 3:
            print("~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~ ~~~ ~~")
        else : 
            print("__ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __ ___ __")            
def unesi_dim_matrice(): # Prompt za unos velicine matrice + ukrasi 
    tip = random.randint(1,4)
    if tip == 1:
        
        print_ukras(1,2)
        print("Tip : Sto je veca dimenzija matrice to vise vremena imate da upamtite resenje!")
        print_ukras(1,2)
        print()
    elif tip == 2:
        print_ukras(1,2)
        print("Tip : Sto je veca dimenzija matrice to veci skor mozete da ostvarite!" )
        print_ukras(1,2)
    else : 
        print_ukras(1,2)
        print("Tip : Dok vezbate bolje uzimajte manje dimenzije matrice!")
        print_ukras(1,2)
    print()
    print_ukras(2,1)
    print(" ==> Unesi Zeljenu dimenziju matrice: od 3 - 10  ")
    print_ukras(2,1)
    dobarunos = True
    k = input()
    while dobarunos : 
        if k == "3" or k== "4" or k== "5" or k== "6" or k== "7" or k== "8" or k== "9" or k=="10":
            dobarunos = False 
        else :
            print("Unesen broj nije u rasponu od [3,10]")
            k = input()
            dobarunos = True 
    k = int(k)
    return k
#time.sleep(5)

def listaResenja(Matrica_klasa): # Pretvara se matrica resenja u listu 
    lista = []
    pom = []
    pom_br = 0
    
    for x in range(Matrica_klasa.dim):
        for y in range(Matrica_klasa.dim):
            # Ako je tip resenja Takav da ide na -> Dodaj resenja redom
            if Matrica_klasa.br_koraka[x][y] == -1: 
                lista.append(Matrica_klasa.resenje[x][y])
            # Ako nije obrni
            elif Matrica_klasa.br_koraka[x][y] == 1: 
                pom.append(Matrica_klasa.resenje[x][y])   
                pom_br += 1
        # Dodavanje obrnutog resenja u listu 
        if pom_br != 0 : 
            pom2= pom[::-1]
            for z in range(pom_br):
                
                lista.append(pom2[z])
                
        pom_br = 0
        
    return lista

def play (br_puta, score, bonus):
    
    dim = unesi_dim_matrice()
    mat = Matrica_klasa(dim)
    bonus += 1
    print(" Vas putic se prikazuje za : ")
    for x in range(0,3):
        
        print(" > ",3-x , "s")
        time.sleep(1)
    
    printMatricu(mat)
    print(" Imate ", dim, "s da zapamtite putic : ")
    
    for x in range(0,dim-3 if dim >6 else dim-1):
        
        print(" > ",dim-3-x if dim > 6 else dim-1-x , "s")
        time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    korisnik_resenje = input('Unesi resenje tako sto ces zavrsiti sa "space" ')
    print("\n")
    kor_res_lista = list(korisnik_resenje)
    
    duzina_putica = listaResenja(mat).__len__()
    if kor_res_lista == listaResenja(mat):
        print("Uspesno ste resili Putic!")
        print("\n")
        score = score + ((100+duzina_putica)* bonus )* (dim * bonus if dim>4 else dim-2 * dim -2 if dim>=5 else 1)
    else :
        print ( " Nazalost niste uspeli resiti putic :( .")
        print("\n")
        score = score - 200*bonus *dim*bonus
    print("Duzina putica je : " , duzina_putica)
    if br_puta > 1 :
        print_ukras(1,3)
        print (" VAS SCORE JE : ", score," Bonus za skor u prethodnoj rundi je : X", bonus)
        print_ukras(1,3)
        return play(br_puta-1, score,bonus)
        
    else : 
        print_ukras(1,3)
        print (" VAS SCORE JE : ", score," Bonus za skor u prethodnoj rundi je : X", bonus  )
        print_ukras(1,3)
        nt = input("\n -> Unesi bilo koji karakter da se vratis na pocetni meni :")
        os.system('cls' if os.name == 'nt' else 'clear')
        return score
        
    
    

    

    
    



















