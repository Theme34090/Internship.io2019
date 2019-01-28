***********
* HANGMAN *
***********

* REQUIREMENT *
- need json and round package to run.
- words.json must be in the same directory with hangman.py.

* HOW TO PLAY *
- run hangman.py with words.json in the same directory.
- choose category by number.
- program will take a random word from selected category within words.json.
- enter your (valid) answer one letter at a time. invalid answer contains special character or multiple letter or number.
- enter 'restart' to restart the game. total score will be reset to 0.
- enter 'exit' to terminate the program.
- you can add or remove words / hints / categories from words.json

* USING HINT *
- hint will be giver for free once per round.
- enter 'hint' to show available hint.
- for each hint used, your round's score will be deductd by .
- some word contains multiple hint that further gives you information.

* SCORING *
- each correct guess rewards score equal to (length of word)/(each presence of that letter).
- using hint will deduct round's score by 33%.
- guessing letter that have already been guessed will deduct score equal to length of word.
- score can be deducted to below 0.
- after finish each round. score will be added to total score for that game.