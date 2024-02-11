name="Masha"
names=["Masha","Stepan","Vlad"]# [ ] - создает список
print(names)
print("Masha"in names)
print("Sergey"in names)# True - это правда (да)
# False - это ложь (нет)
# "Masha" in names - есть ли Masha в списке names
print("Petr"not in names)
print("Stepan"not in names)
for name in names:
    print("hello "+name)# for что-то in список - повторяет код написанный под ним, для каждого элемента списка