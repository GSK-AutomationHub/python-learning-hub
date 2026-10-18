# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

hindi_eng_dict = {'Najdik':'near', 'dur':'far away', 'utho':'stand up', 'baitho': 'sit down'}

for k, v in hindi_eng_dict.items():
    print(f"'{k}' in hindi means '{v}' in english")