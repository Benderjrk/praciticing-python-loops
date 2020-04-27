dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print(breed)

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)
  
for sport in sport_games:
  print(sport)

promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  print(student)
  students_period_B.append(student)

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students.pop())
  
print(students_in_poetry)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  print(location)
  for sold in location:
    scoops_sold += sold 
    print(scoops_sold)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print(fahrenheit)

single_digits = range(10)
squares = []
cubes = [digit ** 3 for digit in single_digits]
for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)
  
print(squares)
print(cubes)

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price

print(total_price)
average_price = total_price / len(prices)

print("Average Haircut Price:\n" + format(average_price, '.2f'))
print("Prices:", prices)
new_prices = [price - 5 for price in prices]

print("New Prices:" ,new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  
print("Total Revenue:\n" + str(total_revenue))

average_daily_revenue = total_revenue / 7

print(average_daily_revenue)

#new list with price under 30
#list hairstyles
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30 ]

print("Cuts under 30", cuts_under_30)
  
#Write your function here
def divisible_by_ten(nums):
  divisible = [num for num in nums if num % 10 == 0]
  return len(divisible)

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Write your function here
def delete_starting_evens(lst):
  # if the len isnt 0 and the first list item isn't even
  while (len(lst) > 0 and lst[0] % 2 == 0):
    # the the lst and remove the first Item of the list and keep looping until its out of the even numbers first
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Write your function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

#Write your function here
def odd_indices(lst):
  new_list = []
  for i in range(1, len(lst), 2):
    new_list.append(lst[i])
  return new_list  

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Write your function here
def exponents(bases, powers):
  lst = []
  for i in range(len(bases)):
    for t in range(len(powers)):
      lst.append(bases[i] ** powers[t])
  return lst
    
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#Write your function here
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for i in range(len(lst)):
    sum += lst[i]
    if sum > 9000:
      break
  return sum
    

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here
def max_num(nums):
  max = int()
  for i in range(len(nums)):
    if nums[i] > max:
      max = nums[i]
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_lst.append(i)
  return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Write your function here
def reversed_list(lst1, lst2):
  print(lst2)
  lst2.reverse()
  print(lst2)
  if lst1 == lst2:
    return True
  else:
    return False


#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))