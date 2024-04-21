import random
def generate_password(length):
  lowercase = 'abcdefghijklmnopqrstuvwxyz'
  uppercase = lowercase.upper()
  digits = '0123456789'
  special_chars = '!@#$%^&*'
  password = ""
  password += random.choice(lowercase)
  password += random.choice(uppercase)
  password += random.choice(digits)
  password += random.choice(special_chars)
  for _ in range(length - 4):
    password += random.choice(lowercase + uppercase + digits + special_chars)
  return password
password_length = int(input("Enter desired password length: "))
generated_password = generate_password(password_length)
print("Your generated password is:", generated_password)
