phrase = input("Enter a phrase: ").strip()
lower_phrase = phrase.lower()

count = lower_phrase.count('a')
print(f"There are {count} occurrences of the letter 'a' in the phrase.")

if count > 0:
    print(f"The first occurrence of 'a' is at position {lower_phrase.find('a') + 1}.")
    print(f"The last occurrence of 'a' is at position {lower_phrase.rfind('a') + 1}.")
else:
    print("The letter 'a' does not appear in the phrase.")
