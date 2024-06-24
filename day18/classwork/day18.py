#შექმენით რიცხვთა დიაპაზონი სადაც გექნებით ლუწი რიცხვები.

numbers_range = range(0,10 + 1,2)
for i in numbers_range:
    print(i)



#შექმენით სია სადაც გექნებათ 1-დან 10 ის ჩათვლით რიცხვები და SLICE ინგის გამოყენებით შექმენით ახალი სია სადაც გექნებათ მხოილოდ ის მნიშვნელობები შეტანილი, რომლის ინდექსბიც არის ლუწი

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:10:2])


# შექმენით პროგრამაც, სადაც გექნებათ ორი სია. პირველში 1-იდან 10-ის ჩათვლით დაამატეთ ლუწი რიცხვები, ხოლო მეორეში კენტები. გამოიყენეთ for ციკლი და append ფუნქცია

even_numbers = []
odd_numbers = []
for i in range(1, 10 + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(even_numbers)
print(odd_numbers)


#შექმენით პროგრამა, სადაც მოხმარებელს შეეკითხებით ხუთ რიცხვს. ლუწები ერთ სიაში, ხოლო კენტები მეორეში დაამატეთ

odd_list = []
even_list = []

for i in range(5):
    user_num = int(input("enter number:  "))

if user_num % 2 == 0:
    even_list.append(user_num)
else:
    odd_list.append(user_num)

print(odd_list)
print(even_list)


#შექმენით პროგრამა სადაც გექნებათ ორი სია. პირველ სიაში 10-იდან 20-ის ჩათვლით ლუწი რიცხვები, ხოლო მეორეში კენტები დაამატეთ. საბოლოოდ გამოიტანეთ ეს სიები (edited)

odd_list = []
even_list = []

for i in range(10, 21):
   if i % 2 == 0:
       even_list.append(i)
else:
    odd_list.append(i)

print(odd_list)
print(even_list)

       





