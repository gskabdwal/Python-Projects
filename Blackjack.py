import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
start = input("\nDo you want to play game of Blackjack? Type 'y' or 'n': ")

while start == "y":

    def assign():
        return random.randint(2, 11)
    list1 = [assign(), assign()]
    add1 = 0
    for x in list1:
        add1 += x
    list2 = [assign(), assign()]
    card1 = list2[0]
    add2 = list2[0]+list2[1]
    print(f"Your cards {list1}, current score: {add1}")
    print(f"Computer's first card: {card1}")

    sum2 = 0
    for a in list1:
        sum2 += a
    sum3 = 0
    for b in list2:
        sum3 += b

    while sum3 < 17:
        a = assign()
        if a == 11 and (sum3+a) > 21:
            list2.append(1)
            sum3 += 1
        elif a == 11 and (sum3+a) < 21:
            list2.append(11)
            sum3 += 11
        else:
            list2.append(a)
            sum3 += a
    rep = 4
    if sum2 > 21:
        rep = 3
    elif sum3 > 21:
        rep = 1

    cont = "x"

    def repeat():

        if (cont == "y") or rep == 4:

            def assign():
                return random.randint(2, 11)

            v = assign()
            if cont == "y":
                list1.append(v)

            sum2 = 0
            for a in list1:
                sum2 += a

    if rep == 4:
        cont = input("\nEnter 'y' for new card, enter 'n' to pass: ")
        repeat()

    def check():
        if (cont == "y") or rep == 4:
            sum3 = 0
            for b in list2:
                sum3 += b

            if sum2 > 21:
                return 3
            elif sum3 > 21:
                return 1

            elif sum2 > sum3:
                return 1
            elif sum2 == sum3:
                return 2
            else:
                return 3

        elif cont == "n":
            if sum2 > 21:
                return 3
            elif sum3 > 21:
                return 1
            elif sum2 > sum3:
                return 1
            elif sum2 == sum3:
                return 2
            else:
                return 3

        else:
            return 4

    check()
    sum2 = 0
    for d in list1:
        sum2 += d

    print(f"Your cards {list1}, current score: {sum2}")
    print(f"Computer's first card: {card1}")
    print(f"Your final cards {list1}, final score: {sum2}")
    print(f"Computer's final cards {list2}, final score: {sum3}")
    if (rep == 1) or (check() == 1):
        print("You Win!")
    elif (rep == 2) or (check() == 2):
        print("Its a Draw!")
    elif (rep == 3) or (check() == 3):
        print("You Lose!")
    start = input("\nDo you want to play game of Blackjack? Type 'y' or 'n': ")
