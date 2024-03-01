



# import random

# questions = [
#     {
#         'question': 'What is the capital of Armenia?',
#         'options': ["New York", "Yerevan", "Paris", "Tbilisi"],
#         'correct_answer': "Yerevan",
#     },
#     {
#         'question': 'Who won the Ballon d\'Or in 2023?',
#         'options': ["Camavinga", "Ronaldo Cr", "Mbappe", "Messi"],
#         'correct_answer': "Messi",
#     },
#     {
#         'question': 'Who was the president of the USA in 2005?',
#         'options': ["Abraham Lincoln", "Barack Obama", "George Bush", "Donald Trump"],
#         'correct_answer': "George Bush",
#     },
#     {
#         'question': 'In which country is Angel Falls located?',
#         'options': ["Brazil", "Venezuela", "Argentina", "Uruguay"],
#         'correct_answer': "Venezuela",
#     },
#     {
#         'question': 'Who was the founder of Apple?',
#         'options': ["Steve Jobs", "Martin Oberin", "Robert Down Jr", "Elon Musk"],
#         'correct_answer': "Steve Jobs",
#     },
#     {
#         'question': 'What is the largest ocean in the world?',
#         'options': ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"],
#         'correct_answer': "Pacific Ocean",
#     },
# # ]

# print("Welcome to the game")

# money = 0
# for _ in range(8):
#     current_question = random.choice(questions)
#     print(current_question["question"])
#     for i, option in enumerate(current_question['options'], 1):
#         print(f"{i}. {option}")
    
#     user_answer = input("Choose an answer (1-4): ")

#     if current_question['options'][int(user_answer) - 1] == current_question['correct_answer']:
#         money += 10
#         print("That's right! You earned 10 money.\n")
#     else:
#         print("Game over.")
#         break

# print(f"You earned {money} money!")



# myls = [1,2,3,[4,5,6],7,8,9,[10,11,12],13,14]
# myls2 = []
# for sublist in myls:
#     if type(sublist) == list:
#         myls2.extend(sublist)
#     else:
#         myls2.append(sublist)
# print(myls2)

# rappers = {"guf":"guf1",
#         "basta": "basta1",
#         "obla":  "obla1",
#         "pharaoh": "pharaoh1",}

# BINARNI POISK
# ml = [1,2,5,7,15,16]
# item = 2
# flag = False
# low = 0
# high = len(ml) -1
# while low <= high:
#     mid = (high+low)// 2
#     guess = ml[mid]
#     if guess == item:
#         flag = True
#         print(mid)
#         break
#     if item > guess:
#         low = mid+1
#     else:
#         high = mid -1
# if not flag:
#     print("null")

    

# num = [1,2,3,4,5,6,10,16,17,18]
# item = 3
# flag = False
# low = 0
# high = len(num) - 1

# while low <= high:
#     mid = (high + low) // 2 
#     guess = num[mid]

#     if guess == item:
#         flag = True
#         print(mid)
#         break
#     if item > guess:
#         low = mid + 1
    
#     else:
#         high = mid - 1
# if not flag:
#     print("null")





# def binary_Serach(list,item):
#     low = 0
#     high = len(list) -1

#     while low <= high:

#         mid = (low+high)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid -1 
#         else:
#             low = mid +1
#     return None
# my_list  = [1,2,3,5,7,8,9]

# print (binary_Serach(my_list,-1))

# def binarySearch(list,item):
#     low = 0 
#     high = len(list) -1 
    
#     while low <= high:
#         mid  = (low+high)// 2
#         guess = list[mid]

#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1 

#     return None
# myls = [1,2,3,5,7,9]
# print(binarySearch(myls,3))



# N = input()

# even_sum = 0
# odd_sum = 0
# for i in range(len(N)):
#     if i % 2 == 0:
#         even_sum += int(N[i])
#     else:
#         odd_sum += int(N[i])

# if (even_sum - odd_sum) % 11 == 0:
#     print("YES")
# else:
#     print("NO")



# SORTAVOREL 
# arr = list(map(int,input().split()))
# flag = True
# for i in range(1,len(arr)):
#     if arr[i] < arr[i -1]:
#         flag = False
#         break
        
# print(flag)     
 

#SORTAVORUM 
# n = input()
# list_number = list(map(int, input().split()))
# numbers = []

# for i in range(-100, 101):
#     for a in list_number:
#         if i == a:
#             numbers.append(i)
# print(*numbers)



#TVI FACTORIALY
# def factorial(n):
#     if  n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# num = 3
# print(num,factorial(num))


