n = int(input().strip())

numbers = str(bin(n)[2:]).split('0')
lenghts = [len(num) for num in numbers]
print(max(lenghts))