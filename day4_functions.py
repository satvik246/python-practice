def greet():
    print("Hello")
    print("have a good day")

greet()

#Functions with Parameters
#parameter is what we define during function definition and argument is what we pass at run time or invoking function
def greet(first_name,last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome Abroad")

greet('Satvik','Kunala')

#with return keyword
#optional parameters must be placed after required parameters
#we can secify argumetns with = sign
def greet(name):
    return f"Hello {name}"

first_name=greet('Satvik')
print(first_name)

# * args (variable number arguments) works as a tuple
def multiply(*numbers) :
    total = 1
    for number in numbers :
        total*=number
    return total

print(multiply(1,2,3,4)) 

# using ** (works as a dictionary)

def save_user(**user):
    print(user["name"])

save_user(id=1,name="satvik",age=24)

#fizzbuzz exercise.if a number is divisible by 3 return Fizz , if it's divisible by 5 return Buzz if its divisible by both return fizzbuzz else return same number
def fizz_buzz(in_number):
    if int(in_number)%3 ==0 and int(in_number)%5 ==0 :
        ans_var = 'FizzBuzz'
    elif int(in_number)%5 ==0 :
        ans_var = 'Buzz'
    elif int(in_number)%3 ==0 :
        ans_var = 'Fizz'
    else :
        ans_var = in_number
    
    return ans_var

print(fizz_buzz(16))
        

x = 10

def change():
    x = 50
    print(x)

change()
print(x)


def product_summary(name, price, quantity, discount=0):
    tot_discount = quantity * (discount*price)/100
    tot_amount = (price*quantity) - tot_discount
    print('Product : ' + name)
    print ('Price : ' + str(price))
    print ('Quantity : ' + str(quantity))
    print('Discount : ' + str(discount) + '%' )
    print ('Total : ' + str(tot_amount)) 

product_summary("Laptop", 80000, 2, 10)