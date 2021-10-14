set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
 
# union of two sets
print("set1 U set2 : ", set1.union(set2))

#intersection of sets
print("set1 intersection set2 : ",
      set1.intersection(set2))
      
# diff. of two sets
print("set1 - set2 ",end="")
print (set1.difference(set2))
print("set2 - set1 ",end="")
print (set2.difference(set1))

#symmetric difference of set
print(set1 ^ set2)
print(set2 ^ set1)
