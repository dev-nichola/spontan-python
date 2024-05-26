# For In python
buah = [
    "Apple", "Orange", "Pineapple"
]

for b in buah :
    print(b)

# For Range 
for x in range(2, 6) :
    print(x)

perulangan = 100
for angka in range(1, perulangan + 1) :
    if angka % 3 == 0 and angka % 5 == 0 : 
        print("FizzBuzz")
    elif angka % 3 == 0 :
        print("Fizz")
    elif angka % 5 == 0 :
        print("Buzz")

# Break
for capek in range(0, 100) : 
    if capek == 50 :
        break
    print("Perulangan Ke + ", capek)

print("Hadeh Capek....")
