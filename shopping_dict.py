import os

SHOPPING_FILE = "shopping_dict.txt"

def load_dict():
    """从文件加载字典，格式：商品名:数量，每行一个"""
    shopping = {}
    if os.path.exists(SHOPPING_FILE):
        with open(SHOPPING_FILE,"r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    # 按冒号分割，例如“苹果：3” -> [“苹果”，“3”]
                    parts = line.split(":")
                    if len(parts) == 2:
                        name,qty = parts[0],int(parts[1])
                        shopping[name] = qty
    return shopping

def save_dict(shopping):
    """保存字典到文件，格式：商品名：数量"""
    with open(SHOPPING_FILE,"w",encoding="utf-8") as f:
        for name,qty in  shopping.items():
            f.write(f"{name}:{qty}\n")

def show_list(shopping):
    if not shopping:
        print("清单为空")
    else:
        for i,(name,qty) in enumerate(shopping.items(),1):
            print(f"{i}.{name} x{qty}")

# 主程序
shopping = load_dict()

while True:
    print("\n1-添加商品 2-删除商品 3-查看清单 4-退出")
    choice = input("请输入数字:")

    if choice == "1":
        name = input("请输入商品名称:")
        try:
            qty = int(input("数量:"))
            if qty <= 0:
                print("数量必须是正数")
                continue
        except ValueError:
            print("请输入数字数量")
            continue

        if name in shopping:
            shopping[name] += qty
            print(f"已更新:{name} 数量增加{qty},现为{shopping[name]}")
        else:
            shopping[name] = qty
            print(f"已添加:{name} x{qty}")
        save_dict(shopping)

    elif choice == "2":
        name = input("商品名称:")
        if name in shopping:
            del shopping[name]
            save_dict(shopping)
            print(f"已删除:{name}")
        else:
            print("清单中没有该商品")

    elif choice == "3":
        show_list(shopping)

    elif choice == "4":
        print("再见!")
        break

    else:
        print("请输入有效数字")
            
    
