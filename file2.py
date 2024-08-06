# languages={
# 'hatim':['urdu','pashtu'],
# 'nadeem':['english','math'],
# 'naeem':['pythton','ruest'],
# 'nasir':['balogy','bunjapi']}

# # print(languages)

# for name,language in languages.items():
#     print(f'it is a name title     {name.title()}')
#     for num in language:
#         print(f' all the language    {num.title()}')


# name="muhammad  numan  khan  of dera ismail khan :"
# print(name.title())

# print(name.upper())

# name="MUHAMMAD  NUMAN  KHAN  OF DERA ISMAIL KHAN"
# print(name.lower())


# first_name="muhsin"
# last_name="shaha"
# full_name=f" {first_name}   {last_name}"
# print(full_name)

# a=7
# b=7
# n=a+b
# print(n)

# a='8'
# b='8'
# c=a+b

# print(c)

# first='musa'
# last='khan'
# full_name=first +"  "+'last'
# # print(full_name)

# full_name=f" mulana {first}  {last}  :"

# print(full_name.upper())


# list=['ali','hashim','asif','nadeem','babar','naeem']
# print(list)

# print(list[1:3])

# add=f' {list[1]}   to {list[4]}'
# print(add)
# sum=list[2]+'  '+list[4]
# print(sum.upper())

# list=[11,33,4,5,5,7,8,8,9,10]

# print(list)

# print(list[0])
# print(list[-4])

# prayer_name=['zuhar','asar','maghrib','isha','fajar','tahajud',]
# print(prayer_name)
# prayer_name.insert(5,'ishraq')
# print(prayer_name)

# prayer_name.append('jasht')
# print(prayer_name)

# del prayer_name[1]
# print(prayer_name)

# prayer_name.pop(3)
# print(prayer_name)

# prayer_name[3]='ishraq'
# print(prayer_name)

# cars =['feed','happy','public','amir','nadeem','zahid','waseem']
# print(cars)

# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# list=[3,5,6,7,9,6,4,3,9,1,0]
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# student=['aslam','asif','amir','hilal','atif','shakir']
# print(student[0])
# print(student[1])
# print(student[2])
# print(student[3])

# for x in student:
#     print(x.title())
#     print(f'{x} student name is good')
# print('thnak')

# for value in range (88):
#     print(value)

# for y in range(15):
#     print(f" sqrare  is",y**2)


# num=[1,2,3,4,5,6,7,8,9,10]
# for number in num:
#     print(number)


# for x in range(22):
#     print(f' cube root is ',x**3)


# cars =['computer','laptop','book','pen']
# for car in cars:
#     if car =='pen':
#         print(car.upper())
#     else:
#         print(car.title())


# cars =['computer','laptop','book','pen']
# for car in cars:
#     if car !='pen':
#         print(car.upper())
#     else:
#         print(car.title())

# age=19
# if age >=18:
#     print(f"you are elder to vote ")
#     print(f'you are cast to vote',)
# else:
#     print(f" you are  very small")
#     print(f" you are waiting to vote")

# age=17
# if age <12:
#     print('kid')
# elif age < 18:
#     print('teen')
# else:
#     print('aduld')


# obtain_number=360
# if obtain_number > 240:
#     print('muqabool')
# elif obtain_number>300:
#     print('jiad')
# elif obtain_number >360:
#     print('jaid jidn')
# else:
#     print('mumtaz')


# obtain_number=360
# if obtain_number < 240:
#      print('rasib')
# elif obtain_number<300:
#      print("maqabool")
# elif obtain_number <360:
#     print('jaid ')
# elif obtain_number <400:
#     print('jisd jidun')
# else:
#      print('mumtaz')


# for value in range(1,22,2):
#     print(value)

# squares=[]
# for x in range(1,11):
#    squares.append(x)
# print(squares**2)


# squares=[]
# cube=[]
# for value in range(1,13):
#     square=value**2
#     squares.append(square)
#     cubes=value**3
#     cube.append(cubes)
    

# print(squares)
# print(cube)


# list=[]
# my_list=[]
# for square in  range(1,33):
#     squares=square**2
#     list.append(squares) 
#     cube=square**3
#     my_list.append(cube)
# print(list)
# print(my_list)

# mark=[]
# mark1=[]
# for x in range(1,22):
#     v=x**2
#     mark.append(v)
#     z=x**3
#     mark1.append(z)
# print(mark)
# print(mark1)

# fruit=('apple','orange','mange','banana')
# my_fruit=fruit
# print(fruit)
# print(my_fruit)
# print(my_fruit[1:3])



# temperatures = [32, 33.5, 30, 31.5, 34, 35]

