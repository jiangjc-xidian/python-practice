import random

while True:
    secret = random.randint(1, 100)
    count = 0
    guesses = []          # 存储历史猜测
    max_attempts = 7      # 最多猜7次

    print("我已经想好了一个1~100之间的整数，你能猜中它吗？")
    print(f"你有{max_attempts}次机会。")

    while True:
        # 检查是否还有剩余机会
        if count >= max_attempts:
            print(f"很遗憾，{max_attempts}次机会用完了。正确答案是 {secret}。")
            break   # 跳出内层循环，进入“是否再玩一局”

        guess = input("猜一个数字：")

        # 检查输入是否为数字
        if not guess.isdigit():
            print("请输入一个有效的整数！")
            continue

        num = int(guess)
        # 可选：检查范围
        if num < 1 or num > 100:
            print("请输入1~100之间的数字！")
            continue

        guesses.append(num)
        count += 1

        if num < secret:
            print("太小了！")
        elif num > secret:
            print("太大了！")
        else:
            # 猜中了，显示历史记录
            print(f"恭喜！你猜了{count}次，历史猜测：{guesses}")
            if count == 1:
                print("天才！一次就中！")
            elif 2 <= count <= 5:
                print(f"不错！你猜了{count}次就猜中了！")
            else:
                print(f"你猜了{count}次才猜对。继续加油！")
            break   # 猜中，跳出内层循环

    # 询问是否继续
    again = input("是否再玩一局？(y/n): ")
    if again.lower() != 'y':
        print("下次再来！")
        break
