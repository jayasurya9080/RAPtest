lst = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
temp=set(lst)
result={}
for i in temp:
    result[i]=lst.count(i)
print(result)