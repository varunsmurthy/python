def strings():
    a = "Hello"
    print (a + "Alice")
    print (a, "Bob")
    print (a + "%s" %("Nick"))
    print (a.lower())
    print (a.upper())
    print (len(a))
    print (a[1:3])
    print (a[0])


def main():
    strings()
    
if __name__ == '__main__':
    main()