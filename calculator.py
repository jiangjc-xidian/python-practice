# 简单计算器

num1=float(input("请输入第一个数字:"))

op=input("请输入运算符(+,-,*,/,%):")

num2=float(input("请输入第二个数字:"))

if op=="+":
      result=num1+num2
elif op=="-":
      result=num1-num2
elif op=="*":
      result=num1*num2
elif op=="/":
      if num2==0:
          result="除数不能为0!"
      else:
           result=num1/num2
elif op=="%":
      if num2==0:
            result="除数不能为0！"
      else:
            result=num1%num2
else:
      result="不支持的运算符"

print("结果是:",result)
