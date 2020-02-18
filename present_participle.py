import sys

vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # y must be included, otherwise we get wrong answers for words like play
verb_list = sys.argv[1:]

for verb in verb_list:
    if verb[-2:] == "ie":
        verb = verb[:-2] + "ying"
    elif len(verb) > 2 and verb[-1] == "e":  # len(verb) > 2 is for the word 'be'
        verb = verb[:-1] + "ing"
    elif len(verb) > 2 and (verb[-3] not in vowels and verb[-2] in vowels and verb[-1] not in vowels):
        verb = verb + verb[-1] + "ing"
    else:
        verb = verb + "ing"
    print(verb)

# test verbs: swim look play bake lie run sing be
