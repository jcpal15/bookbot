def main():
    book_path = "books/frankenstein.txt"
    print(f"---This is a silly report on {book_path}---")
    book_text = get_book_text(book_path)
    book_wc = get_word_count(book_text)
    character_count = get_character_count(book_text)
    print(f"The book has {book_wc} words.")
    bdict = baby_dict(character_count)
    sort_dict(bdict)
    
    
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    characters = text.lower()
    char_count_dict = {}
    for char in characters:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict

def baby_dict(dict):
    letters = []
    for x in dict:
        if x.isalpha(): 
            baby_dict = {'letter' : x , 'count' : dict[x]}
            letters.append(baby_dict)
    return letters

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    dict.sort(reverse=True, key=sort_on)
    for x in dict:
        print(f"This book contains the letter {x['letter']} {x['count']} times. Isn't that mudane?")
    
            


main()