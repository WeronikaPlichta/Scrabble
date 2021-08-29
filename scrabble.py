#! /usr/bin/python3

from sys import argv

def scrabble(n, file_name):
    f=open(file_name)
    for line in f:
        word =(line.strip('\n').lower())
        if len(word)>=2:
            available_letters = list(n) 
            true = 0 
            for i in word:
                if i in available_letters:
                    available_letters.remove(i)
                else:
                    true = 1
                    break
            if true == 0:
                print (word)
    



if __name__ == '__main__':
    n = argv[1]
    if len(argv) == 2:
        file_name = ('/usr/share/dict/words')
    else:
        file_name = argv[2] 
    scrabble(n, file_name)
