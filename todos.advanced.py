import json

FILE_NAME = "todos.json"

def load():
    try:
        with open(FILE_NAME,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(todos):
    with open(FILE_NAME,"w",encoding="utf-8") as f:
        json.dump(todos,f,indent=2,ensure_ascii=False)

def show(todos):
    if not todos:
        print("空")
    else:
        for i,t in enumerate(todos,1):
            print(f"{i}.{t['text']}|优先级：{t['priority']}|截止日期：{t['due']}")
todos = load()
while True:
    print("\n1-添加 2-删除 3-查看 4-退出")
    c = input(">")
    if c == "1":
        text = input("内容:")
        priority = input("优先级(高/中/低):")
        due = input("截止日期（YYYY-MM-DD）:")
        todos.append({"text":text,"priority":priority,"due":due})
        save(todos)
        
    elif c == "2":
        show(todos)
        if todos:
            try:
                idx = int(input("编号:"))
                if 1 <= idx <= len(todos):
                    todos.pop(idx-1)
                    save(todos)
            except:pass
    elif c == "3":
        show(todos)
    else:
        break
                
                
