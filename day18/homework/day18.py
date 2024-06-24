#მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ სიაში. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.

numbers = []

for i in range(5):
    num = int(input("please enter number: "))
    numbers.append(num)

result = 0

for num in numbers:
    result = result + num

print(result)



#სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ სიაში არსებული ყველაზე დიდი რიცხვი, მინიშნება: გამოიყენეთ for ციკლი. არ გამოიყენოთ max მეთოდი.

numbers = [3,6,-1,2,8,9,4,5,7,-2]

max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)


#სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი. შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა.

numbers = []

for i in range(30, 50 + 1):
    numbers.append(i)


odd_count = 0

for number in numbers:
    if number % 2 != 0:
        odd_count = odd_count +1

print(odd_count)

#სიაში შეიტანეთ 10-იდან 50-ის ჩათვლით არსებული 4-ის ჯერადი რიცხვები. შემდეგ შეაბრუნეთ ეს სია და დაბეჭდეთ ის, test case: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

numbers = []

for i in range(12, 50 + 1, 4):
    numbers.append(i)


reversed_list = []

for index in range(len(numbers) -1,-1,-1):
    reversed_list.append(numbers[index])

print(numbers)
print(reversed_list)


#თქვენი დავალებაა, რომ სიაში შეიტანოთ 50-იდან 100-მდე არსებული ყველა რიცხვი. შემდეგ გამოიყენეთ for ციკლი და დაბეჭდეთ ყველა ლუწი რიცხვი  მათი ინდექსებით. test case: ["50 - 0", "52 - 3", "54 - 5", "56 - 7"]

even_numbers = []

for index in range(0, len(numbers)):
    if numbers[index] % 2 == 0:
        even_numbers.append(str(numbers[index]) + "-" + str(index))

print(numbers)
print(even_numbers)