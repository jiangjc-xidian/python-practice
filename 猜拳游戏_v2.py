import random

choices = ["石头","剪刀","布"]
player_score = 0
computer_score = 0


print("请出拳:0-石头，1-剪刀，2-布")

while True:
    player = int(input("请输入数字:"))
    computer = random.randint(0,2)


    print(f"你出了:{choices[player]}")
    print(f"电脑出了:{choices[computer]}")


    if player == computer:
        print("平局")
    elif (player == 0 and computer == 1) or \
         (player == 1 and computer == 2) or \
         (player == 2 and computer == 0):
        print("你赢了！")
        player_score += 1
    else:
        print("你输了！")
        computer_score += 1

    again = input("再来一局?(y/n):")
    if again != "y":
        print("下次再来。")
        print(f"你赢了{player_score}局，输了{computer_score}局。")
        break
