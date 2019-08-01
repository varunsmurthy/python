import sys


def count_words_in_string(sentence, word_count_dict):
    for word in sentence.split():
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1


def main():
    print("entering main")
    parent_word_count_dict = {}
    count_words_in_string("this is the first sentence being used the first time", parent_word_count_dict)
    print(parent_word_count_dict)
    count_words_in_string("this is now th second sentence", parent_word_count_dict)
    print(parent_word_count_dict)


if __name__ == "__main__":
    main()
