def replace_word(abstract,word_to_replace,word_replacement):
    return abstract.replace(word_to_replace,word_replacement)

abst_input = input("Enter an abstract : ")
word_to_replace = input("Enter the word to replace : ")
word_replacement = input("Enter the word to replace with : ")

print("\nYou entered : "+abst_input)
print("\nAfter replacement : "+replace_word(abst_input,word_to_replace,word_replacement))