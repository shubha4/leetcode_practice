#Merge Strings Alternatively Problem

#First Attempt - with strings
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

#Second Attempt - with list
def mergeAlternately(word1, word2):
    new_string_list = []
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        new_string_list.append(word1[i])
        new_string_list.append(word2[i])
    new_string_list.extend(word1[min_length:])
    new_string_list.extend(word2[min_length:])
    return ''.join(new_string_list)

word1 = "abcdes"
word2 = "pqr"
print(mergeAlternately(word1, word2))
       