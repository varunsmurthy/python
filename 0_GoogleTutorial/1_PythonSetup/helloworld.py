import sys


def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'World'
    print('Hello' + name)
    print('Hello', name)

    print('Number of arguments = ', len(sys.argv))
    print('Arguments = ', sys.argv)


if __name__ == '__main__':
    main()
