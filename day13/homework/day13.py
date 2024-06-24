#დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
#If the age is less than 18, print "You are a minor."
#If the age is between 18 and 65, print "You are an adult."
#If the age is 65 or older, print "You are a senior citizen."





age = int(input("enter your age: "))
if age < 18:
    print("you are a minor")
elif age >= 18 and age < 65:
    print("you are an adult")
else:  
    age > 65
    print("you are a senior citizen")




#შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.


for i in range(5):
    number = int(input("Please enter number: "))

    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is odd")



#დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
#If the grade is A, print "Excellent!"
#If the grade is B, print "Good job!"
#If the grade is C, print "You passed."
#If the grade is D, print "You can do better."
#If the grade is F, print "You failed."
    


grade = (input("please enter your grade - A, B, C, D, F :  "))
if grade == "A":
    print("excellent!")
elif grade == "B":
    print("good job!")
elif grade == "C":
    print("you passed")
elif grade == "D":
    print("you can do better")
else:
    grade == "F"
    print("you failed")



#დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით

i = 1
while i < 10:
    print(i)
    i = i + 1




# შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს


num = int(input("guess the number (1 - 10) : "))
while num != 5:
    num = int(input("guess the number (1 - 10) : "))
if num == 5:
    print("yoy won!")

#დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით.

for i in range (5, 50 +1 , 5 ):
    print(i)


#შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით.
    
for i in range(10,1,-1):
    print(i)

    


