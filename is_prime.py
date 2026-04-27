def is_prime(n):
    if num < 2:
        return False
    
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    num_str = input("请输入一个正整数（输入q退出）:")
    if num_str == "q":
        print("再见")
        break
    if not num_str.isdigit():
        print("请输入正整数:")
        continue

    num = int(num_str)

    if is_prime(num):
        print(f"{num}是质数")
    else:
        print(f"{num}不是质数")
