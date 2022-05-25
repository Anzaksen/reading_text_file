# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open(filename, "r")
    open_file = file.read()
    return open_file


def count_words():
    text = read_file_content("./story.txt")
    dict1 = {}
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('?', '')
    text = text.replace('\n', '')
    list1 = text.split(' ')
    list1.remove('')
    for word in list1:
        if word not in dict1:
            dict1[f'{word}'] = 1
        else:
            dict1[f'{word}'] += 1
    print(list1)
    return dict1


f = count_words()
print(f)
