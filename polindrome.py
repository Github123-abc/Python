num = input('Enter the number:')
rev = ''.join(reversed(num))
if (num == rev):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')
