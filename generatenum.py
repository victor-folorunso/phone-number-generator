import random

print("step1: input constant characters \nstep2: input total length of all characters\nstep3: the bot will generate all phone numbers!!!")
print('NOTE: THE + WOULD AUTOMATICALLY BE PREFIXED')
all_number_len = int(input("\nenter total character length: "))
const_number_len = int(input("enter total constant character length: "))

number_constants = []
print('enter constant: +')
for item in (const_number_len * 'x'):   # x is just a multiplucant.it is useless
	single_const = input("enter constant: ")
	number_constants.append(single_const)
	
joint_const = "+" + ''.join(number_constants) #join all the constants,with the plus
rem_numbers = all_number_len - len(number_constants)
characters = ['0','1','2','3','4','5','6','7','8','9']
numbers = []

while True:
	cache_num = []
	len_num_count = 0
	while len_num_count != rem_numbers:
		cache_num.append(random.choice(characters))
		len_num_count += 1
	#make list become plain text(joined)
	result = ''.join(cache_num)
	#store password in list "numbers"
	if result not in numbers:
		numbers.append(result)	
	if len(numbers) == pow(len(characters), rem_numbers):#possible_combinations
		break	
		

for derived in numbers:
	print(joint_const + derived)
#print(len(numbers))
