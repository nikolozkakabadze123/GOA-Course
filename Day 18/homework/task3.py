'''ლოგიკური ოპერაციებზე დავალებები:
4)and-ის გამოყენებით გააკეთეთ  boolean მაგალითები მაგალითად True and False და ასე შემდეგ კომენტარში ახსენით თუ რატო გამოდის ეგეთი  შედეგი როგორიცაა False
5)იგივე რამ გააკეთეთ ოღონდ უკვე or-ის გამოყენებით მაგალითად True or False და კომენტარში ახსენით თუ რატომ არის საბოლოო პასუხი True და კიდე ბევრი მაგალითი გააკეთეთ კომენტარით ახსენით
'''

#and
#True and False უბრუნებს False, რადგან and-ის ოპერატორი მაშინ აბრუნებს True, როცა ორივე პირობა True-ა. აქედან, რადგან მეორე პირობა False-ია, საბოლოო შედეგი იქნება False.
# True and False
print(True and False)  # შედეგი: False

#რადგან ორივე პირობა False-ია, and-ის ოპერატორი ყოველთვის დააბრუნებს False.
# False and False
print(False and False)  # შედეგი: False

#როდესაც ორივე პირობა True-ა, and-ის ოპერატორი აბრუნებს True.
# True and True
print(True and True)  # შედეგი: True

#or
#True or False უბრუნებს True, რადგან ერთი პირობა მაინც არის True. or-ის ოპერატორი უბრუნებს True, თუ რომელიმე პირობაა True
# True or False
print(True or False)  # შედეგი: True

#რადგან ორივე პირობა არის False, or-ის ოპერატორი აუცილებლად დააბრუნებს False
# False or False
print(False or False)  # შედეგი: False

#მიუხედავად იმისა, რომ პირველი პირობა False-ა, მეორე პირობა არის True, ამიტომ or-ის ოპერატორი მაინც დააბრუნებს True.
# False or True
print(False or True)  # შედეგი: True

