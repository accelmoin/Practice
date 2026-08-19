a = 10
b = 20
c = a + b
print(c)

a = ["hello",1,23,2.9]
b = [1,2,3,4]
c = (1,2,3,4)
cars = ["Ford", "Volvo", "BMW"]

print(f"{a}\n {b}\n {c}")

print(type(a))
print(type(b))
print(type(c))

import array
arr = array.array("i",[-1, 2, 3, 4])
print(arr)
print(type(arr))

r = range(11,21)
print(type(r))    # <class 'range'>
print(list(r))    # [0, 1, 2, 3, 4]
