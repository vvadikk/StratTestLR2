#Вариант 19
def is_a_palindrome(s):
    if s == ''.join(reversed(s)):
        return 'Палиндром'
    else:
        return 'Не палиндром'
s = input('Введите строку: ')
print(is_a_palindrome(s))