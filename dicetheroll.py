import random


def diceroll():
    print("\n<--- Rolling the dice ---->\n")

    num = random.randint(1, 6)

    return num

res = diceroll()
print(res)


while True:
    ask=input("<---- wanna roll again ----> \n")
    if ask.strip() == 'y':
        res = diceroll()
        print("--->:", str(res))
    if ask.strip() == "n":
        break
