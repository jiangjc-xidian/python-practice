def double_even(numbers):
    return [n * 2 for n in numbers if n % 2 == 0]

while True:
    user_input = input("请输入整数列表（用逗号分隔，如1，2，3，4）或输入q退出:")
    if user_input.lower() == 'q':
        print("再见")
        break
    try:
        nums = [int(x.strip()) for x in user_input.split(',')]
        result = double_even(nums)
        print("结果:",result)
    except ValueError:
        print("输入格式有误，请重新输入")
