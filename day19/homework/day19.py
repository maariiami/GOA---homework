#ნამრავლის გამოთვლა: დაწერეთ ალგორითმი, რომელიც დაბეჭდავს სიის ყველა ელემენტის ნამრავლს.

numbers = [1,2,3,4,5]
print(numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4])

#უარყოფითი რიცხვების ამოღება: დაწერეთ ალგორითმი, რომელიც მიიღებს მთელ რიცხვთა სიას და ამოიღებს ყველა უარყოფით რიცხვს, დაბეჭდავს ახალ სიას ამ ელემენტების გარეშე.

numbers = [-3,-2,-1,0,1,2,3]
list = []
for num in numbers:
    if num >0:
        list.append(num)
print(list)



#საშუალოს პოვნა: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას და დააბრუნებს მის საშუალო არითმეტიკულს.

numbers = [1,2,3,4,5,3]
print((numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5]) / 6)

#სიების შეერთება: დაწერეთ ალგორითმი, რომელიც მიიღებს ორ რიცხვთა სიას, გააერთიანებს მათ ერთ სიაში და ამ სახით დაბეჭდავს.

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list1 + list2)

#დუბლიკატების სია: დაწერეთ ალგორითმი, რომელიც მიიღებს სიას. თქვენ შემდეგ ამ სიის დუბლიკატებს გადაიტანთ ახალ სიაში და დაბეჭდავთ მას.

list1 = [1,2,3,7,2,8,3,5,9,7,5,2]
list2 = [2,3,7,5]
print(list2)

