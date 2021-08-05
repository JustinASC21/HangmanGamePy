  

## Hangman Game

import random

random_words = []

w = open("Top1000Words.txt","r")
# will only readlines one time when the program starts
words = w.readlines()
# first item is an unexpected word, so we can omit this
words = words[1:-1]

for word in words:
    # we strip the words so the "\n" is omited from the words
    split_word = word.strip()
    random_words.append(split_word)
    # we add this to our random_words list
    
# now we can guess from these 1000 words
hang_word = (random.choice(random_words)).lower()
# make random word into an array, [_,_,_,_] to [_,t,_,_]

word_ar = ['_' for char in hang_word]


def make_array(word,letter = ' '):

    global word_ar

    # logic checks if letter args is present
    if letter != ' ':
        # letter function
        # fills in letters called from args
        # loops through len of word, checks if letter is same as letter inputted
        # then takes index and replaces that index in the word array
        for index in range(0,len(word)):
            # print(index,word[index])

            if letter.lower() == word[index]:

                word_ar[index] = word[index]
        # One liner:
        return word_ar


        # word_ar = new_word_array
        # return word_ar
    # else:
    #     #word array
    #     print(*word_ar)



# make_array(hang_word,'a')
correct = True
penalty_list = []
used_letters = []


while correct:
    if ''.join(word_ar) == hang_word:
        print()
        print('Hooray, Good Job')
        print(f"Your word was '{hang_word}'")
        correct = False
    else:
        print(*word_ar)
        user = str(input('Make a single letter guess: '))
        if len(user) > 1 or user == "":
            print("Error, type a single letter!")
        else:
            if user.lower() in hang_word:
                if user.lower() in used_letters:
                    # when the letter you already guessed correctly is used again as your guess
                    print("Already used!")
                else:
                    used_letters.append(user.lower())
                    print('Correct letter!')
                make_array(hang_word,user.lower())
            elif user.lower() in penalty_list:
                # when the letter already guessed incorrectly is used again
                print("You have tried that letter already!")
            else:
                # warns the user to try again
                penalty_list.append(user.lower())
                print("Try again")
