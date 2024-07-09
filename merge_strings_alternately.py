#Merge Strings Alternatively Problem

#First Attempt
def mergeAlternately(word1, word2):
    new_string = ""
    for i, j in zip(word1, word2):
        new_string = new_string + i + j

    if len(word1) > len(word2):
        leftover_letters = word1[len(word2):]
        return new_string + leftover_letters
    elif len(word2) > len(word1):
        leftover_letters = word2[len(word1):]
        return new_string + leftover_letters
    else: 
        return new_string

word1 = "abcdes"
word2 = "pqr"
print(mergeAlternately(word1, word2))

            
        