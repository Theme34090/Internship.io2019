import json
import random
import os

class Round:
    score = 0
    word = ''
    correct_guess = []
    wrong_guess = []
    count = 0
    remaining_letters = 0
    hints = []
    unique_letter = []

    def __init__(self, word, hints, score):
        self.word = word
        self.score = score
        self.hints = hints
        self.correct_guess = []
        self.wrong_guess = []
        self.count = 8
        tmp = []
        for i in word:
            if i.lower() not in tmp and i.isalpha():
                tmp.append(i.lower())
        self.remaining_letters = len(tmp)
        self.unique_letter = tmp

    def __str__(self):
        out = ''
        for i in self.word:
            if i.lower() in self.correct_guess:
                out += i + ' '
            elif not i.isalpha():
                out += i + ' '
            else:
                out += '_ '
        wrong_guessed = ''
        for i in self.wrong_guess:
            if i not in wrong_guessed:
                wrong_guessed += i + ' ,'
        return out.strip() + '   score: ' + str(self.score) \
            + ' , remaining guess: ' + str(self.count) \
            + ' , wrong guessed: ' + wrong_guessed.strip(', ')

    def check_answer(self, ans):
        ans = ans.lower()
        if ans in self.wrong_guess + self.correct_guess:
            self.score -= len(self.word)
            if self.count > 1:
                print('Already guessed. Try other letter')
            else:
                print("Pls don't spam")
        elif ans in self.word.lower():
            self.correct_guess.append(ans)
            self.set_score(ans)
            self.remaining_letters -= 1
            return
        else:
            self.wrong_guess.append(ans)
            print('Wrong guessed!')
        self.count -= 1

    def get_hint(self, level):
        try:
            hint = self.hints[level]
            if level != 0:
                self.score -= len(self.word) / 3
            return hint
        except IndexError:
            print('No more hint!')
            return ''

    def set_score(self, ans):
        self.score += len(self.word) / len(self.unique_letter)


def check_valid(ans):
    if ans == 'exit':
        exit()
    if ans == 'restart':
        return 'restart'
    if ans == 'hint':
        return 'hint'
    if (not ans.isalpha()) or len(ans) > 1:
        print('Please enter valid answer')
        return False
    return True


def select_category():
    print('Please select category by number')
    category = {}
    cnt = 1
    for k in words.keys():
        category[cnt] = k
        print(str(cnt) + ' : ' + k)
        cnt += 1
    while True:
        try:
            selected_category = words[category[int(input('>>> '))]]
            return selected_category
        except:
            print('Please enter valid category number')


# main program
'''
try:
    with open("words.json", "r") as read_file:
        words = json.load(read_file)
except FileNotFoundError:
    print('words.json not found! please try again.')
    exit()
'''
words = {}
for filename in os.listdir(os.getcwd()):
    if '.json' in filename:
        with open(filename, "r") as read_file:
            tmp = json.load(read_file)
            words.update(tmp)
print("Welcome to Hangman\n\n"
      "Available command\n"
      "- 'hint' : get a hint\n"
      "- 'exit' : terminate the game\n"
      "- 'restart' : restart the game\n")
selected_category = select_category()
total_score = 0
round_number = 1
used_words = []
category_complete = False
while True:
    reset_game = False  # reset category, score, round_number, used_words
    if category_complete:
        selected_category = select_category()
        category_complete = False
    while True:
        # Check for available word
        while True:
            word = random.choice(list(selected_category.keys()))
            if word not in used_words:
                used_words.append(word)
                break
            if len(used_words) == len(selected_category):
                print('\nRun out of word! please select another category.')
                category_complete = True
                break
        if category_complete:
            break  # only reset category
        # Round start
        rnd = Round(word, selected_category[word], total_score)
        hint_level = 1
        hint = ''
        print('\nRound {} start!'.format(round_number))
        print(rnd.get_hint(0))
        # each guess
        while rnd.count > 0:
            print(rnd)
            ans = str(input('>>> '))
            valid = check_valid(ans)  # check for invalid answer
            if valid == 'restart':
                reset_game = True
                break
            elif valid == 'hint':
                hint = rnd.get_hint(hint_level)
                if hint:
                    print('Hint : ' + hint)
                hint_level += 1
            elif not valid:
                continue
            else:
                rnd.check_answer(ans)
            if rnd.remaining_letters == 0:
                round_number += 1
                print(rnd.word)
                print("Congrats! You got it right.")
                total_score = rnd.score
                total_score = total_score // 1
                print("Total score : " + str(total_score))
                break
        if rnd.remaining_letters == 0:
            continue
        if reset_game:
            selected_category = select_category()
            total_score = 0
            round_number = 1
            used_words = []
            break
        print('You are dead! The correct answer is "{}"'.format(rnd.word))
