a = {1,2,11,22} #Indexing is not in set Hashable means an object has a fixed (unchangeable) hash value that Python can use to identify it.
b = {1,7,8,22,3}

print(a.union(b))
print(a.intersection(b))
#It is not possible. ✅

# s = {1, 2, 3, 4, [2, 3]}

# This gives:

# TypeError: unhashable type: 'list'
# Why?

# A set can contain only hashable (immutable) elements.

# ✅ 1, 2, 3, 4 → Hashable
# ❌ [2, 3] → List is mutable, so it is not hashable
s = {1, 2, 3, 4, (2, 3)}
print(s) #This works because (2, 3) is a tuple, which is hashable (as long as all its elements are hashable).