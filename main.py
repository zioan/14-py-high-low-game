import random
from game_data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""
comparation_list = []
score = 0
answer = ''
game_continue = True
correct_answer = []

first_follower_count = 0
second_follower_count = 0


def second_comparation_item():
    second = random.choice(data)
    comparation_list.append(second)
    comparation_list[1]["order"] = "B"


first = random.choice(data)
comparation_list.append(first)
comparation_list[0]["order"] = "A"


def reasign():
    comparation_list[0] = comparation_list[1]
    comparation_list[0]["order"] = "A"
    comparation_list.pop()
    second_comparation_item()


def display():
    print("\n")
    print(
        f"{comparation_list[0]['name']} - {comparation_list[0]['description']} from {comparation_list[0]['country']}")
    print(vs)
    print(
        f"{comparation_list[1]['name']} - {comparation_list[1]['description']} from {comparation_list[1]['country']}")
    print("\n")


def follower_count():
    global first_follower_count
    global second_follower_count
    first_follower_count = comparation_list[0]["follower_count"]
    second_follower_count = comparation_list[1]["follower_count"]


def check_correct_answer():
    global correct_answer
    if first_follower_count > second_follower_count:
        correct_answer = comparation_list[0]
    else:
        correct_answer = comparation_list[1]


def ask_user():
    global answer
    answer = input("Who is more popular on Instagram? A / B ").capitalize()


# init first game
second_comparation_item()
display()
follower_count()
check_correct_answer()
ask_user()


def next_question():
    print(f"You have {score} points")
    reasign()
    display()
    ask_user()
    follower_count()
    check_correct_answer()


while game_continue:
    if correct_answer['order'] == answer:
        print("Win")
        score += 1
        next_question()

    else:
        print("Fail")
        score = 0
        next_question()
