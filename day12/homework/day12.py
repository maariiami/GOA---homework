#დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი.

num = int(input("please enter number: "))
if num > 0 :
    print("number is positive")
if num < 0 :
    print("number is negative")
if num == 0 :
    print("number is 0")


#დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision".
    
print("1. km - miles")
print("2. miles - km")

choice = int(input("please enter operation number (1 or 2): "))
number = float(input("please enter number to convert it: "))

if choice == 1: 
    print(number / 1.6)
elif choice == 2:
    print(number * 1.6)    
else:
    print("wrong decision")


#შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი, საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია.
    
name = input("enter your name: ")
lastname = input("enter your lastname: ")
age = input("enter your age: ")
mail = input("enter your mail: ")

print("your name is" ,name, "your lastname is" ,lastname, "you're" ,age, "your mail is" ,mail,)


#მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

result = (num1 + num2 + num3) / 3

print(result)




    










