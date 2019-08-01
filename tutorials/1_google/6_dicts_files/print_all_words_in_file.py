import sys
import count_words


def main():
    filename = "small.txt"
    print(filename,":")
    print(count_words.count_words_in_file(filename))

    filename = "alice.txt"
    print(filename, ":")
    print(count_words.count_words_in_file(filename))


if __name__ == "__main__":
    main()