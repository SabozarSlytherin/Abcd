import time 
import Igra
import Logovanje
import os 
from _overlapped import NULL

class Scores():
    def __init__(self, username,highscr, lowscr):
        self.username = username
        self.highscore = highscr
        self.lowscore = lowscr
def changeAttribute(user, attribt, amount):
    allusers = Logovanje.loadAllUsers()
    for x in range(0,len(allusers)):
        if user.username == allusers[x].username:
            if attribt == 'username':
                allusers[x].username = input("\n Unesite novi username : ")
            elif attribt == 'ime':
                allusers[x].ime = input("\n Unesite novo ime  ")
            elif attribt == 'prezime':
                allusers[x].ime = input("\n Unesite novo prezime  ")
            elif attribt == 'password':
                allusers[x].password = input("\n Unesite novu sifru : " )
            elif attribt == 'highscore':
                allusers[x].highscore = amount 
            elif attribt == 'lowscore':
                allusers[x].lowscore = amount 
            elif attribt == 'godine' :
                allusers[x].godine = amount 
    return allusers 
            
                
            
def sortnizAsc(niz):
    i = 0
    for i in range(i , len(niz)-1):
        minimum = i
        j = i+1
        for j in range(j, len(niz)):
            if niz[j].highscore < niz[minimum].highscore : 
                minimum = j
        pom = niz[i]
        niz[i] = niz[minimum]
        niz[minimum] = pom 
    return niz
def sortnizDesc(niz):
    i = 0
    for i in range(i , len(niz)-1):
        minimum = i
        j = i+1
        for j in range(j, len(niz)):
            if niz[j].highscore > niz[minimum].highscore : 
                minimum = j
        pom = niz[i]
        niz[i] = niz[minimum]
        niz[minimum] = pom 
    return niz

def showHighScores():
    
    usrlist = Logovanje.loadAllUsers()
    pom = sortnizDesc(usrlist)
    usrlist = pom
    #[4,5,9,7,3] #[4,5,9,7,3] # [9,7,5,4,3]
      
    print("  RANK \t| USERNAME \t\t| HIGHSCORE")
    for x in range(len(usrlist)):
        Igra.print_ukras(1,1)
        print(" > ",x+1, ". ",usrlist[x].username[:21] , "\t" if len(usrlist[x].username)>13 else"\t\t", usrlist[x].highscore)
def showLowScores():
    
    usrlist = Logovanje.loadAllUsers()
    pom = sortnizAsc(usrlist)
    usrlist = pom
    #[4,5,9,7,3] #[4,5,9,7,3] # [9,7,5,4,3]
      
    print("  RANK \t| USERNAME \t\t| LOWSCORE")
    for x in range(len(usrlist)):
        Igra.print_ukras(1,1)
        print(" > ",x+1, ". ",usrlist[x].username[:21] , "\t" if len(usrlist[x].username)>13 else"\t\t", usrlist[x].lowscore)

def loginMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    Igra.print_ukras(2,2)
    print("\t Dobrodošli u \"Putić pamćenja\" v 1.0 ! ")
    Igra.print_ukras(2,2)
    print("\t > 1. Log-in : \n \t > 2. Register ( new users ) \n\t > 3. HighScores\n\t > 4. LowScores \n\t > 5. Lista igraca \n\t > 6. Kako igrati ? \n\t > 7. exit")
    Igra.print_ukras(1,2)
    akcija = input(" Unesite zeljeni broj akcije : ")
    Igra.print_ukras(1,2)
    print()
    
    if akcija == '7':
        print("\t Dovidjenja, do sledeceg puta ! ^^ ")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif akcija == '1': 
        currentUser = Logovanje.login()
        if currentUser.username == '0' or currentUser.username == NULL:
            loginMenu()
        else :
            gameMenu(currentUser)
    elif akcija == '2': 
        currentUser = Logovanje.registerNewUser()
        gameMenu(currentUser)
    elif akcija == '3': 
        showHighScores()
        nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
        os.system('cls' if os.name == 'nt' else 'clear')
        return loginMenu()
    elif akcija == '4': 
        showLowScores()
        nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
        os.system('cls' if os.name == 'nt' else 'clear')
        return loginMenu()
    elif akcija == '5':
        listaigraca = Logovanje.loadAllUsers()
        for x in range(len(listaigraca)):
            print("\n\t ", x+1,". ", listaigraca[x].username)
        nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
        os.system('cls' if os.name == 'nt' else 'clear')
        return loginMenu()
    elif akcija == '6':
        print(" Putic memorije je igra koja nagradjuje brzo kucanje i pamcenje, svaki korisnik \
        moze da testira svoje vestine u 3 razlicita gamemode-a \n > 1. Trio-putic ( Korisnik 3 puta zaredom resava putic\
        \n > 2. Penta-putic (- || - 5 -||-) \n > 3. Deka-putic (- || - 10 - || - ) \n\n kroz putic se krece \
        koriscenjem tastera 'WASD', koji se koriste kao strelice za kretanje, kada se dodje do E, ili \
        kraja puta , korisnik treba da pritisne space i zatim toga enter kako bi potvrdio svoje resenje \n \
        OBRATITI PAZNJU: I slovo S, koje oznacava pocetak se takodje ponasa kao strelica ili kao 'Korak' \
        pa tako ako pise S -> ; korisnik 2 puta unosi taster d, kako bi se dva puta kretao u levo jer se i S racuna \
        takodje ako stoji 'v' ispod slova S on se tretira kao korak nadole odnosno zahteva unos karaktera za \
        kretanje dole 's'. \n PAZNJA !!: Iskljuciti capslock . \n\n \t Hvala na citanju korisnickog uputstva! \n")
        nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
        os.system('cls' if os.name == 'nt' else 'clear')
        return loginMenu()
    else : 
        print("Do sledeceg vidjenja ! ")
        time.sleep(1)
    
