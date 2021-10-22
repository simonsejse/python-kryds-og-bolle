import random

from random import randint

succesfuldetræk=[
    [1,2,3],
    [1,5,9],
    [2,5,8],
    [3,6,9],
    [4,5,6],
    [7,8,9],
    [3,5,7],
    [1,4,7],
]

spillepladen = [
   [' ','|',' ','|',' '],
   ['-','+','-','+','-'],
   [' ','|',' ','|',' '],
   ['-','+','-','+','-'],
   [' ','|',' ','|',' '],
]

def hvis_plade():
    print(' ')
    print('================================================================')
    for i in range(len(spillepladen)):
        for j in range(len(spillepladen)):
            print(spillepladen[i][j], end='')
        print('\n')
    print('================================================================')

def returnerHvilkenRækkeOgKolonneDerÆndres(placering):
    #key er en integer og value er en tupple. man skal se det som par, som hedder key-value pairs.
    # der er to parametre placering og træk hvor placeringen er en plads på brættet fra 1 til 9. trækket er så X eller O
    return {
        1 : (0,0),
        2 : (0,2),
        3 : (0,4),
        4 : (2,0),
        5 : (2,2),
        6 : (2,4),
        7 : (4,0),
        8 : (4,2),
        9 : (4,4)
    } [placering]

xPos = []
oPos = []
hvisTur = 'X'

def valgtePlaceringErTom(placering):
    return (placering not in xPos and placering not in oPos)

def placer_træk(placering,træk):
    xPos.append(placering) if træk == 'X' else oPos.append(placering)
    tupel=returnerHvilkenRækkeOgKolonneDerÆndres(placering)
    #dette er manual funktion : spillepladen[2][2]='x'
    spillepladen[tupel[0]][tupel[1]]=træk # her automatiseres valget, hvor der findes indeksene og træk kan indsættes.
    global hvisTur
    hvisTur = 'O' if hvisTur == 'X' else 'X'
    hvis_plade()

    
def computerLavTræk():
    #Ændrer 'X' til det modsatte af spillerens valgte identitet
    randomTal = random.randrange(1, 10)
    placer_træk(randomTal, 'O' if spillerIdentitet == 'X' else 'X') if valgtePlaceringErTom(randomTal) else computerLavTræk()

    
erSpilletSlut = False

hvem_starter = None

spillerIdentitet = ''

sum = lambda x,y: x + y

def tjekVinder():
    global erSpilletSlut
    
    for i in range(len(succesfuldetræk)):
        if all(elem in xPos for elem in succesfuldetræk[i]):
            print('================================================================')
            print('X har vundet!!')
            print('================================================================')
            erSpilletSlut = True
    for i in range(len(succesfuldetræk)):
        if all(elem in oPos for elem in succesfuldetræk[i]):
            print('================================================================')
            print('O har vundet!!')
            print('================================================================')
            erSpilletSlut = True

while hvem_starter is None:
    try:
        hvem_starter = int(input('Vælg 1. hvis du starter, og 2. hvis maskinen skal starte\n'))

        if not(hvem_starter == 1 or hvem_starter == 2):
            raise TypeError('Tallet skal være enten 1 eller 2')
        spillerIdentitet = 'X' if hvem_starter == 1 else 'O'
    except ValueError as e:
        print('Det skulle være et tal!')
    except TypeError as valueError:
        hvem_starter = None
        print(valueError)


while erSpilletSlut == False:
    if sum(len(xPos), len(oPos)) == 9:
        print('Ingen vandt desværre...')
        erSpilletSlut = True
        break

    if hvisTur == spillerIdentitet:
        try:
            placering = int(input('Vælg tal fra 1-9 alt efter, hvor du kunne tænke dig at placere dit svin henne.\n'))
            if placering < 1 or placering > 9:
                raise TypeError('Tallet skal være mellem 1-9')
            if valgtePlaceringErTom(placering):
                 placer_træk(placering, spillerIdentitet)
            else:
                 raise TypeError('Placering er ikke tom!')
        except ValueError:
            print('Det er ikke et tal brormand nr. 1')
            continue
        except TypeError as e:
            print(e)
    else:
        computerLavTræk()
    tjekVinder()
   
