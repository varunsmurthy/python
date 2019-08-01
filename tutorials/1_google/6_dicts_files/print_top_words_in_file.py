import sys
from count_words import count_words_in_file


def get_dict_value(dict_tuple):
    return dict_tuple[1]


def get_top_n_words(master_word_count_dict, n):
    top_n_words_list = []
    sorted_input_list = []
    sorting_pointer = 0;
    for k,v in reversed(sorted(master_word_count_dict.items(), key=get_dict_value)):
        sorted_input_list.append((k,v))

    ip_word_count = len(master_word_count_dict)
    if n<ip_word_count:
        for i in range(n):
            top_n_words_list.append(sorted_input_list[i])
    else:
        top_n_words_list = sorted_input_list

    return top_n_words_list


def main():
    filename = "small.txt"
    top_word_count = 5;
    word_count_dict = count_words_in_file(filename)
    top_words_list = get_top_n_words(word_count_dict, top_word_count)
    print(filename,":")
    print(top_words_list)

    filename = "alice.txt"
    top_word_count = 5;
    word_count_dict = count_words_in_file(filename)
    top_words_list = get_top_n_words(word_count_dict, top_word_count)
    print(filename, ":")
    print(top_words_list)

if __name__ == "__main__":
    main()