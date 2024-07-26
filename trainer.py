import random

def choose_menu():
    print("""
Topic 1: Times tables up to 12x12
Topic 2: Multiplying by 11
Topic 3a: Squaring nums ending in 5
Topic 3b: Multiplying nums with same first digit whose last digits add up to 10
Topic 4: Multiplying nums between 10 and 20
Topic 5: Squaring 2 digit nums""")
    topic_chosen = int(input("> "))
    if topic_chosen == 1:
        topic_1()
    elif topic_chosen == 2:
        topic_2()
    return topic_chosen

def topic_1():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    print(f"\n{a} X {b} = ")
    guess = input("> ")
    if guess.lower() in ["exit", "back"]:
        choose_menu()
    while int(guess) != a*b:
        print("try again!\n")
        guess = input("> ")
    print("correct!")
    topic_1()

def topic_2():
    first = random.randint(0, 1)
    a = random.randint(10, 9999)
    if first == 0:
        print(f"\n{a} X 11 = ")
    else:
        print(f"\n11 X {a} = ")
    guess = input("> ")
    if guess.lower() in ["exit", "back"]:
        choose_menu()
    while int(guess) != a*11:
        print("try again!\n")
        guess = input("> ")
    print("correct!")
    topic_2()

topic = choose_menu()