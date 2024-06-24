#შექმენით 2 ცვლადი სადაც შეტანილი გექნებათ ადამიანის წონა და სიმაღლე, (required_weight,required_height) რომლის მნიშვნელობაც იქნება 50 და 170 , შემდეგ მომხმარებელს შემოატანინეთ მისი წონა input ფუნქციის მეშვეობითდა შეამოწმეთ მომხმარებლის წონა თუ უდრის required_weight ცვლადს და მომხარებლის სიმაღლე თუ უდრის required_height, აგრეთვე მეორე პრინტში შეამოწმეთ თუ აღემატება წონას და ნაკლებია სიმაღლეზე, თითქმის ყველა კომბინაცია შედარების ოპერატორების.



required_height = 170
required_weight = 50

person_height = int(input("enter your height: "))
person_weight = int(input("enter your weight: "))

print(required_height == person_height)
print(required_weight == person_weight)

print(required_height > person_height)
print(required_weight < person_weight)


#მომხმარებელს შემოატანინეთ აჯიმანიებისა და ბუქნების რაოდენობა, ტქვენ კი შეამოწმეთ უდრის ტუ არა აჯიმანიების რაოდენობა აუცილებელს ან ბუქნების რაოდენობა აუცილებელს



target_pushups = 100
target_squats = 50

pushups = int(input("how many pushups have you done?  "))
squats = int(input("how many squats have you done? "))

print(target_pushups == pushups)
print(target_squats == squats)


