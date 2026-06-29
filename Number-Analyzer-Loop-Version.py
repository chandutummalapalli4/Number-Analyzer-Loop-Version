num = int(input("Enter a Number: "))
original = num
temp1=num
max_digit = 0
min_digit = 9
total = 0
product = 1
count = 0
reverse = 0

while temp1 > 0:
    digit = temp1 % 10

    total += digit
    product *= digit
    reverse = reverse * 10 + digit
    count += 1

    if digit > max_digit:
        max_digit = digit

    if digit < min_digit:
        min_digit = digit

    if digit % 2 == 0:
        print("Even Digit:", digit)
    else:
        print("Odd Digit:", digit)
    temp1//= 10 
temp2=num
Amstrong=0
while temp2>0:
    digit=temp2%10
    Amstrong+=digit**count
    temp2//=10
print("Sum Of Numbers:", total)
print("Product of Numbers:", product)
print("Count of Digits:", count)
print("Reverse of Number:", reverse)
print("Largest Digit is:", max_digit)
print("Smallest Digit Is:", min_digit)
if original==reverse:
    print("It is palindrome")
else:
    print("Not a palindrome")
if Amstrong==original:
    print("Amstrong Number")
else:
    print("Not a Amstrong Number")
