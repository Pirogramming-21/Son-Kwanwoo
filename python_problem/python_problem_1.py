num = 0;

while True:
    try:
        a = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ", ))
        if a in [1,2,3]:
            break
        else:
            print("1,2,3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")
        
for i in range(1, a+1):
    num += 1
    print("playerA : ", num)
    
while True:
    try:
        b = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ", ))
        if b in [1,2,3]:
            break
        else:
            print("1,2,3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")

for i in range(1, b+1):
    num += 1
    print("playerB : ", num)