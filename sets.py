#creating sets- duplicates will not be allowed
set={10,20,30,40,50}
print(set)

set2={10,10,20,30,40,30}
print(set2)



#check if an element is exist in the set

if 12 in set2:
    print("Element  found")
else:
    print("Element not found")

#Adding elements to a set

myset={1,2}
myset.add(10)
myset.add(15)
myset.add(25)
myset.add(30)
myset.add(45)
print(myset)

#taking away from a set

myset.remove(25)
print(myset)


#set Opreations

# 1. union of sets
# 2. intersections of sets
# 3. diffrence or sets
# 4. symmetric of diffrence of sets


a={1,2,3,4,5}
b={4,5,6,7,8}


# 1. union of sets

print(a.union(b))

# 2. intersections of sets

print(a.intersection(b))


# 3. diffrence or sets

print(a.difference(b))
print(b.difference(a))


# 4. symmetric of diffrence of sets

print(a.symmetric_difference(b))



