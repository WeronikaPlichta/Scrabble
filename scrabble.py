#! /usr/bin/python3

#Weronika Plichta

from sys import argv

def scrabble(n, nazwa_pliku):
    f=open(nazwa_pliku)
    for linia in f:
        slowo =(linia.strip('\n').lower())
        if len(slowo)>=2:
            dostepne_litery = list(n) #zamieniam litery na listę, żeby móc je potem z niej pojedyńczo pobierać
            prawda = 0 #dodaję znaczniki prawda/fałsz, aby okreslić, czy dane słowo ma zostać wyprintowane przez funkcję
            for i in slowo:
                if i in dostepne_litery:
                    dostepne_litery.remove(i) #jeżeli z liter, które mamy da sie ulozyc dane slowo,usuwamy je [słowo] z dostepnej puli
                else:
                    prawda = 1
                    break
            if prawda == 0:
                print (slowo)
    



if __name__ == '__main__':
    n = argv[1]
    if len(argv) == 2:
        nazwa_pliku = ('/usr/share/dict/words') #ustawiam plik, jako domyślny
    else:
        nazwa_pliku = argv[2] #Część kodu wyświetlająca plik domyślny w przypadku braku wprowadzenia nazwy przez użytkownika działa poprawnie
    scrabble(n, nazwa_pliku)
