#setup
import random
user_input = "Open"
turn = 1
money = 0
support = 0
action_history_list = [0]


#event pool
def event(x):
    global money, support
    if x==1:
        print(f"{party_name} received a $5 donation!")
        money += 5

    if x==2:
        print("You can organise a protest!")
        response = str(input("Yes(1) or No(2)? (No by default): "))
        if response == "1":
            change = random.randint(-10, 20)
            support += change
            if change > 0:
                print(f"Protest was succesful! {party_name} gained popularity.")
            if change == 0:
                print("Protest was boring, and nobody really liked it.")
            if change < 0:
                print(f"Protest quickly escalated to riot, dealing major reputation damage to {party_name}")
        
    if x==3:
        print("You can run a promotion campaign for $5!")
        response = str(input("Yes(1) or No(2)? (No by default): "))
        if response == "1":
            money -= 5
            change = random.randint(1,5)
            support += change
            print(f"{party_name} gained {change}% in popularity!")

    if x==4:
        print("You can receive a $10 bribe! (You risk losing followers)")
        response = str(input("Yes(1) or No(2)? (No by default): "))
        if response == "1":
            money += 10
            change = random.randint(-10,0)
            support += change
            if change == 0:
                print("Seems like you got away with it.")
            if change < 0:
                print(f"People have spotted {party_name}'s act of corruption!")


#start settings
print("Welcome to ElectionSim v0! \n Select your difficulty: Easy (1) or Hard (2) (easy by default)")

difficulty = int(input("Difficulty: "))

if difficulty == 2:
    money = 10
    support = 5
    end_turn = 30
else:
    money = 50
    support = 10
    end_turn = 45

print("\nNow name your party.")

party_name = input("Enter name: ")
if not party_name:
    party_name = "Unknown Party"


#game itself
print(f'\nYou got {end_turn} days until the start of elections. Hurry up!\n{party_name} need to gain at least 50% of support in order to win')

while user_input != "Close":
    print('-'*10)
    #victory/loss (NO WAYYYYYYY ITS THE MFING | |! || |_ REFERENCE!!!!!!!) conditions
    if turn == end_turn:
        print("The day has come!")
        if support < 50:
            print(f"Unfortunately, {party_name} haven't got enough votes ({support} out of at least 50).")
            user_input = "Close"
            exit()
        else:
            print(f"Congratulations! {party_name} got {support}% of the votes and won the elections.")
            user_input = "Close"
            exit()
    if money < 0:
        print(f"{party_name} lost budget and got disqualified from elections.")
        if action_history_list[-1] == 3:
            print(f"Most likely, {party_name} spent all of their money trying to get attention")
        user_input = "Close"
        exit()
    if support <= 0:
        print(f"{party_name} lost support and got disqualified from elections.")
        if action_history_list[-1] == 4:
            print(f"This happened after {party_name} got into a huge corruption scandal.")
        if action_history_list[-1] == 2:
            print(f"Recent riot was fatal for the reputation of {party_name}.")
        user_input = "Close"
        exit()

    #turn
    print(f'Day {turn}/{end_turn}, $: {money}, support: {support}%')

    action_history_list.append(random.randint(1,4))
    while action_history_list[-1] == action_history_list[-2]:
        action_history_list[-1] = random.randint(1,4)

    event(action_history_list[-1])
    user_input = input("Next Turn -> ")
    turn += 1