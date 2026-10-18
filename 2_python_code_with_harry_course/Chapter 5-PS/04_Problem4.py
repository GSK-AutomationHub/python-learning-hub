# Create an empty dictionary. Allow 4 friends to enter their favorite language as value
#  and use key as their names. Assume that the names are unique.


def get_friend_fav_language():
    fav_lang = {}
    for i in range(1,5):
        name = input("Please enter your name: ")
        language = input("Please enter your favorite prog. language: ")
        fav_lang.update({name:language})
    return fav_lang

print(get_friend_fav_language())

# If the names of 2 friends are same; what will happen to the program in problem ?
# ---> latest K:V pair will override eariler one

# If languages of two friends are same; what will happen to the program in problem ?
# ---> dict ll get created  w/o error, dict accepts duplicate values
