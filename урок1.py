"""
print(5)
print(153)
print(5*16)
print("hello")
print("hello "+"matvej")"""
import random
name=input("как тебя зовут ")
print(name+" привет")
choice=input("хочешь ли ты сыграть в игру ")
if choice=="да":
    print("хорошо давай сыграем в игру угадай число")
    print("угадай число от 1 до 10")
    secret_number=random.randint(1,10)
    user_number=input("какое число ты думаешь я загадал ")
    user_number=int(user_number)
    if secret_number>user_number:
        print("моё число больше")
    if secret_number<user_number:
        print("моё число меньше")
    if secret_number==user_number:
        print("молодец ты угадал красавчик")
        
    user_number=input("какое число ты думаешь я загадал ")
    user_number=int(user_number)
    if secret_number>user_number:
        print("моё число больше")
    if secret_number<user_number:
        print("моё число меньше")
    if secret_number==user_number:
        print("молодец ты угадал красавчик")

    user_number=input("какое число ты думаешь я загадал ")
    user_number=int(user_number)
    if secret_number>user_number:
        print("моё число больше")
    if secret_number<user_number:
        print("моё число меньше")
    if secret_number==user_number:
        print("молодец ты угадал красавчик") 
