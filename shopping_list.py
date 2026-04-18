import os

SHOPPING_FILE = "shopping.txt"


def load_list():
    """从文件加载购物清单"""
    if os.path.exists(SHOPPING_FILE):
        with open(SHOPPING_FILE,"r",encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_list(lit):
    """保存购物清单到文件"""
    with open(SHOPPING_FILE,"w",encoding="utf-8") as f:
        for item in lit:
            f.write(item + "\n")


shopping_list = load_list()

while True:
    print("\n请选择操作:")
    print("1-添加商品 2-删除商品 3-查看清单 4-退出")
    choice = input("输入数字:")

    if choice == "1":
        item = input("请输入商品名称:")
        if item in shopping_list:
            print("该商品已在清单中")
        else:
            shopping_list.append(item)
            save_list(shopping_list)
            print(f"已添加:{item}")
        
    elif choice == "2":
        if not shopping_list:
            print("当前清单为空")
        else:
            item = input("请输入要删除的商品名称:")
            if item in shopping_list:
                shopping_list.remove(item)
                save_list(shopping_list)
                print(f"已删除{item}")
            else:
                print("清单里没有这个商品")
    elif choice == "3":
        if not shopping_list:
            print("清单为空")
        else:
            print("当前购物清单:")
            """ 此处也可为(更为简洁):
            for i,item in enumerate(shopping_list,1):
                print(f"{i}.{item}")"""
            for i in range(len(shopping_list)):
                print(f"{i+1}.{shopping_list[i]}")     
    elif choice == "4":
        print("再见!")
        break
    else:
        print("输入无效，请重试")
            
