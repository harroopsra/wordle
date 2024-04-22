import random

WORD_SIZE = 5

words = []
with open('./wordle/sgb-words.txt', 'r') as this_file:
    for line in this_file:
        words.append(line.rstrip())

target_word = random.choice(words)

target = list(target_word)

print("---WELCOME TO WORDLE---")
print("Each word will have")
print("0.5 - Right Letter, Wrong position")
print("1 - Right letter, Right position")

turn_count = 0
over = True

while over:
    print("")

    guess = input(f"Enter a {WORD_SIZE} letter word: ")
    print("")

    if guess == "!cheat":
        print(target)
        continue

    if len(guess) != WORD_SIZE:
        print("Not a valid word (Wrong size)")
        continue

    if guess not in words:
        print("Not a valid english word")
        continue

    correct = [0 for _ in range(WORD_SIZE)]
    for i in range(len(guess)):
        if guess[i] == target[i]:
            correct[i] = 1
        elif guess[i] in target:
            correct[i] = 0.5
    
    turn_count += 1

    print(f"Turn Number: {turn_count}")
    print(f"Your guess was           : {list(guess)}")
    print(f"This is how close you are: {correct}")
    
    # Exit condition
    if list(guess) == target:
        over = False
        print(f"You won! The correct word is indeed {target_word}. It only took you {turn_count} tries")

    elif turn_count == WORD_SIZE+1:
        print("You ran out of turns. Whomp whomp")
        over = False