import os
import wordle.wordle as wordle

# TODO qol stuff, maybe color code functions? combine has and has at?

path = os.path.join('../data', 'dict.txt')
word = wordle.Wordle(path)