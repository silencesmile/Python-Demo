'''
查找最长回文字符串
（回文字符串形式为：aba， abcba）如果没有则返回None

思路：
先找最小，然后向外扩散
'''


def func(str):
    list = []
    for j in range(len(str) - 1):
        # 设置每次查询步长
        num = 1
        if j > 0 and j + 1 < len(str):
            if str[j - num] == str[j + num]:
                # 判断最小回文字符串
                newStr = str[j - num] + str[j] + str[j + num]

                # 已找到最小，向外扩散一层
                num += 1
                while j-num > 0 and j + num < len(str):
                        if str[j - num] == str[j + num]:
                            newStr = str[j - num] + newStr + str[j + num]
                            num += 1
                        else:
                            break

                list.append(newStr)

    # 查到回文字符串，判定最长的
    if len(list) > 0:
        maxStr = list[0]
        for index in range(len(list) -1):
            if len(list[index]) > len(maxStr):
                maxStr = list[index]

        # 存在多个相同长度的回文字符串
        newList = []
        for temp in list:
            if len(temp) == len(maxStr):
                newList.append(temp)
        return newList
    else:
        return None


def main():
    list = func("cbdb")
    print(list)

if __name__ == '__main__':
    main()



