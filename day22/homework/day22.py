#შექმენით ფუნქცია სახელად numbers_product. ფუნქციას გადაეცით სამი არგუმენტი - start, end, step. შემდეგ გამოიყენეთ while ციკლი (for ციკლი არ შეიძლება) და სიაში დაამატეთ რიცხვები - დაიწყეთ start-იდან, იტერაცია მოახდინეთ step-ით და ციკლი ამუშავეთ end-ამდე. განიხილეთ ეს სია და მოახდინეთ მასზე ფილტრაცია, კიდევ ახალ სიაში დაამატეთ მარტო 3-ის ჯერადი რიცხვები. საბოლოოდ დააბრუნეთ 3-ის ჯერადების სიის ყველა რიცხვის ნამრავლი - product.
def numbers_product(start, end, step):
    list = []
    product = 1
    current_number = start
    while current_number <= end:
        if current_number % 3 == 0:
            list.append(current_number)
            product *= current_number
            current_number += step
            return product
        

#შექმენით ფუნქცია სახელად hashtag generator. მომხმარებელს შეეკითხეთ წინადადება და ის გადაეცით არგუმენტად ფუნქციას. მუშაობის წესები: საბოლოო ვერსია იწყება #-თი, სიტყვები შეერთებულია, ყველა სიტყვა იწყება დიდი ასოთი. Test case:"abc def ghi" -> "#AbcDefGhi"
def hashtag_generator(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    if not capitalized_words:
        return None
    hashtag = '#' + ''.join(capitalized_words)
    return hashtag


#შექმენით ფუნქცია სახელად num_divisors. ამ სიას არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ სია, სადაც იქნება ამ რიცხვის ყველა გამყოფი. Test case: 20 -> [1, 2, 4, 5, 10, 20]
def num_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


# შექმენით ფუნქცია manual_split. ამ ფუნქციაში უნდა შეიმუშავოთ split-ის მსგავსი ალგორითმი, მაგრამ არ გამოიყენოთ თვითონ split. თქვენ ფუნქციას არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი სიტყვა. ასევე მომხმარებელს შეეკითხეთ start, end, step მნიშვნელობები, გადაეცით ფუნქციას და იმუშავეთ სიტყვაზე. Test case: "Hello World!", 2, 6, 2 -> "lo".
def manual_split(string, start, end, step):
    result = ""
    if start < 0:
        start = len(string) + start
    if end < 0:
        end = len(string) + end
        for i in range(start, end, step):
            result += string[i]

    return result


#Codewars:
 
#1. https://www.codewars.com/kata/5467e4d82edf8bbf40000155/python

def descending_order(num):
    digits = list(str(num))
    digits.sort(reverse=True)
    result = int(''.join(digits))
    return result


#2. https://www.codewars.com/kata/54c27a33fb7da0db0100040e/python

def is_square(n):
    return n >= 0 and int(n ** 0.5) ** 2 == n

#3. https://www.codewars.com/kata/55908aad6620c066bc00002a

def equal_x_and_o(string):
    string = string.lower()
    count_x = string.count('x')
    count_o = string.count('o')
    return count_x == count_o

