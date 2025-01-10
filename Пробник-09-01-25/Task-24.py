with open("24-input.txt") as f:
    data = f.readline()

print(len(data))


from string import ascii_uppercase

##for i in ascii_uppercase[1:]:
##    data = data.replace(i, "B")
##
##for i in range(100):
##    data = data.replace("BB", "B")

C = data.count("A")
N = 0
for i in range(1, C):
    N += i

CC = data.count("AA")
RES = N - CC

print(RES)

        
        


































