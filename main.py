# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

# anagram
def find_anagrams(sentence):
    # [assignment] Add your code here
    words = sentence.split(' ')
    for i in range(len(words)):
        if not words[i] == words[i + 1]:
            return False
        else:
            return True


def find_anagram2(word1, word2):
    if not len(word1) == len(word2):
        return False
    else:
        for i in range(len(word1)):
            if not word1[i] == word2[i]:
                return False
            else:
                return True
            


# palindrome
def find_palindrome(word):
    for i in range(len(word)):
        if not word[i] == word[len(word) - i - 1]:
            return False
        else:
            return True


print(find_anagrams("racecar racecar"))
print(find_anagram2("awe", "awe"))
print(find_palindrome("paper"))
