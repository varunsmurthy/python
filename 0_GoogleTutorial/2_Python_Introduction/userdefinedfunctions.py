import sys


def repeat(word, count):
    op_str_1 = word * count

    op_str_2 = ''
    for i in range(count):
        op_str_2 = op_str_2 + word

    print(op_str_1)
    print(op_str_2)


def main():
    if len(sys.argv) > 1:
        word = sys.argv[1]
        count = sys.argv[2]
        repeat(word, int(count))
    else:
        print('No arguments')


if __name__ == '__main__':
    main()
