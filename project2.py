import random 

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("اكتب تخمينك (من 1 إلى 100): "))

    if (guess < number ) :
        print("تخمينك أقل من الرقم الصحيح.")
    elif ( guess > number): 
        print("تخمينك أكبر من الرقم الصحيح.")
    else:
        print("تهانينا! لقد خمّنت الرقم الصحيح:", number)
        break
 