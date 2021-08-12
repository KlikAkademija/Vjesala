rjecnik_zivota = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

import random
from rijeci import lista_rijeci
import string

def dohvati_rijec(lista_rijeci):
    rijec = random.choice(lista_rijeci)
    while ('-' in rijec) or (' ' in rijec):
        rijec = random.choice(lista_rijeci)

    return rijec.upper()

def vjesala(lista_rijeci):
    rijec = dohvati_rijec(lista_rijeci)
    slova_rijeci = set(rijec)
    abeceda = set(string.ascii_uppercase)
    iskoristena_slova = set()

    zivoti = 7

    while len(slova_rijeci) > 0 and zivoti > 0:
        print(f'Ostalo ti je {zivoti} života.')
        print('Iskoristio si ova slova: ', ' '.join(iskoristena_slova))

        # p y t - - -
        lista_rijec = [slovo if slovo in iskoristena_slova else '-' for slovo in rijec]
        print(rjecnik_zivota[zivoti])
        print('Trenutna rijec: ', ' '.join(lista_rijec))

        slovo_igraca = input('Pogodi slovo: ').upper()
        if slovo_igraca in abeceda - iskoristena_slova:
            iskoristena_slova.add(slovo_igraca)
            if slovo_igraca in slova_rijeci:
                slova_rijeci.remove(slovo_igraca)
            else:
                zivoti = zivoti - 1
                print('Slovo nije u riječi.')
        elif slovo_igraca in iskoristena_slova:
            print('Već je uneseno ovo slovo. Pokušaj ponovno!')
        else:
            print('Neispravan znak. Pokušaj ponovno!')

    if zivoti == 0:
        print(rjecnik_zivota[zivoti])
        print(f'Izgubio si, žao mi je. Riječ je bila {rijec}.')
    else:
        print(f'Bravo, pogodio si riječ: {rijec}')
        
vjesala(lista_rijeci)

