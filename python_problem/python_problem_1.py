import random

def brGame(player):
    global num
    if player == "computer":
        n = random.randint(1, 3)
    else:
        while True:
            try:
                n = int(input(f"{player}, 부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
                if n in [1, 2, 3]:
                    break
                else:
                    print("1,2,3 중 하나를 입력하세요")
            except ValueError:
                print("정수를 입력하세요")

    for i in range(1, n + 1):
        num += 1
        print(f"{player} : ", num)
        if num == 31:
            return True
    return False

def two_player():
    while num < 31:
        if brGame("playerA"):
            print("playerB win!")
            break
        
        if num < 31 and brGame("playerB"):
            print("playerA win!")
            break
        
def one_player():
    while num < 31:
        if brGame("computer"):
            print("player win!")
            break
        
        if num < 31 and brGame("player"):
            print("computer win!")
            break

num = 0

while True:
    try:
        mode = int(input("게임 모드를 선택하세요 (1: 혼자 플레이, 2: 둘이 플레이): "))
        if mode in [1,2]:
            break
        else:
            print("1 또는 2를 입력하세요")
    except ValueError:
        print("1 또는 2를 입력하세요")
        
if mode == 1:
    one_player()
else:
    two_player()

# num = 0;

# while num < 31:
#     # playerA
#     while True:
#         try:
#             a = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ", ))
#             if a in [1,2,3]:
#                 break
#             else:
#                 print("1,2,3 중 하나를 입력하세요")
#         except ValueError:
#             print("정수를 입력하세요")
            
#     for i in range(1, a+1):
#         num += 1
#         if num == 31:
#             print("playerA : ", num)
#             print("playerB win!")
#             break
#         else:
#             print("playerA : ", num)
    
#     if num == 31:
#         break
    
#     # playerB
#     while True:
#         try:
#             b = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ", ))
#             if b in [1,2,3]:
#                 break
#             else:
#                 print("1,2,3 중 하나를 입력하세요")
#         except ValueError:
#             print("정수를 입력하세요")

#     for i in range(1, b+1):
#         num += 1
#         if num == 31:
#             print("playerB : ", num)
#             print("playerA win!")
#             break
#         else:
#             print("playerB : ", num)
    
#     if num == 31:
#         break