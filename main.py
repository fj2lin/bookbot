def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    print(get_book_text("books/frankenstein.txt"))

main()