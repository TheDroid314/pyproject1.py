from random import shuffle

card_ls =[]
for line in open('cards.txt'):
    card_ls.append(line)

cl =[]
di=[]
he =[]
sp =[]
x =[]
for item in card_ls:
    y = item[:-1]
    x = y.split('mi')
    cl.append(x[0])
    di.append(x[1])
    he.append(x[2])
    sp.append(x[3])
    

a =0
clo =[]
wor =[]
while True:
    if a == 0:
        pass
    elif a % 9 == 0:
        clo.append(wor)
        wor = []
    if a == 117:
        break
    wor.append(cl[a])
    a += 1


a =0
dia =[]
wor =[]
while True:
    if a == 0:
        pass
    elif a % 9 == 0:
        dia.append(wor)
        wor = []
    if a == 117:
        break
    wor.append(di[a])
    a += 1
a =0
hea =[]
wor =[]
while True:
    if a == 0:
        pass
    elif a % 9 == 0:
        hea.append(wor)
        wor = []
    if a == 117:
        break
    wor.append(he[a])
    a += 1
a =0
spa =[]
wor =[]
while True:
    if a == 0:
        pass
    elif a % 9 == 0:
        spa.append(wor)
        wor = []
    if a == 117:
        break
    wor.append(sp[a])
    a += 1


clo.reverse()
dia.reverse()
hea.reverse()
spa.reverse()
cards = hea + dia + spa+ clo
c = [' _________ ','|         |','|         |','|         |','|         |','|         |','|         |','|         |',' ~~~~~~~~~ ']

cards.insert(0,c)
def deck_lookup(x):
    if x <14:
        suits = 'Hearts'
    elif x <27:
        suits = 'Dimands'
    elif x <40:
        suits = 'Spades'
    else:
        suits = 'Clovers'

    while x > 13:
        x = x -13
    if x == 1:
        car = 'Ace'
    elif x == 11:
        car = 'Jack'
    elif x == 12:
        car = 'Queen'
    elif x == 13:
        car = 'King'
    else:
        car =  str(x)
    cardletter = car + ' of ' + suits
    return cardletter


def value(x):
    while True:
        if x <14:
            if x >10:
                x = 10
            return x
        else:
            x = x -13

def valuel(x):
    val = 0
    for item in x:
        z = value(item)
        val = val + z
    return val

def printf(a):
    b = len(a)
    c =[]
    y = 0 
    o = 0
    for item in a:
        c.append(cards[item])
    for item in c[0]:
        m = ' '
        for car in c:
            l = str(car[y])
            m = m + l
        print(m)
        y += 1




master_deck =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]

def draw_two(x):
    y =[]
    y.append(x.pop())
    y.append(x.pop())
    return y

bank = 100
bet =10
working_deck = []




while True:
    if len(working_deck) < 10:
        for item in master_deck:
            working_deck.append(item)
        shuffle(working_deck)
    while True:
        a = input('bet ~')
        b = int(a)
        if b < bank:
            bet = b
            break
        elif b == 'end':
            break
        else:
            print('not enough in the bank')
    player_hand = draw_two(working_deck)
    dealer_hand = draw_two(working_deck)
    jk = [dealer_hand[0], 0]
    printf(jk)
    print('\n\n\n\n\n')
    printf(player_hand)
    while True:
        a = input('hit/stay ~')
        b = str(a)
        if b == 'hit':
            player_hand.append(working_deck.pop())
            printf(jk)
            print('\n\n\n\n\n')
            printf(player_hand)
        elif b == 'stay':
            break
    while True:
        if valuel(dealer_hand) < 17:
            dealer_hand.append(working_deck.pop())
        else:
            break
    printf(dealer_hand)
    print(valuel(dealer_hand))
    print('\n\n\n\n\n')
    printf(player_hand)
    print(valuel(player_hand))
    if valuel(player_hand) > 21:
        print('bust')
        bank = bank - bet
        print(f'you have {bank} in bank')
    elif valuel(dealer_hand) > 21:
        print('dealer bust')
        bank = bank + bet
        print(f'you have {bank} in bank')
    elif valuel(dealer_hand) > valuel(player_hand):
        print('dealer Wins')
        bank = bank - bet
        print(f'you have {bank} in bank')
    elif valuel(dealer_hand) < valuel(player_hand):
        print('you Win')
        bank = bank + bet
        print(f'you have {bank} in bank')
    else:
        print('draw')
        print(f'you have {bank} in bank')
        


