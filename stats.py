
def get_num_words(book):
    words = book.split()
    return (words)    


def get_c_count(book):
    words = book.lower()
    c_count = {}

    for c in words:
        if c in c_count:
            c_count[c] += 1

        else:
            c_count[c] = 1


    return c_count 
