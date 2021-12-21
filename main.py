from data import values
import random
import os
cond=True
#a=random.choice(values)
b=random.choice(values)
score=0
print("""Welcome to Higher Lower Game !!!
You will be given two choice 'A' and 'B'
You will have to choose if 'A' can be higher than 'B' """)
while cond:
    a=b
    b=random.choice(values)
    while a['name']==b['name']:
        b=random.choice(values)
    print(f"""Compare 
A : {a['name']} who is {a['description']} from {a['country']}
with
B : {b['name']} who is {b['description']} from {b['country']}"""    )
    guess=input("""Who is having more followers ?
Enter 'A' for A and
Enter 'B' for B\n""")
    os.system("cls")
    val_a=a['follower_count']
    val_b=b['follower_count']
    if guess=='A':
        if val_a>val_b:
            print('Correct')
            score+=1
        else:
            print('Wrong')
            cond=False
            
    else:
        if val_a<val_b:
            print('Correct')
            score+=1
        else:
            print('Wrong')
            cond=False
           
    print('Your current score is',score)
    print()
print('\nFinal score is',score)
print('The Game Ends .')





    


