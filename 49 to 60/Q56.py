# Longest Word in a Sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print("The longest word is:", longest_word)

#key=len argument tells Python to compare the words based on their length.