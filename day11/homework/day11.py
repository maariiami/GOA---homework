#Timer: დაწერეთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე, დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა".

i = 10
while i>=1:
    print(i)
    i = i - 1

print("time is up")



#პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ, რომ სწორი პაროლი არის "12345678".

password = int(input("please enter password: "))
while password != 12345678:
    password = int(input("please enter password: "))


#ლუწი რიცხვები: დაწერეთ პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე while ციკლის გამოყენებით.

i = 0
while i<= 20:
    print(i)
    i = i + 2


#შეამოწმეთ ლუწია თუ კენტი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს და ბეჭდავს ლუწია თუ კენტი.

num = int(input("please enter number: "))
if num % 2 == 0:
    print("num is even")
if num % 2 != 0:
    print("num is odd")






#რიცხვების შედარება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ.

num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))
print(num1 < num2)
print(num1 > num2)
print(num1 == num2)





#რიცხვის გამოცნობა: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად.

num = 2
num = int(input("enter number: "))
while num != 2:
    num = int(input("enter number: "))




#რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან.
number = int(input("please enter number: "))

while number % 2 != 0:
    number = int(input("Please enter number: "))




#რიცხვების კლასიფიკაცია: შექმენით პროგრამა, სადაც 50-იდან 100-ის ჩათვლით გამოიტანთ კენტ რიცხვებს. ციკლის გარეთ შექმენით ჯამის ცვლადი, სადაც დაემატება ციკლის ის რიცხვები, რომლებიც მეტია 75-ზე. ბოლოს დაპრინტეთ ამ ცვლადის მნიშვნელობა
    
for i in range(50, 100 + 1):
    if i % 2 != 0:
        print(i)
    if i > 75:
        sum = sum + i
print(sum)




#რიცხვების შედარება: მომხმარებელს შეეკითხეთ რიცხვი. სანამ ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე, დაპრინტეთ ის და მასზე მოახდინეთ იტერაცია 1-ით.


number = int(input("Please enter number: "))

number_after_addition = number + 20

while number < number_after_addition:
    print(number)
    number = number + 1





#სახელის გამოცნობა. შექმენით ცვლადი სადაც იქნება შენახული თქვენი სახელი. მომხმარებელს შეეკითხეთ სახელი და სანამ თქვენსას არ შემოიტანს თავიდან შეეკითხეთ. 

name = "mari"
name = input("what is your name? ")
while name != "mari":
    name = input("what is your name? ")


    




    


    



