import random

while True:
    # 生成1~100的随机数
    secret = random.randint(1,100)
    count = 0
    print("我已经想好了一个1~100之间的整数，你能猜中它吗？")

    while True:
        guess = input("猜一个数字:")

        # 检查输入是否为数字
        if not guess.isdigit():
            print("请输入一个有效的整数!")
            continue

        num = int(guess)
        count += 1

        if num < secret:
            print("太小了!")
        elif num > secret:
            print("太大了!")
        else:
            if count == 1:
                print(f"天才！你猜了{count}次就猜中了！")
            elif 2<= count <= 5:
                print(f"不错！你猜了{count}次就猜中了！")
            else:
                print(f"你猜了{count}次才猜对，继续加油!")
            break # 跳出内层循环

    # 询问是否继续
    again = input("是否再玩一局？(y/n):")
    if again.lower() != 'y':
        print("下次再来!")
        break
            
