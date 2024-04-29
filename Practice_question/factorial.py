#how to calculate factorial of a number
#-------------------------using a recursion function------------------------------------------#


def factorial(number):
    if(number==0):
        return 1
    else:return number * factorial(number-1)

   


output=factorial(2)
print(output)

#-----------------------------------without recursion function----------------------------------#


def factorial(number):
    result =1
    if number == 0: return 1
    else:
        for i in range(1,number+1):
            result*=i
        return result


output=factorial(5)
print(output)



#------------------------------- using while loop-------------------------------------#

number = int(input("enter number of your choice: "))


factorial=1

while number>0:
    factorial  *= number
    number-=1
print(factorial)

