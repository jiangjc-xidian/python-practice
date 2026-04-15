import os

TODO_FILE = "todo.txt" #保存文件名称

def load_todos():
    """从文件加载待办事项，返回列表"""
    todos = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE,"r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    todos.append(line)
    return todos

def save_todos(todos):
    """保存待办事项文件"""
    with open(TODO_FILE,"w",encoding="utf-8") as f:
        for item in todos:
            f.write(item + "\n")

def show_todos(todos):
    """显示所有待办事项"""
    if not todos:
        print("暂无待办事项。")
    else:
        for i, item in enumerate(todos,start=1):
            print(f"{i}.{item}")

def main():
    todos = load_todos()
    while True:
        print("\n请选择操作:")
        print("1-添加  2-查看  3-删除  4-退出")
        choice = input(">")

        if choice == "1":
            new_item = input("请输入新事项:")
            todos.append(new_item)
            save_todos(todos)
            print("已添加!")
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            show_todos(todos)
            if todos:
                try:
                    idx = int(input("请输入要删除的编号:"))
                    if 1 <= idx <= len(todos):
                        removed = todos.pop(idx-1)
                        save_todos(todos)
                        print(f"已删除{removed}")
                    else:
                        print("编号超出范围")
                except ValueError:
                    print("请输入数字编号")
        elif choice == "4":
            print("再见！事项已保存。")
            break
        else:
            print("无效选择，请重新输出")
        
main()

