import random, json

with open("words.json", "r") as json_file:
    word_list = json.load(json_file)

with open("hangmanPics.json", "r") as json_file:
    animations = json.load(json_file)

while True:
    userStatus = input(' Enter "e" to exit or "p" to play\n->>')
    if userStatus == "e":
        break
    elif userStatus == "p":
        random_word = random.choice(word_list)
        blank_list = []
        for ch in random_word:
            blank_list.append("_")
        print(blank_list)
        lives = 7
        win = 0
        while lives:
            user_input = (input("Enter character: ")).lower()
            index = 0
            if user_input in blank_list:
                print(f"You have already entered {user_input}")
                continue
            for char in random_word:
                if user_input == char:
                    blank_list[index] = user_input
                    win += 1
                index += 1
            if user_input in random_word:
                print(f"Your guess {user_input} is in the word , completed words {win}")
            else:
                print(animations[7 - lives])
                lives -= 1
                print(
                    f"Your guess {user_input} is not in the word, you loose one life. Remaining: {lives}"
                )
            print(blank_list)
            if win == len(random_word):
                break

        final_user_answer = ""
        for i in blank_list:
            final_user_answer += i
        if final_user_answer == random_word:
            print("Congratulations!! You won")
        else:
            print(f"You lost!! Never give up... The word was {random_word}")
        print("\n\n\n ------------------New Game----------------- ")
