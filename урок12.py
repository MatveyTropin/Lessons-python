"""def say_hi (name,lastname):
    print("Hello "+ name + lastname)
say_hi("Mark ","Ogorodov")
say_hi("Sergey ","Ivanov")
say_hi("Stepan ","Artamonov")
def get_square_area (a):
    S=a*a
    print('square area is '+ str(S))
get_square_area(10)"""

"""def get_rect (a,b):
    S=a*b
    P=(a+b)*2
    print("rect square is="+str(S))
    print("rect Perimeter is="+str(P))
get_rect(a=20,b=30)
get_rect(a=3000,b=800)"""
def pow(n,d):
    answer=1
    while d>0:
        answer=answer*n
        d=d-1
    return answer
answer=pow(n=4,d=20)
print(answer)

def get_circle (r):
    S=3.14*r*r
    return S
    
answer=get_circle(r=2)
print(answer)
print("circle square is="+str(answer))