# def bubble_sorting(strings):
#     n = len(strings)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if len(strings[j]) < len(strings[j+1]):
#                 strings[j], strings[j+1] = strings[j+1], strings[j]


# strings = ["banana","kiwi","orange","penaple","watermelon"]

# bubble_sorting(strings)
# for string in strings:
#     print(string)

# def bubble_sort(strings):
#         n = len(strings)
#         for i in range(n):
#             for j in range(0,n-i-1):
#                 if len(strings[j]) < len(strings[j+1]):
#                     strings[j], strings[j+1] = strings[j+1],strings[j]
#         return strings


# string = ["lemon","apple","pomegranate","kiwi"]




# n = int(input())
# ls = list(map(int,input().split()))
# count = 0
# for i in range(n):
#     for j in range(len(ls) -1 -i ):
#         if ls[j] > ls[j+1]:
#             ls[j], ls[j+1] = ls[j+1],ls[j]
#             count += 1
# print(*ls)
# print(count)
        




# n = int(input())
# ls = list(map(int,input().split()))


# for i in range(n):
#     for j in range(len(ls) - 1):
#         if ls[j] > ls[j+1]:
#             ls[j], ls[j+1] = ls[j+1],ls[j]
            

# print(*ls)





# n = [-2, 8, 1, 2, 4, 3, 6, 8, 7]
# a = len(n)

# for i in range(1, a):
#     for j in range(i, 0, -1):
#         if n[j] < n[j - 1]:
#             n[j], n[j - 1] = n[j - 1], n[j]
#         else:
#             break

# print(n)









# print(bubble_sort(string),'--------------')

# print(string)

# usersAkaNames = [
#      {
#         "aka_name":'Tiko',
#          "id": 7
#     },
#      {
#          "aka_name":'Lyut',
#          "id": 33
#     },
#      {
#          "aka_name":'Ando',
#          "id": 1
#     },
#      {
#          "aka_name":'Arm',
#          "id": 2
#     },
#      {
#          "aka_name":'Mat',
#          "id": 10
#     },
# ]

# usersName = [
#      {
#          "name":'Lyudvig',
#          "id":33
#     },
#      {
#          "name":'Andranik',
#          "id":1
#     },
#      {
#          "name":'Matevos',
#          "id":10
#     },
#      {
#          "name":'Arman',
#          "id":2
#     },
#       {
#         "name":'Tigran',
#          "id":7
#     },
# ]

# ziped = zip([1,2,3,4],['a','1','sd','d'])

# print(list(ziped))

#mergedUsers = []


# for i in usersAkaNames:

#     for j in usersName:
#         if i["id"] == j["id"]:

#             foundUser = {
#                     "id": i["id"],
#                     "name": j["name"],
#                     "aka_name": i["aka_name"],
#                 }

#             mergedUsers.append(foundUser)
#             break

# print(mergedUsers)



# for i in usersAkaNames:

#     for j in usersName:
#         if i["id"] == j["id"]:
#             i['name'] = j['name']
#             break


# print(usersAkaNames)



# for i in diArr:
#     print(f"hello my name is {i['name']} I am {i['id']} yo")

# # a = int(input())
# # b = int(input())

# # while b > 0:
# #     c = a % b
# #     a = b
# #     b = c
    
# # print(a,b)




# def msum(*args):
#     tmp = 0
#     for el in args:
#         tmp += el
#     return tmp
# print(msum(1,2,3))
# print(msum())
# print(msum(1,10,40))


# def function():
#     ml = ["hello",'good',"my","world"]


#     a = list(filter(lambda x : len(x) > 4,ml))
#     return a
# print(function())




# def even_max(*args):
#     if len(args) == 0:
#         return None
    
#     mmax = args[0]
#     for i in args:
#         if i % 2 == 0 and i > mmax:
#             mmax = i
#     if mmax == args[0]
#     return



# def ge_indexes(ml,target):
#     for i in range(len(ml)):
#         for  j in range(len(ml)):
#             if ml[i] + ml[j] == target:
#                 return i,j
# print(ge_indexes([1,2,7,11,15], 9))

    
    
    
# def my_targ(myls,target):
#     for i in range(len(myls)):
#         for j in range(len(myls)):
#             if myls[i] + myls[j] == target:
#                 return i,j
# print(my_targ([1,9,5,6,76,14],11))




# HASHVEL TVERI GUMARY
# def my_int(*args):
#     total = 0
#     for i in args:
#         if isinstance(i, int):
#             total += i
#     return total
    
# result = my_int(1, 2, 45, "hello", "good")
# print(result)






# TOXERI QANAKY
# def my_str(*args):
#     total = 0
#     for i in args:

