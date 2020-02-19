import sys


def create_chardict(word):
    word = word.lower()
    chardict = {}
    for char in word:
        if char in chardict.keys():
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict


def areanagrams(word1, word2):
    chardict1 = create_chardict(word1)
    chardict2 = create_chardict(word2)
    if chardict1 == chardict2:
        return True
    else:
        return False

# test areanagrams print(areanagrams("listen", "Silent"))


def findanagrams(words):
    print("List of all anagrams:")
    for i, word1 in enumerate(words[:-1], 1):
        for word2 in words[i:]:
            if word1 != word2 and areanagrams(word1, word2):
                print(word1, word2)


try:
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        words = [line.rstrip('\n') for line in file]
except IndexError:
    print("Please enter file name.")
except IOError:
    print("File does not exist.")
else:
    findanagrams(words)
