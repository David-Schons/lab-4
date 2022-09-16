number = float(input("Enter your upper limit: "))

perfect = 0
deficient = 0
abundent = 0
sum=0
index = 1
test = 1
while index <= number:
    while test < index:
        if index % test == 0:
            sum = test + sum
        test = test+1
    if sum == index:
        perfect = perfect + 1
    elif sum > index:
        abundent = abundent+1
    elif sum < index:
        deficient = deficient +1

    sum = 0
    test=1
    index = index + 1

print("between 1 and",number,",There are:")
print(deficient,"Deficient numbers")
print(perfect,"perfect numbers")
print(abundent,"abundent numbers")

