import random

choices = ["石头","剪刀","布"]
player_score = 0
computer_score = 0

print("欢迎来玩石头剪刀布！输入 石头 剪刀 或 布")

while True:
    player = input("你的选择:")
    if player not in choices:
        print("请输入 石头、剪刀 或 布")
        continue

    computer = random.choice(choices)
    print(f"电脑出了:{computer}")

    # 判断胜负
    if player == computer:
        print("平局!")
    elif (player == "石头" and computer == "剪刀") or \
         (player == "剪刀" and computer == "布") or \
         (player == "布" and computer == "石头"):
        print("恭喜你取得胜利！")
        player_score = player_score + 1
    else:
        print("很遗憾，你输了。")
        computer_score = computer_score + 1

    again = input("再玩一局？(y/n):")
    if again != "y":
        print(f"你一共赢了{player_score}局，输了{computer_score}局。")
        print("欢迎下次再来!")
        break
        
