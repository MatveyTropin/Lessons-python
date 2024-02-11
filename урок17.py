"""name="Jame"
names=["BOB","Jame","Alex",[20,12,35]]
print(names[2])
names[2]="Sergey"
print(names)
names[3][0]=21
print(names)"""

field = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

"""print(field[0][0],field[0][1],field[0][2])
print(field[1])
print(field[2])"""
for x in range(3):
    for a in range(3):
        print(field[x][a],end=" ")
    print()


field = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]
] 

for x in range(2):
    for a in range(5):
         print (field[x][a],end=" ")
    print()