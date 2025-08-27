from stats import get_num_words
from stats import get_c_count
import sys



def get_book_text():
    with open(sys.argv[1]) as f:
        file_content = f.read()
        return file_content


def main():
    print(sys.argv)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {sys.argv[1]}...\n")
    file = get_book_text()
    num_words = get_num_words(file) 
    print("--------- Word Count -------\n")
    print(f"Found {len(num_words)} total words")
    print("--------- Character Count -------\n")
    
    c_counts = get_c_count(file)
    
    for c, value in sorted(c_counts.items()):
        print(f"{c}: {value}")
    #print(c_counts)

def check_args():    
    if len(sys.argv) >= 2:
        print("hello")
        main()
        sys.exit(0)
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

check_args()
