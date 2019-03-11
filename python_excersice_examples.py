
name = 'John'
age = 30
is_new = True 

name = input('What is your name ? ')
print ('Hi ' + name)



name0 = input('What\'s your name ?')
color = input('What is your favourite colour ? ')
print (name0 +  " likes "  + color)


birth_year = input('Birth year ')
age = 2019 - int(birth_year)
print(age)


list= [2,2.5,3,3.5,4,4.5,5]
for i in list:
    print (i)

waga_kg=input('Podaj swoją wagę w kg:  ')
waga_lbs= int(waga_kg)*2.2
print("twoja waga wynosi " + str(waga_lbs) + " funtów ")


robert_is = input('Jak mieszka robert  ? ')
robert_now = f'Robert mieszka teraz : {robert_is}'

print(robert_now)
print(robert_now.upper())
print(robert_now.lower())
print(robert_now.find('mieszka'))
print(robert_now.replace('daleko', 'bardzo daleko '))
print ('daleko' in robert_now)

x = 2.9
print(round(x))
print(abs(-x))




# ---------------------- IF STATMENT ------------------------


is_hot = False
is_cold=True

if is_hot:
    print('It is a hot day')
    print('drink plenty of water')
elif is_cold:
    print('It is a cold  day ')
    print('Wear warm clothes')
else:
   print("It's a lovely day ")
print('Enjoy your day')





good_credit = False
bad_credit = True

good_price = 1000000 * 1.1
bad_price = 1000000 * 1.2

if good_credit:
    print(f" Good price is:   {good_price}")

elif bad_credit:
    print (f"Bad price is: {bad_price}")
else:
    print('Down payment: ') 



has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
    print ('Eligible for loan')



has_high_income = True
has_good_credit = False

if has_good_credit or has_high_income:
    print ('Eligible for loan')



has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print ('Eligible for loan')

temperature = 31

if temperature > 30:
    print("It's a hot day ")
elif temperature < 10:
    print("It's a cold day ")
else :
    print("it's neither hot or cold ")




name = ('dawid')
if len(name) < 3 :
    print ('name must be at least 3 characters')
elif len(name) >= 50: 
    print ('name can be maxiumum of 50 characters')
else: 
    print ("name look's good . ")


weight = int(input("Input your Weight: "))
lbs_kg = input ("(L)bs or (K)g: " )
lbs = weight * 0.45
kg = weight * 2.2

if lbs_kg.upper() == 'L':
    print (f'Your weight = {lbs}kg  ')
elif lbs_kg.upper() == 'K':
    print (f'Your weight = {kg}lbs ')
else:
    ("Input 'L' or 'K' ")


# --------------- WHILE LOOP -----------------------------------

i = 1 
while i<=5:
    print(i)
    i = i+1
print("Done")


i = 1 
while i<=5:
    print('*' * i)
    i = i+1
print("done :D ")


secret_number = 9
guess_count = 0
guess_limit = 3 
while guess_count < guess_limit:
    insert_num = int((input('Insert the number: ')))
    guess_count += 1 
    print (insert_num)
    if insert_num == secret_number:
        print("Great the secret number is 9 ! You won!  ")
        break

    elif insert_num != 9:
        print("Try again")
    else:
        print("You lose ! ")





class Person():
 def __init__(self, name, favouriteFilm, age):
     self.age = age
     self.name = name
     self.favouriteFilm = favouriteFilm

p1 = Person('RObert', 'Bob_Budowniczy', 18)
p2 = Person('Dawid', 'sdasasd', 20)
print(p1.name)
print(p1.favouriteFilm)
print(p1.age)
print(p2.age)

 
       
     

    
  