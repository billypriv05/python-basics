# ask the user for their name
username = input("whats your name? ")

# ask the user for their favourite integer
fav_num= int(input("favourite number? "))

# double, halve and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

print()
# greet the user
print("hi, {}, you favourite number is {}".format(username, fav_num))
print()
# output the results of doubling, halving
# and squaring their favourite number
print("double {} is {}".format(fav_num, double))
print("half {} is {}".format(fav_num, half))
print(" {} squared is {}".format(fav_num, squared))
print()