***********
* HANGMAN *
***********

* REQUIREMENT *
- need json package to run.
- words.json must be in the same directory with hangman.py.

* HOW TO PLAY *
- run hangman.py with words.json in the same directory.
- choose category by number.
- program will take a random word from selected category within words.json.
- enter your (valid) answer one letter at a time. invalid answer contains special character or multiple letter or number.
- enter 'restart' to restart the game. total score will be reset to 0.
- enter 'exit' to terminate the program.
- you can add or modify words / hints / categories from words.json

* USING HINT *
- hint will be given for free once per round.
- enter 'hint' to show available hint.
- for each hint used, your score will be deducted by 33% of length of word.
- some word contains multiple hint that further gives you information.

* SCORING *
- each correct guess rewards score equal to (length of word)/(each presence of that letter).
- using hint will deduct your total score for 33% of length of word.
- guessing letter that have already been guessed will deduct score equal to length of word.
- score can be deducted to below 0.
- after finish each round, score will be kept.
