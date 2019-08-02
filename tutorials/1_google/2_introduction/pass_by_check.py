import sys


def check_numerical(ip_numerical):
    ip_numerical = ip_numerical + 5


def check_string(ip_string):
    ip_string = ip_string + " is modified"


def check_list(ip_list):
    ip_list.append(5)
    ip_list[0] = 10


def check_dict(ip_dict):
    ip_dict["added_key1"] = 10
    ip_dict["added_key2"] = 20


def main():
    a = 5
    print("before calling: a = " + str(a))
    check_numerical(a)
    print("after calling: a = " + str(a))

    a = "test string"
    print("before calling: a = " + str(a))
    check_string(a)
    print("after calling: a = " + str(a))

    a = [0,1,2,3,4,5]
    print("before calling: a = " + str(a))
    check_list(a)
    print("after calling: a = " + str(a))

    a = {'this': 77, 'there': 45, 'hi': 10, 'at': 23, 'Hello': 7}
    print("before calling: a = " + str(a))
    check_dict(a)
    print("after calling: a = " + str(a))

if __name__ == "__main__":
    main()