# import random
# random.choice() - This function is used to generate 1 random number from a container.

# random.randrange() - This function is also used to generate random number but within a
# range specified in its arguments.

# random.seed() - This number is used to generate a float random number less than 1
# and greater or equal to 0.

# random.random() - This function maps a particular random number with the seed argument mentioned.
# All random numbers called after the seeded value returns the mapped number.

# random.shuffle() - This function is used to shuffle the entire list to randomly arrange them.

# random.uniform() - This function is used to generate a floating point random number between
# the numbers mentioned in its arguments.

# Eg: 1
import random
print('\t \t Hi!! \n Welcome To Todays Python Horoscope')

s1 = input('Enter your Name: ')
sum = 0
ans = 0
for val in s1:
    val1 = ord(val)
    sum = sum+val1
# print(sum)
while sum != 0:
    i = sum % 10
    ans = ans+i
    sum = sum/10
# print(int(ans))
ans = random.randrange(1, 11)
if ans == 1:
    print('You will have Lucky day')
elif ans == 2:
    print('Your Crush Will talk to you')
elif ans == 3:
    print('Carefull with your words')
elif ans == 4:
    print('Will meet your Love')
elif ans == 5:
    print('Careful while handling vehicles')
elif ans == 6:
    print('You will receive a gift')
elif ans == 7:
    print('Unexpected thing will happen to you')
elif ans == 8:
    print('Be silent Today')
elif ans == 9:
    print('Some one is Missing you today')
elif ans == 10:
    print('Today will be a Sleepy day')
elif ans == 11:
    print('Careful With Relationships')
else:
    print('Your chance is tomorrow')
