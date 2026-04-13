# 一行表达式计算器

count = 0

while True:
    expr = input("请输入表达式(或quit退出,restart重新开始):")

    if expr == "quit":
        print("你共计算了",count,"次")
        print("再见")
        break

    elif expr == ("restart"):
        print("重新开始本次计算")
        continue

    # 按空格分割表达式，得到三个部分：数字1、运算符、数字2
    parts = expr.split()

    # 检查分割后是否正好是3个部分
    if len(parts) != 3:
        print("格式错误！请按格式输入：数字 运算符 数字 （例如5 + 3）")
        continue

    first, op, second = parts # 解包赋值

    # 尝试转换为数字
    try:
        num1 = float(first)
        num2 = float(second)
    except ValueError:
        print("请输入有效数字!")
        continue

    # 计算
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if second == 0:
            result = "除数不能为0"
        else:
            result == num1 / num2
    elif op == "%":
        if second == 0:
            result = "除数不能为0"
        else:
            result == num1 % num2
    elif op == "**":
        result = num1 ** num2
    else:
        result == "不支持的运算符"

    print("结果是:",result)
    print()
    count = count + 1
