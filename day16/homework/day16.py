#შექმენით სია სადაც შეინახავთ თქვენთვის საყვარელ ფილბეს და დაბეჭდეთ მთლიანი სია/ კონკრეტული ფილმი

films = ["Life of Pi", "cast Away", "The Impossible", "The terminal", "The way back"]
print(films)
print(films[2])

#შექმენით 2 სია და გააერთიანეთ ისინი

girls = ["mari", "nini", "ani", "nata", "masho"]
boys = ["tazo", "luks", "nika", "saba", "bacho"]
print(girls + boys)

#შექმენით სტრინგი მაგ. თქვენი სახელი, და გამოიტანეთ სახელის პირველი და ბოლო სიმბოლო

name = "mari"
print(name[0] + name[3])

#შექმენით სია და სტრინგი ხოლო შემდეგ დაბეჭდეთ len ფუნქციის გამოყენებით მათი ზომა

cars = ["BMW", "Mercedes", "Corvette", "ferrari"]
print(len(cars))

#შეცვალეთ სიიდან რომელიმე მნიშვნელობა

num = [1, 4, 6, 8, 10]
num[0] = 2
print(num)

#შექმენით რიცხვების სია სადაც 10 რიცხვს შეიტანთ, გამოიტანეთ პირელ ინდექსა და ბოლო ინდექსზე მყოფი ელემენტების ჯამი

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0] + numbers[9])