# total_temperature = sum(temperatures)
# average = total_temperature / len(temperatures)

# print( average)


# scores = [32, 54, 67.5, 29, 35, 80, 95, 44.5, 100, 65]
# max_scores=sum(scores)
# average=max_scores/len(scores)
# print(max_scores)
# print(average)

# names = ["Allen", "Baker", "Charlie", "Dennis", "Elmo", "Fido", "Gabriel"]
# for name in names:
#     if len(name)>4:
#         print(name)
#     else:
#         print('not is name',name)
# print(len(name))

# scores = [32, 54, 67.5, 29, 35, 80, 95, 44.5, 100, 65]
# scores[3]=44
# # mark=scores[3]
# # print(type (mark))
# print(scores)



# temperature = int(input("Please enter a temperature: "))
# if temperature < 0:
#     print("Its freezing.")
# elif temperature < 15:
#     print("Its cold.")
# elif temperature < 26:
#     print("Its warm.")
# else:
#     print("Invalid.")

# temp=int(input("plese enter temp"))
# if temp < 0 :
#    print(f"it fereezing")
# elif temp < 15 :
#    print(f"it is a cold")
# elif temp < 45:
#    print(f"it is warm")
# else:
#    print(f"it is a invaled")


# numbers_list1 = [10, 21, 32, 43, 54, 66, 99]
# for number in numbers_list1:
#     if number%2 == 0:
#         print(number)

# list=[3,5,2,5,32,53,35,23,65,]
# for num in list:
#     if num%2==0:
#         print(num)


# numbers_list2 = [15, 22, 84, 13, 99, 56, 73]
# max_number = numbers_list2[0]
# min_number = numbers_list2[0]
# for number in numbers_list2:
#     if number > max_number:
#         max_number = number
#     if number < min_number:
#         min_number = number
# print(f"Maximum number in the list {max_number} and minimum number is {min_number}.")

# list=(36,44,22,11,55,33,66,88,99,)
# max_n=list[0]
# min_n=list[0]
# for num in list:
#     if num>max_n:
#         max_n=num
#         if num < min_n:
#             min_n=num
# print(max_n)
# print(min_n)


# aliens=[]
# for number in range(1,9):
#     new_alien={'name':'adil','age':33,'city':'lahore'} 
#     aliens.append(new_alien)
# print(aliens)


# alien1=[]
# for alien in range (1,9):
#     aliens={'color':'yellow','points':8,'spead':'slow',}
#     alien1.append(aliens)
# print(alien1)

# for alien in alien1[:3]:
#     if alien['color']=='yellow':
#      alien['color']='green'
# alien['points']=9,
# alien[' spead']='mediun'
# print(alien)

# users={
# 'students':
# {'first':'urdu',
# 'location':'english',
# 'last':'math'
# },
# 'car':
# {'first':'kamran',
# 'location':'lahore',
# 'last':'khan'
# }
# }

# # for k , v in users.items():
# #     print(k)
# #     print(v)
# for name ,languages in users.items():
#     print(f"it is a users name ",name)
#     full_name=f"{languages     ['first']}    {languages['last']}"
#     location=f"  {languages     ['location']}"
#     print(f"\n    language      {full_name.upper()}")
#     print(f"\n     location     {location.title()}")




# surah_info = [
#     {"number": 1, "name_english": "Al-Fatiha", "name_urdu": "الفاتحہ", "number_of_verses": 7},
#     {"number": 2, "name_english": "Al-Baqara", "name_urdu": "البقرہ", "number_of_verses": 286},
#     {"number": 3, "name_english": "Aal-E-Imran", "name_urdu": "آل عمران", "number_of_verses": 200},
#     {"number": 4, "name_english": "An-Nisa", "name_urdu": "النساء", "number_of_verses": 176},
#     {"number": 5, "name_english": "Al-Ma'idah", "name_urdu": "المائدہ", "number_of_verses": 120},
#     {"number": 6, "name_english": "Al-An'am", "name_urdu": "الانعام", "number_of_verses": 165},
#     {"number": 7, "name_english": "Al-A'raf", "name_urdu": "الاعراف", "number_of_verses": 206},
#     {"number": 8, "name_english": "Al-Anfal", "name_urdu": "الانفال", "number_of_verses": 75},
#     {"number": 9, "name_english": "At-Tawbah", "name_urdu": "التوبہ", "number_of_verses": 129},
#     {"number": 10, "name_english": "Yunus", "name_urdu": "یونس", "number_of_verses": 109},]

# for k  in surah_info[1:5]:
#     print(k)


#     if surah ['number_of_verses']>20:
#         print(f" {surah['number']}  {surah['name_english']} {surah['number_of_verses']}")


