import time
import Igra


class User():
    def __init__(self, username, password, ime, prezime, godine,highscore,lowscore,admin):
        self.username = username 
        self.password = password 
        self.ime = ime 
        self.prezime = prezime 
        self.godine = godine
        self.highscore = highscore
        self.admin = admin
        self.lowscore = lowscore

def login():

    logged_user = User('0','0','0','0','0','0','0','0')
    usr = input("Username : ")
    passwrd = input("Password : ")
    for line in open("users.txt", "r").readlines():
        if len(line)> 1:
            username, password, ime, prezime, godine, highscore,lowscore, admin = line.split('?')
            
            if usr == username and passwrd == password:
                logged_user = User(username, password, ime, prezime, godine,highscore,lowscore, admin)
                print("Uspesno ste se ulogovali !")
                time.sleep(0.5)
                return logged_user
    if logged_user.ime == '0' :
        c = input("Pogresno ste uneli podatke: \n > 1. Pokusaj ponovo \n > 2. Vrati se nazad \n > 3. Napravi novi nalog")
        if c == '1':return login()
        elif c == '3':
           return  registerNewUser()
        else : 
            return logged_user


    
def updateFile(users):
    file = open("users.txt", "w")
    allusers = users
    for x in range(len(allusers)): 
        file.write(splitToString(allusers[x]))
        
    file.close()

def splitToString(user):
    
    fulluser = '?'.join([user.username, user.password, user.ime, user.prezime,str(user.godine),\
                          str(user.highscore),str(user.lowscore), user.admin])
    return fulluser
def loadAllUsers():
    logged_users = []
    for line in open("users.txt", "r").readlines():
        if len(line)> 1: 
            username, password, ime, prezime, godine, highscore,lowscore, admin = \
            line.split('?')
            
            pomocniUser = User(username, password, ime, prezime, godine,highscore, lowscore, admin)
        logged_users.append(pomocniUser)
    return logged_users

def registerNewUser():
    ime = input(" > Unesite vase ime : ")
    prezime = input(" > Unesite vase prezime : ")
    username = input(" > Unesite vas username : ")
    password = input(" > Unesite vasu sifru : ")
    godine = eval(input(" > Unesite vase godine : "))
    
    if username == '0':
        while username == '0':
            Igra.print_ukras(2,1)
            username = input(" > Uneli ste 0 kao username pokusajte ponovo!\
            \n >Unesite vas username: ")
            Igra.print_ukras(2,1)
    if username != '0' : 
        for line in open("users.txt" , "r"):
            username2 = line.split('?')
            
            while username == username2 or username == '0': 
                if username == '0' : 
                    username = input(" > Uneli ste 0 username pokusajte ponovo!\
                    \n >Unesite vas username: ")
                else : 
                    username = input(" >To korisnicko ime je vec zauzeto pokusajte ponovo! \
                    \n > Unesite vas username: ")
                       
        
    while len(password) < 5: 
        password = input("Vasa sifra mora imati bar 5 karaktera !\
        \n > Unesite vasu sifru :  ")
    
    while godine <= 0 :
        godine = eval(input(" Ne mozete uneti negativne godine ili 0 , pokusajte ponovo!\
         \n > Unesite vase godine : "))
    
    reg_user = User(username,password, ime, prezime, godine, 0 , 0, 'no')
    Igra.print_ukras(1,3)
    print("Uspesno ste se registrovali! " )
    Igra.print_ukras(1,3)
    fulluser = splitToString(reg_user)
    
    file = open('users.txt', 'a+')
    file.write("\n")
    file.write(fulluser)
    
    file.close()
    
    time.sleep(2)
    return reg_user


    
    
    

    