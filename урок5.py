# 1) Нельзя писать число в начале названия переменной 
# 2) Нельзя использовать слова, которые сам Python использует
# 3) Нельзя писать названия переменными русскими словами
# 4) Нельзя использовать разные символы (;,.@#$%^&()+!), кроме нижнего подчеркивания _
current_year=2022
print("Now "+ str(current_year)+" year")
birth_year=int(input("When did you born?"))
age=current_year-birth_year
print("You are "+str(age)+" years old")