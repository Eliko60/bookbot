def get_book_words_num(file_path):
    with open(file_path) as f:
        file_content = f.read()
        words = file_content.split()
        word_count = len(words)
    return file_content, word_count
def character_count(file_content):
    characters = {}
    list_of_chr = []
    for character in file_content:
        chr_lower = character.lower()
        if chr_lower not in list_of_chr:
            list_of_chr.append(chr_lower)
    characters = dict.fromkeys(list_of_chr)
    for chr in file_content:
        chr_lower = chr.lower()
        if characters[chr_lower] == None:
            characters[chr_lower] = 1
        else:
            characters[chr_lower] += 1
    return characters
def generate_report(characters, word_count):
    def sort_on(item):
        return item[1]
    sorted_list = sorted(characters.items(), reverse=True, key=sort_on)
    sorted_dict = {}
    for key, value in sorted_list:
        sorted_dict[key] = value
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in list(sorted_dict.items()):
        key, value = item
        if key.isalpha() == True:
            print(key+":", end=" ")
            print(value)
    print("============= END ===============")


    
