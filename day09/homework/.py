#მომხმარებელს შეეკითხეთ ხელფასი
#თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?
#თუ 1000----10000 -ია , დაუპრინტეთ you mid
#თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო



salary = int(input("How much is your salary?  "))
if salary > 10000:
    print("Did you study in Goa?")
elif salary > 1000 and salary < 10000:
    print("You mid")
elif salary < 1000:
    print("Enter Goa")
