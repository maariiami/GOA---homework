# შექმენით ორი სია, პირველში საყვარელი ადამიანების სახელები, ხოლო მეორეში ფავორიტი მანქანები ჩაწერეთ. ორივე სიაში 5 ელემენტი უნდა გქონდეთ. თავდაპირველად დაბეჭდეთ ორივე სია, შემდეგ გამოიყენეთ ინდექსები და დაბეჭდეთ კონკრეტული ელემენტები


favpeoples = ["mari", "nini", "ani", "nata", "masho"]
favbooks = ["zebuloni", "mox", "in the end they both die", "matteo falcone", "taras bulba"]
print(favpeoples)
print(favbooks)
print(favpeoples[4])
print(favbooks[3])

#შექმენით ორი სთრინგი, პირველში შეინახეთ თქვენი სახელი, ხოლო მეორეში გვარი. საბოლოოდ გამოიტანეთ თქვენი ინიციალები - სახელის პირველი ასო + . + გვარის პირველი ასო

name = "mari"
lastname = "abramishvili"
print(name[0] + "." + lastname[0])

#შექმენით ორი სია, უნდა გქონდეთ ორივე განსხვავებული ზომის. len ფუნქციის გამოყენებით გაიგეთ მათი სიგრძე

girls = ["mari", "nini", "ani", "nata", "masho"]
boys = ["luka", "nika", "saba", "andria", "bacho"]
print(len(girls))
print(len(boys))

#len ფუნქციის გამოყენებით გამოიტანეთ თქვენი გვარის ბოლო ასო

lastname = "abramishvili"
print(lastname[len(lastname)-1])