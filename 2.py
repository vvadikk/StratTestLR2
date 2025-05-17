letters = ['a', 'x', 'y', 'z', 'w', 'o', 'v']
numbers = [5, 7, 2, 1, 11, 9, 0]
d = dict(zip(letters, numbers))
print(d)
s = sum(d.values())
print('Сумма:', s)
with open('ex2-1.txt', 'w') as f:
    f.write(str(s))
