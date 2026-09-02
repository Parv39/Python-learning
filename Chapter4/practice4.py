# a = [1,4,5,3]
# a.sum()
# print(a) Not works

# b = 1,2,3,4
# sum(b)
# print(b) Not works
#sum() is a built-in Python function, not a method of lists or tuples.
# Therefore, use sum(list) or sum(tuple), not list.sum() or tuple.sum().

b = (1, 2, 3, 4)

print(sum(b))
#OR
c = sum(b)
print(c)