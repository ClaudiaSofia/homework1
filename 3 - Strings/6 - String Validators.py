if __name__ == '__main__':
    s = raw_input()
    print any(e.isalnum() for e in s)
    print any(e.isalpha() for e in s)
    print any(e.isdigit() for e in s)
    print any(e.islower() for e in s)
    print any(e.isupper() for e in s)