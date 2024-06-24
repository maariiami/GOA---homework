#თქვენით მოიფიქრეთ for ციკლისთვის 10 მაგალითი, მაუშევარი ატვირთეთ github ზე

for num in range(5):
    print(num)

for num in range(10):
    print(num)


for i in range(5):
    print("hello")


for num in range(3):
    print("num")

for num in "hello":
    print(num)


for num in "mari":
    print(num)

for num in "goa":
    print(num)

for num in range(2):
    print(num)

for num in range(6):
    print(num)
    
for num in "apple":
    print(num)



#0-იდან 20-ის ჩათვლით დაპრინტეთ ყველა მთელი რიცხვი.
    
i = 0
while i <= 20:
    print(i)
    i = i + 1
 

 #50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით. ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი, რომელსაც ციკლში მიემატება საიტერაციო ცვლადის მნიშვნელობა. საბოლოოდ დაპტინტეთ sum ცვლადის მნიშვნელობა.

sum_variable = 0
for i in range(50,101):
    sum_variable = sum_variable + i
    print(sum_variable)


#-10-იდან 10-ის ჩათვლით დაატრიალეთ for ციკლი და იტერაცია მოახდინეთ 3-ით (გაიხსენეთ step), დაპრინტეთ საიტერაციო ცვლადის მნიშვნელობა ყოველ ციკლის დატრიალებაზე.
    

for i in range(-10,11,3):
    print(i)

    




