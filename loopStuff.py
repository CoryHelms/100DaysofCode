#Iterate through every number in a list to separate out even and odd numbers. Identify possible outlier values as well

numbers = [1,2,3,4,5,6,7,8,9,10,11,250,349875]

evens = []
odds = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])
    elif numbers[i] % 2 == 1:
        odds.append(numbers[i])

print(evens)
print(odds)

#Find the sum of all numbers in a list
nums = [4,5,6,7]
numsum = 0
evenNumSum = 0

for num in nums:
    numsum += num

print("Sum of all numbers is", numsum)

#sum of all even numbers
for num in nums:
    if num % 2 == 0:
        evenNumSum += num

print("Sum of all even numbers is", evenNumSum)


#count all even numbers in numbers list
evenCount = 0
for num in numbers:
    if num % 2 == 0:
        evenCount += 1

print("The amount of even numbers in numbers list is", evenCount)

