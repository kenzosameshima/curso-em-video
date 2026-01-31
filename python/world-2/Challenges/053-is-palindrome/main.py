string_input = input('Type anything: ')

normalized_string = ''.join(
    char.lower()
    for char in string_input
    if char.isalnum()
)

if normalized_string == normalized_string[::-1]:
    print(f'The string "{string_input}" is a palindrome.')
else:
    print(f'The string "{string_input}" is not a palindrome.')
