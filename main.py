# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

t = (name1 + name2).lower().count("t")
r = (name1 + name2).lower().count("r")
u = (name1 + name2).lower().count("u")
e = (name1 + name2).lower().count("e")

true_total_count = t + r + u + e

l = (name1 + name2).lower().count("l")
o = (name1 + name2).lower().count("o")
v = (name1 + name2).lower().count("v")
e = (name1 + name2).lower().count("e")

love_total_count = l + o + v + e

combine_true_and_love = int(str(true_total_count) + str(love_total_count))

print(combine_true_and_love)
if true_total_count<10 or love_total_count <10:
  if combine_true_and_love < 10 or combine_true_and_love > 90:
    print(f"Your score is {combine_true_and_love}, you go together like coke and mint.")
  elif combine_true_and_love >= 40 and combine_true_and_love <= 50:
    print(f"Your score is {combine_true_and_love}, you are alright together")
  else:
    print(f"Your score is {combine_true_and_love}")
else:
  print("You are not for each other")