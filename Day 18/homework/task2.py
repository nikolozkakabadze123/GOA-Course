'''Python:
input დავალებები:
1)დაწერეთ პროგრამა, რომელიც ითხოვს მომხმარებლის სახელს და ამის შემდეგ ბეჭდავს: "გამარჯობა, სახელი!"
2)მომხმარებელს შემოატანინეთ მასზე ინფორმაცია და ეს ყველაფერი ერთ print-ში დაბეჭდეთ'''

# პირველი დავალება: მომხმარებლის სახელი და გაცილება
name = input("შეიყვანეთ თქვენი სახელი: ")
print("გამარჯობა," + name + "!")

# მეორე დავალება: ასაკი, ქალაქი და ჰობი და მათი ერთ print-ში დაბეჭდვა
age = input("შეიყვანეთ თქვენი ასაკი: ")
city = input("შეიყვანეთ თქვენი ქალაქი: ")
hobby = input("რა გიყვართ? ")

print("მომხმარებელზე ინფორმაცია: " + age + " " + city + " " + hobby)
