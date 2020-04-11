if __name__ == '__main__':
    str = raw_input()
    digit=False
    alpha=False

    for c in str:
        if c.isdigit():
            digit=True
        if c.isalpha():
            alpha=True
        if alpha and digit:
            break

    print digit or alpha
    print alpha
    print digit
    print alpha and ( str.islower() or not str.isupper() )
    print alpha and ( str.isupper() or not str.islower() )