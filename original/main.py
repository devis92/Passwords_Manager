#Password Generator Project
import random
from random import choice, randint, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PassGen:
  def __init__(self):
    self.password = self.generate()
  
  def generate(self):
    global letters, numbers, symbols
    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  
    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    return password
    
    
  
  # def __init__(self):
  #   self.nr_letters = random.randint(8, 10)
  #   self.nr_symbols = random.randint(2, 4)
  #   self.nr_numbers = random.randint(2, 4)
  #   self.password_list = []
    
  # def generate(self):
  #   for char in range(self.nr_letters):
  #     self.password_list.append(random.choice(letters))

  #   for char in range(self.nr_symbols):
  #     self.password_list += random.choice(symbols)

  #   for char in range(self.nr_numbers):
  #     self.password_list += random.choice(numbers)

  #   random.shuffle(self.password_list)

  #   password = ""
  #   for char in self.password_list:
  #     password += char
  #   print(f"Your password is: {password}")
