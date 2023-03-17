list1=['a','b','c','d','e','f']
list2=['d','e','f','g','h']
print("missing values in second list:",",".join(set(list1).difference(list2)))
print("additional values in second list:",",".join(set(list2).difference(list1)))