#         if isinstance(i,str):
#             total += 1
#     return total
# result = my_str(1,2,"helo","good")
# print(result)
        

#MIJIN TIVY
# def average_func(*args):
    
#     summ = 0
#     nums = 0

#     for i in args:
#         if isinstance(i, (int, float)):
#             summ += i
#             nums += 1
        
#     if nums == 0:
#         return 0
#     else:
#         average = summ / nums
#         return average


# result = average_func(1, 2, 3, "4", "5", 6, "hello")
# print(result) 

#MIJIN TVABANAKANY
# def find_average(*args):
#     summ = 0
#     nums = 0
#     for i in args:
#         if isinstance(i,(int,float)):
#             summ += i
#             nums += 1
#     if nums == 0:
#         return 0
#     else:
#         average = summ/nums
#         return average
# result = find_average(1,2,3,"hello")
# print(result)

# num = [10,20,30,40,50]
# def find_average(numbers):
#     average_1 = sum(numbers)/len(numbers)
#     return average_1
# average_1 = find_average(num)
# print(average_1)


# def math(num1,num2):
    

#     return num1 * num2

# print(math(3,5))
   


# def lo_case(mystr):
#     low = ""

#     for i in mystr:
#         chrCode = ord(i)
#         if chrCode > 64 and chrCode < 89:
#             low += chr(chrCode + 32)
#         else:
#             low += i 
    
#     return low

# print(lo_case('Inch Or BBBaaA4'))

        

# lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# def up_case(mystr):
#     upp = ""

#     for i in mystr:
#         if  i in lowercase:
#              upp += uppercase[lowercase.index(i)]
#         else:
#             upp += i 
    
#     return upp



# print(up_case('AAb'))



#ARAJI TARY DARCVAC MECATAR
# def makeUpperFirst(mystr):
#     newStr = ''


#     for i in range(len(mystr)):
#         chrCode = ord(mystr[i])

#         if  (chrCode > 96 and chrCode < 123) and (mystr[i-1] == ' ' or i == 0): 
#             newStr += chr(ord(mystr[i]) - 32) 
#         else:
#             newStr += mystr[i]
    
#     return newStr

# print(makeUpperFirst('hello my name is Ara'))



#BARY HAKARAK
# def revers_str(mystr):
#     res = ""
#     for i in range(len(mystr)-1,-1,-1):
#         res += mystr[i]
#     return res
# print(revers_str("hello"))
    
# def rev_str(mstr):
#     rev = ""
#     for i in range(len(mstr)-1,-1,-1):
#         rev += mstr[i]
#     return rev
# print(rev_str("hello"))





#AMENA ERKAR BARY
# def long_str(mstr):
#     wrd = mstr.split(' ')
#     long_wrd = ""
#     for i in wrd:
#       if len(i) > len(long_wrd):
#          long_wrd = i
#     return long_wrd
# print(long_str("hello my"))


    
# def most_letter(mystr):
#     leter_count = {}
#     for i in mystr:
#         if i.isalpha():
#             i = i.lower()
#             if i in leter_count:
#                 leter_count[i] += 1
#             else:
#                 leter_count[i] = 1


#     max_count = 0
#     most_letter = None
#     for letter, count in leter_count.items():
#         print(letter, count)
#         if count > max_count:
#             max_count = count
#             most_letter = letter
#     return most_letter
# print(most_letter(long_str("hello my good wooooooooorldlest")))



    

# my_tuple = (100,)
# print(my_tuple * 3)



# def get_cont(filename):
#     f = open(filename)
#     return f.readlines()


# def creat_user_dict(ml):
#     md = {}
#     for i in ml:
#         i = i.strip().split(": ")
#         md[i[0]] = i[1]
#     return md
# cnt = get_cont("a.txt")
# users = creat_user_dict(cnt)
# print(users)

# Open a file in write mode ('w')

with open('write.txt', 'w') as file:
    file.write("Hello, world!\n")


def read_file(wikifile):
    
    return open(wikifile).read()

    















# def let_count(mstr):
#     md = {}
#     for i in mstr:
#         if i.isalpha():
#             if i in md:
#                 md[i] += 1
#             else:
#                 md[i] = 1
#     return md 


# def count_words(mstr):
#     ml = mstr.split()
#     count = 0
#     for i in ml:
#         if i.isalpha():
#             count+= 1 
#     return count


# def sent_count(mstr):
#     print(mstr.split("."))
#     return len(mstr.split("."))


# cnt = read_file("a.txt")

# print(cnt)
# print(let_count(cnt))
# print(count_words(cnt))
# print(sent_count(cnt))



