import textwrap
# -*- coding: utf-8 -*-

introduction = "This is a quiz based on Python concepts. \
                You can choose between 3 levels of difficulty: \
                easy, medium and hard,\
                Each of them includes 4 gaps to fill, you can choose \
                how many times per gap you can fail."
level_list = ["1", "2", "3"]
sentence_list = ["___1___ loops are traditionally used when you have a block of code \
                 which you want to repeat a fixed number of times. \
                 The ___2___ loop, used when a condition needs to be checked \
                 each iteration, or to repeat a block of code forever. \
                 ___3___ programming language allows to use one loop \
                 inside another loop, the inner loop is called ___4___",
                 "The ___1___ statement rejects all the remaining statements in the current \
                 iteration of the loop and moves the control back to the top \
                 of the loop. ___2___ terminates the loop statement and \
                 transfers execution to the statement immediately following \
                 the loop. The ___3___ statement in Python is used when a \
                 statement is required syntactically but you do not want any \
                 command or code to execute. If the else statement is used \
                 with a ___4___ loop, the else statement is executed when \
                 the loop has exhausted iterating the list.",
                 "When a class definition is entered, a new ___1___ \
                 is created, and used as the ___2___ scope, thus, all \
                 assignments to ___3___ variables go into this new \
                 ___4___. In particular, function definitions bind\
                 the name of the new function here."]

"""Hard coded answers which match the locations of text to be replaced,
If player answers correctly but with wrong first letter case then
the correct sentence displayed after winning the quiz will be with
correct case."""
answer_list = [["For", "while", "Python", "nested"],
               ["Continiue", "Break", "Pass", "for"],
               ["namespace", "local", "local", "namespace"]]

"""A list of words to be replaced passed in to the play game function."""
to_be_replaced = ["___1___", "___2___", "___3___", "___4___"]

def word_in_pos(word, parts_of_speech):
    """Checks if a word in parts_of_speech is a
    substring of the word passed in."""
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def pick_difficulty():
    """Asks for player to pick difficulty, an integer
    between 1 and 3, if the player types something else,
    prompt the player again"""
    
    level = raw_input("Pick a number between 1 and 3 to choose difficulty ")
    if level in level_list:
        return int(level)
    else:
        return pick_difficulty()

def pick_fails():
    """Allows player to pick how many wrong answers they can give
    per question and outputs their choice.
    If user input is not an integer, the function is called again."""
    
    fails = raw_input("Choose a number of times a question can fail ")
    try:
        fails = int(fails)
    except ValueError:
        return pick_fails()
    else:
        return fails

def replace_element(list, old_element, new_element):
    """ Check if an element is in a list and replace that
    element with a new element, return modified list"""

    if old_element in list:
        index = list.index(old_element)
        list[index] = new_element
    return list

def get_input(sentence, current_answer_list, word, replacement,
              replaced, wrong_answer_count, fails):
    """Get user input for current gap at current level of difficulty.
    
    If input matches with appropriate answer from anser_list current level
    replace the gap with according answer.
    
    Else increment wrong_anwer_count by 1 and check if game is over
    or if not, recursively prompt for another input."""
    answer_position = to_be_replaced.index(replacement)
    user_input = raw_input("Type in a: " + replacement + " ")
    if user_input.lower() == current_answer_list[answer_position].lower():
        word = current_answer_list[answer_position]
        replace_element(sentence, replacement, word)
        print textwrap.fill(" ".join(sentence), 70)
        replaced.append(word)
    else:
        print "Not Correct"
        wrong_answer_count = wrong_answer_count + 1
        print wrong_answer_count
        if wrong_answer_count == fails:
            print "Game Over, You have failed " + str(fails) + " times!"
            new_game()
        else:
            get_input(sentence, current_answer_list, word, replacement,
                      replaced, wrong_answer_count, fails)

def new_game():
    """Ask player if they would like to play again if answer is yes
    start a new game by calling play_game, if answer is anything
    else, exit the quiz."""

    game = raw_input("For a new game type yes ").lower()
    if game == "yes":
        play_game()
    else:
        print"Good Bye"
        raise SystemExit

def play_game():
    """Starts the quiz by invoking function which returns the level of
    difficulty which in turn saves the variables of appropriate sentence, answer list
    and the prints the sentence.

    For loop will iterate over the sentence and check if current word is
    in the words to be replaced list.

    If yes, then get_input function is called which gets user input and checks
    it's correctness and pushes correct answer to the replaced list
    If not, the current word will be pushed to replaced list.

    Replaced list will be joined to a string a printed and user is prompted for a
    new game"""

    print (textwrap.fill(introduction, 70))
    difficulty = pick_difficulty() - 1
    fails = int(pick_fails())
    current_answer_list = answer_list[difficulty]
    sentence = sentence_list[difficulty].split()
    print(textwrap.fill(" ".join(sentence), 70))
    wrong_answer_count = 0
    replaced = []
    for word in sentence:
        replacement = word_in_pos(word, to_be_replaced)
        if replacement is not None:
            get_input(sentence, current_answer_list, word, replacement,
                      replaced, wrong_answer_count, fails)
        else:
            replaced.append(word)
    print (textwrap.fill(" ".join(replaced), 70))
    print "You won!"
    new_game()

print play_game()
