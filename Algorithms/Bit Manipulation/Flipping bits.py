def flippingBits(n):
    uu = '{:032b}'.format(n)
    uuu = str(uu)
    print (uuu)
    ss = ''
    for i in uuu :
        if i == '1':
            ss = ss + '0'
        else:
            ss = ss + '1'
    gh = int(ss,2)
    return (gh)