# first_name=surah_info[0]
# print(first_name['number'])
# print(first_name['name_english'])
# print(first_name['name_urdu'])
# print(first_name['number_of_verses'])

# for name  in surah_info[5:9]:
# #     print(name)
#    print(name['name_english'])

# for surah in surah_info:
#     print(surah['name_english'])
#     print(surah['name_urdu'])
#     print(surah['number_of_verses'])

# numbers = [66,77,40,35,20]
# details = []

# for x in numbers:
#     if x % 2 == 0:
#         print(f"{x} is an even number")
#         details.append(f"{x} is an even number")
#     else:
#         print(f"{x} is an odd number")
#         details.append(f"{x} is an odd number")

# numbers=[11,22,33,44,55,66,77,88,99,100]
# list=[]
# for x in numbers:
#     if x %2==0:
#         print(f"even number is {x}")
#         list.append(x)
#     else:
#         print(f"odd number{x}")
#         list.append(x)

# list=[33,55,44,22,55,66,77,88,]
# array=[]
# for y in list:
#     if y %3==0:
#         print(y)
#         array.append(y)
#     else:
#         print(y)
#         array.append


# list=[33,55,44,22,55,66,77,88,]
# array=[]
# for y in list:
#     array.append(y)
# print(array)

# list=[33,55,44,22,55,66,77,88,]
# sum=0
# for z in list:
#     if z %2==0:
#        sum=sum+z
# print(list)
# print(sum)

# list=[33,55,44,22,55,66,88,]
# odd_n=[]
# even_n=[]
# for v in list:
#     if v %2==0:
#       even_n.append(v)
# else:
#     odd_n.append(v)

# print(f'even number{(even_n)}')
# print(f'odd number{(odd_n)}')




# numbers = [18,7,12,4,65,88,99,43]
# even=[]
# odd =[]

# for number in numbers:
#     if number%2==0:
#         even.append(number)
#     else:
#         odd.append(number)

# print(f"total number of even numbers: {len(even)}")
# print(f"total number of odd numbers: {len(odd)}")


# list = [18,7,12,4,65,88,99,3]
# odd = 0 
# even = 0
# for item in list:
#     if item % 2 == 0:
#         even = even + 1
#     else:
#         odd += 1

# print(f'odd numbers is {odd} in the list.')
# print(f'even numbers is {even} in the list.')

# list = [18,7,12,4,65,88,99,3]
# even=0
# odd=0
# for num in list:
#     if num%2==0:
#         even=num+1
#     else:
#         odd=num+1
# print(f'even nunber{even}')
# print(f'odd number{odd}')

# list = [18,7,12,4,65,88,99,3]
# count1=0
# count2=0
# sum1=0
# sum2=0
# for x in list:
#     if x %2==0:
#         count1=count1+1
#         sum1=sum1+x
#     else:
#         count2=count2+1
#         sum2=sum2+x
# print(count1)
# print(count2)
# print(sum1)
# print(sum2)


#numbers=[18,7,12,4,65,88,99]
# even_count=0
# for x in numbers:
#     even=x%2==0
#     even_count+=even
# print(f"{even_count} numbers is evevn")
# even_count=0
# for x in numbers:
#     even=x%2==0
#     even_count+=even
# print(f"{even_count} numbers is evevn")



# numbers=[18,7,12,4,65,88,99]
# even=0
# for  y in numbers:
#     if y %2==0:
#        even=even+y
#     print(even)


# arry = [18,7,12,4,65,88,99,4]
# odd = []
# even =[]
# list1 = 0
# list2 = 0
# num1 =0
# num2 =0
# for arr in arry:
    
#     if arr%2 == 0:
#         x=odd.append(arr)
#         list1 += 1
#         num1 =num1 +arr
#         evg1 = num1/list1
#     else: 
#         arr % 2 != 0
#         y = even.append(arr)
#         list2 += 1
#         num2 = num2 + arr
#         evg2 = num2/list2
# print(num1)
# print(num2)
# print(evg1)
# print(evg2)
# print(list1)
# print(list2)



# list=[11,33,22,44,66,55,66,88,77,88,99]
# even=[]
# odd=[]
# even_count=0
# odd_count=0
# sum1=0
# sum2=0
# for y in list:
#     if y %2==0:
#         even=y
#         even_count=even_count+1
#         sum1=sum1+y
#         everage=sum1/even_count
#     else:
#         odd=y
#         odd_count=odd_count+1
#         sum2=sum2+y
#         everage=sum2/odd_count
#     print("even",even)
#     print(odd,"odd")
# print(even_count)
# print(odd_count)
# print(sum1)
# print(sum2)
# print(everage)
# print(everage)