import random

# Magic 8-Ball setting up
name = "Sem"
question = "Is Pear silly?"
answer = ""

# Generating a random number
random_number = random.randint(1, 12)
print(random_number)

# Control Flow 
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "As you wish"
elif random_number == 11:
  answer = "Of course, no need to ask"
elif random_number == 12:
  answer = "Always"
else:
  answer = "Error"

# Control flow of name
if name == "":
  print(f"{question}")
# Control flow of question
if question == "":
  question = input("Please ask a question: ")
else:
  print(f"{name} asks a question: {question}")
# See the result
print(f"Magic 8-Ball's answer: {answer}")