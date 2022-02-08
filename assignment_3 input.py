#question_1
str_1=input("Please enter the string:\n")
list=str_1.split()
dict={}
if len(list)==1:
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)

#question_2
while True:
    day = int(input("Please enter the day:\n"))
    month = int(input("Please enter the month:\n"))
    year = int(input("Please enter the year:\n"))
    if 1<=day<=31 and 1<=month<=12 and 1800<=year<=2025:
        break
    else:
          print("Invalid date")
if month==(1 or 3 or 5 or 7 or 8 or 10):
    if day==31:
        day=1
        month=month+1
        print(day,month,year,sep="/")
    else:
        day+=1
        print(day, month, year, sep="/")

elif month==(4 or 6 or 9 or 11):
    if(day==30):
        day=1
        month=month+1
        print(day, month, year, sep="/")
    elif(day<30):
        day+=1
        print(day, month, year, sep="/")
    else:
        print("Please enter a valid date")#if day is 31
elif month==2:
    if (year%4==0):
        if(day==29):
            day=1
            month+=1
            print(day, month, year, sep="/")
        elif(day<29):
            day+=1
            print(day, month, year, sep="/")
        else:
            print("please enter a valid date")
    else:
        if(day==28):
            day=1
            month+=1
            print(day, month, year, sep="/")
        elif(day<28):
            day+=1
            print(day, month, year, sep="/")
        else:
            print("Please enter a valid date")
elif(month==12):
    if(day==31):
        day=1
        month=1
        year+=1
        print(day, month, year, sep="/")
    else:
        day+=1
        print(day, month, year, sep="/")

# question 3
list_1 = list(int(num) for num in input("Enter the numbers you want to square while leaving space after every number:\n").strip().split())
print("input list is:", list_1)
list_2 = [(base, pow(base, 2)) for base in list_1]
print("Required output is:\n", list_2)

#Question_4
grade=int(input("Please enter your grade between 4 and 10:\n"))
if grade==10:
    print("Your grade is \'A+\' and Outstanding performance")
elif grade==9:
    print("Your grade is \'A\' and Excellent performance")
elif grade==8:
    print("Your grade is \'B+\' and Very good performance")
elif grade==7:
    print("Your grade is \'B\' and Good performance")
elif grade==6:
    print("Your grade is \'C+\' and Average performance")
elif grade==5:
    print("Your grade is \'C\' and Below average performance")
elif grade==4:
    print("Your grade is \'D\' and Poor performance")
else:
    print("ERROR")

#Question_5
num=6
for i in range(num):
    for j in range(i):#for printing blank spaces in the begining of every line
        print(' ', end='')
    for j in range(2*(num-i)-1):
            print(chr(65+j),end='')#using ASCII values for printing Alphabets
    print()

# question_6
student_details = {}
while True:
    name = input("Please enter student's name and for stopping enter N:\n")
    if name == 'N':
        break
    SID = int(input("Please enter student's SID and for stopping enter N:\n"))
    if SID == 'N':
        break
    student_details[SID] = name  # Storing SID's in keys and names in values
# question 6 part a
print("Part A :", student_details)
# question 6 part b
sorted_by_name={k:v for k,v in sorted(student_details.items(),key=lambda v:v[1])}
print("Part B :", sorted_by_name)
# question 6 part c
sorted_by_SID={k:v for k,v in sorted(student_details.items())}
print("Part C :",sorted_by_SID)
# question 6 part d
ssid=int(input("Please enter SID of the student you want to search for:\n"))
print("Part D :", student_details[ssid])

# question_7
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)


num = int(input("Enter the number of terms in the series:\n"))
if num <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence: ")
    sum = 0
    for i in range(num):
        print(recur_fibo(i))
        sum = sum + recur_fibo(i)
average = float(sum/num)
print("Average of resultant fibonacci series is", average)

# question 8
set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 4, 6, 8}
set_3 = {1, 5, 9, 13, 17}
# question 8 part A
union_set_1_2 = set_1.union(set_2)  # taking union of set 1 and 2
intersection_set_1_2 = set_1.intersection(set_2)  # taking intersection of set 1 and 2
set_4 = union_set_1_2-intersection_set_1_2   # storing elements of 1 and 2 which are not common in both in set_4
print("Part A :", set_4)
# question 8 part B
set_5 = set_1.union(set_2.union(set_3))-set_1.intersection(set_2)-set_1.intersection(set_3)-set_2.intersection(set_3)
print("Part B: ", set_5)
# question 8 part C
set_6 = set_1.intersection(set_2).union(set_1.intersection(set_3)).union(set_3.intersection(set_2))-set_1.intersection(set_2.intersection(set_3))
print("Part C :", set_6)
# question 8 part D
set_7 = set()
for i in range(1, 11):
    if i not in set_1:
        set_7.add(i)
print("Part D :", set_7)
# question 8 part E
set_8 = set()
for i in range(1, 11):
    set_8.add(i)  # making a set of elements from 1 to 10
set_9 = set_8-set_1-set_2-set_3  # removing elements which are present in set_1,set_2 and set_3
print("Part E :", set_9)
