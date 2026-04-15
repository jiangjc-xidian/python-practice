import random

print("请选择难度:")
print("1.简单（1~50）")
print("2.中等（1~100）")
print("3.困难（1~200）")

difficulty = input("输入数字选择难度:")

if difficulty == "1":
    max_num = 50
elif difficulty == "2":
    max_num = 100
elif difficulty == "3":
    max_num = 200
else:
    print("请输入有效数字！")

while True:
    secret = random.randint (1,max_num)
    count = 0
    guesses = []
    max_attempts = 10

    print(f"我已经想好了一个1~{max_num}之间的整数，你能猜中他吗？")
    print(f"你有{max_attempts}次机会。")

    while True:

        if count >= max_attempts:
            print(f"很遗憾，{max_attempts}次机会已用完。正确答案是{secret}。")
            break

        guess = input("猜一个数字:")

        if not guess.isdigit():
            print("请输入一个有效的整数！")
            continue

        num = int(guess)

        if num < 1 or num > max_num:
            print(f"请输入1~{max_num}之间的数字！")
            continue

        guesses.append(num)
        count += 1
        if num < secret:
            print("太小了！")
        elif num > secret:
            print("太大了")
        else:
            if count == 1:
                print("天才！一次就中！")
            elif 2 <= count <= 5:
                print(f"不错！你猜了{count}次就猜中了！")
            else:
                print(f"你猜了{count}次才猜对，继续加油！")
            print(f"历史猜测:{guesses}")
            break

    again = input("是否再玩一局？(y/n):")
    if again.lower() != 'y':
        print("下次再来!")
        break
            
