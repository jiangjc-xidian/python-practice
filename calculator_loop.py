# 带循环的计算器（含计数功能）

count = 0   # 记录次数

while True:
    # 获取第一个数字，检查是否要退出
    first = input("请输入第一个数字（或输入quit退出):")
    if first == "quit":
        print("你共计算了",count,"次")   # 退出时显示次数
        print("再见!")
        break

    # 获取运算符和第二个数字
    op = input("请输入运算符（+，-，*，/，%）:")
    second = input("请输入第二个数字:")

    # 转化成数字（注意：此时已经排除了 quit）
    num1 = float(first)
    num2 = float(second)

    # 计算
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if second == "0":
            result = "除数不能为0"
        else:
            result = num1 / num2
    elif op == "%":
        if second == "0":
            result = "除数不能为0"
        else:
            result = num1 % num2
    else:
        result = "不支持的运算符"

    print("结果是:",result)
    print() # 打印一个空行，让界面更清爽


    count = count + 1   # 每次计算完，次数加1
             
