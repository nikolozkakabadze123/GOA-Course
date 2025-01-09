'''4) Bonus დავალება
შექმენით პროგრამა, რომელიც განსაზღვრავს productive ცვლადის მნიშვნელობას შემდეგი პირობების მიხედვით:
read_pages ცვლადში ინახება წაკითხული გვერდების რაოდენობა (მთლიანი რიცხვი).
free_time ცვლადში ინახება boolean მნიშვნელობა (True/False), რომელიც გვიჩვენებს, ჰქონდა თუ არა თავისუფალი დრო.
productive ცვლადი იქნება ჭეშმარიტი (True), თუ მოსწავლემ წაიკითხა მინიმუმ 20 გვერდი და თავისუფალი დრო ჰქონდა.

მაგალითი:
თუ read_pages = 25 და free_time = True, მაშინ productive = True.
თუ read_pages = 15 და free_time = True, მაშინ productive = False.
თუ read_pages = 30 და free_time = False, მაშინ productive = False.
'''
read_pages =25
free_time = True
productive = (read_pages>=20) and free_time
print(productive)
