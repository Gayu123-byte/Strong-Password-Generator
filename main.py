import random
import array
maxlen=8
temp_pass=0
digits=['0','1','2','3','4','5','6','7']
lowercase=['a','b','c','d','e','f','g','h','i']
uppercase=['A','B','C','D','E','F','G','H','I']
symbols=['!','@','#','$','%','^','&','*','(',')']
combinedlist=digits+lowercase+uppercase+symbols
rand_digit=random.choice(digits)
rand_upper=random.choice(uppercase)
rand_lower=random.choice(lowercase)
rand_symbol=random.choice(symbols)
temp_pass=rand_digit+rand_upper+rand_lower+rand_symbol
for x in range (maxlen -4):
    temp_pass=temp_pass+random.choice(combinedlist)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
password=""
for x in temp_pass_list:
    password=password+x
print(password)