def playMenu(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t Izaberite mode igre :\n  > 1. Trio-Putic \n  > 2. Penta-Putic \n  > 3. Deka-Putic (!Veoma dugo traje!)\n\
  > 4. Highway to !HELL! \n  > 5. Nazad \n")
    akcija = input()
    hscr = int(user.highscore) 
    lscr = int(user.lowscore) 
    if akcija == '1':
        pom = Igra.play(3,0,0)
        if pom > int(user.highscore):
            user.highscore = pom
        if pom < int(user.lowscore):
            user.lowscore = pom
    elif akcija == '2': 
        pom = Igra.play(5,0,0)
        if pom > int(user.highscore):
            user.highscore = pom
        if pom < int(user.lowscore):
            user.lowscore = pom
    elif akcija == '3':
        pom = Igra.play(10,0,0)
        if pom > int(user.highscore):
            user.highscore = pom
        if pom < int(user.lowscore):
            user.lowscore = pom
    elif akcija == '4': 
        pom = Igra.play(66,0,0)
        if pom > int(user.highscore):
            user.highscore = pom
        if pom < int(user.lowscore):
            user.lowscore = pom
    else :
        gameMenu(user)
        
    if hscr != user.highscore or lscr != user.lowscore : 
        changeAttribute(user, 'highscore', hscr )
        changeAttribute(user, 'lowscore', lscr)
    usrlist = Logovanje.loadAllUsers()
    
    for x in range(len(usrlist)):
        if usrlist[x].username == user.username:
            usrlist[x] = user
            
    Logovanje.updateFile(usrlist)
    gameMenu(user)
    
        
def gameMenu(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    Igra.print_ukras(1,2)
    print( "\n\t\t  +++    +++   +   +  +++++ \n \
            \t +      +   +  ++ ++  +    \n \
            \t + +++  +++++  + + +  +++++ \n \
            \t +   +  +   +  +   +  +    \n \
            \t  +++   +   +  +   +  +++++ \n ")
    Igra.print_ukras(1,2)
    print("\t > 1. Play! \n\t > 2. Kako igrati? \n\t > 3. HighScores\n\t > 4. LowScores\n\t < 5. Log-out \n")
    if user.admin == "yes\n" :
        print("\t > 6. ADMIN_TOOLS \n")
    akcija = input(" Unesite zeljeni broj akcije : ")
    
    if akcija == '1': 
        playMenu(user)
    elif akcija == '2': 
         print(" Putic memorije je igra koja nagradjuje brzo kucanje i pamcenje, svaki korisnik \
        moze da testira svoje vestine u 3 razlicita gamemode-a \n > 1. Trio-putic ( Korisnik 3 puta zaredom resava putic\
        \n > 2. Penta-putic (- || - 5 -||-) \n > 3. Deka-putic (- || - 10 - || - ) \n\n kroz putic se krece \
        koriscenjem tastera 'WASD', koji se koriste kao strelice za kretanje, kada se dodje do E, ili \
        kraja puta , korisnik treba da pritisne space i zatim toga enter kako bi potvrdio svoje resenje \n \
        OBRATITI PAZNJU: I slovo S, koje oznacava pocetak se takodje ponasa kao strelica ili kao 'Korak' \
        pa tako ako pise S -> ; korisnik 2 puta unosi taster d, kako bi se dva puta kretao u levo jer se i S racuna \
        takodje ako stoji 'v' ispod slova S on se tretira kao korak nadole odnosno zahteva unos karaktera za \
        kretanje dole 's'. \n PAZNJA !!: Iskljuciti capslock . \n\n \t Hvala na citanju korisnickog uputstva! \n")
         nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
         os.system('cls' if os.name == 'nt' else 'clear')
         gameMenu(user)
    elif akcija == '3': 
        showHighScores()
        nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
        os.system('cls' if os.name == 'nt' else 'clear')
        gameMenu(user)
    elif akcija == '4':
        showLowScores()
        nt = input("\n -> Unesi bilo koji karakter da se vratis nazad :")
        os.system('cls' if os.name == 'nt' else 'clear')
        gameMenu(user)
    elif user.admin == "yes\n" and akcija == '6': 
        print("UNDER CONSTRUCTION ! ")
        time.sleep(3)
        gameMenu(user)
    elif akcija == '5':
            
        print("\t Dovidjenja, do sledeceg puta ! ^^ ")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        loginMenu()
    else : gameMenu(user)
    

loginMenu()
        