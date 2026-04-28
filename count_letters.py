def count_letters(s):
    # 创建一个空字典
    result = {}
    # 遍历字符串中的每一个字符
    for ch in s:
        # 只处理字母（用ch.isalpha() 判断）
        if ch.isalpha():
            # 转换为小写
            ch_low = ch.lower()
            # 如果字典中已有该字母，计数+1；否则设置为1
            result[ch_low] = result.get(ch_low,0) + 1
    return result

# 主程序
while True:
    text = input("请输入一个字符串（输入q退出）：")
    if text == "q":
        print("再见")
        break
    stats = count_letters(text)
    print(stats)
