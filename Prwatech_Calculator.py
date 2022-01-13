# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:16:57 2022

@author: ASUS
"""

Name - Mayur Suresh Rathod
mail id - mayurrathod1124@gmail.com
## Calculator
 
def addition():
    n=int(input("How many numbers you want to add: "))
    a=[]
    for i in range(1,n+1):
        i=int(input("Enter your number: "))
        a.append(i)
    sum=0
    for x in range(0,len(a)):
        sum=sum+a[x]
    print("\nThe Sum of Number is {}".format(sum))

def subtraction():
    n=int(input("How many numbers you want to subtract: "))
    a=[]
    for i in range(1,n+1):
        i=int(input("Enter your number: "))
        a.append(i)
    b=0
    sub=0
    for x in range(0,len(a)):
        b=a[x]-b
        sub=-b
    print("\nThe Sum of Number is {}".format(sub))

def multiplication():
    n=int(input("How many numbers you want to multiply: "))
    a=[]
    for i in range(1,n+1):
        i=int(input("Enter your number: "))
        a.append(i)
    b=1
    for x in range(0,len(a)):
        b=a[x]*b
    print("\nThe Sum of Number is {}".format(b))

def division():
    a=int(input("Enter Numerator: "))
    b=int(input("Enter Dinominator: "))
    div= a/b
    print("\nThe Sum of Number is {}".format(div))

def AND():
    a=int(input("Enter the first value: "))
    b=int(input("Enter the second value: "))
    AND= a&b
    print('The value of AND operator is',AND)


def OR():
    a=int(input("Enter the first value: "))
    b=int(input("Enter the second value: "))
    OR= a|b
    print('The value of AND operator is',OR)


def NOR():
    a=int(input("Enter the first value: "))
    b=int(input("Enter the second value: "))
    NOR= a^b
    print('The value of AND operator is',NOR)

def factorial():
    n=int(input("Enter the number: "))
    m=1 
    for i in range(1,n+1):
        if i!=n+1:
            m=i*m     
    print(f"The Factorial of {n} is {m}")

def fabonacci():
    n=int(input("Enter the number: "))
    a=0
    b=1
    z=[0,1,]
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        z.append(b)
    print(f"The Fabonacci of {n} is {z}")

def permutation():
    n=int(input("Enter Total number of items in sample: "))
    r=int(input("Enter number item selected from sample: "))
    m=1 
    for i in range(1,n+1):
        if i!=n+1:
            m=i*m
    a=n-r
    b=1
    for x in range(1,a+1):
        if x != a+1:
            b=x*b
    p=m/b
    print("The total numbers of ways are",int(p))

def reverse():
    n=int(input("Enter the number: "))
    rev=0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    print("The reverse of given integer is", rev)

def combination():
    n=int(input("Enter Total number of items in sample: "))
    r=int(input("Enter number item selected from sample: "))
    m=1 
    for i in range(1,n+1):
        if i!=n+1:
            m=i*m
    a=n-r
    b=1
    for x in range(1,a+1):
        if x != a+1:
            b=x*b
    c=1
    for z in range(1,r+1):
        if z!=r+1:
            c=z*c
    p=m/(c*b)
    print("The total numbers of combinations are",int(p))

def mean_median_mode():
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele) # adding the element
    sum=0
    n = len(lst)
    for x in range(0,len(lst)):
        sum=sum+lst[x]
    mean = sum / n
    print("Mean is: " + str(mean))
    #Median
    lst.sort()
    if n % 2 == 0:
        median1 = lst[n//2]
        median2 = lst[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = lst[n//2]
        print("Median is: " + str(median))
    #Mode
    from collections import Counter
    data = Counter(lst)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    print("Mode is: "+ str(get_mode))

def variance():
    dict_list = dict() 
    n = int(input("Enter number of elements : "))    
    for i in range(0, n):
        data = input('Enter name & score separated by ":" ') 
        temp = data.split(':') 
        dict_list[temp[0]] = int(temp[1]) 
        for key, value in dict_list.items(): 
            #print('Name: {}, Score: {}'.format(key, value))
            dict_list.update()
    print("\nDictionary is:", dict_list)
    lst = []
    sum=0
    v=0
    for value in dict_list.values():
        lst.append(value)
    for x in range(0,len(lst)):
        sum=sum+lst[x]
    mean = sum / len(lst)
    for z in range(0,len(lst)):
        v=v + ((lst[z]-mean)**2)
        #v = v + ([((lst[z] - mean) ** 2)]) 
    variance = v / len(lst)
    std = variance ** 0.5
    print("The Variance is: ",variance)
    print("The Standard Deviation is: ",std)

choice = 0

while choice != 16:
    print("\n---------------------Menu---------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. AND Operation")
    print("6. OR Operation")
    print("7. NOR Operation")
    print("8. Factorial ")
    print("9. Fibonacci")
    print("10. Permutation")
    print("11. Integer reverse")
    print("12. Combination")
    print("13. Mean, Mode and Median")
    print("14. Dictionary, variance and standard deviation")
    print("15. Exit")

    choice = int(input("\nEnter Your Choice: "))
    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        AND()
    elif choice == 6:
        OR()
    elif choice == 7:
        NOR()
    elif choice == 8:
        factorial()
    elif choice == 9:
        fabonacci()
    elif choice == 10:
        permutation()
    elif choice == 11:
        reverse()
    elif choice == 12:
        combination()
    elif choice == 13:
        mean_median_mode()
    elif choice == 14:
        variance()
    elif choice == 15:
        break
    else:
        print("Please Select An Option From the Menu!")
