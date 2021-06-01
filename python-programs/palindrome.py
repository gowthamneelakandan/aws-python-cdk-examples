name="pip"
def palindrome(name):
  if name == name[::-1]:
    print("Palindrome")
  else:
    print("Not Palindrome")

palindrome(name)
