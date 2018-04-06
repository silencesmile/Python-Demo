# 输入一个字符串 查找该字符串内的最长回文字符串（回文字符串形式为：aba， abcba）如果没有则返回None
# 例如输入'adaffcgasdabcbaxx' 其最大回文字符串为abcba

'''
思路：根据回文字符串特性  必为单数
将字符串进行截取 3，5，7.。。  判断是否为回文字符串

'''


def func(String):
    list1 = []
    index = 0
    while index < len(String):
        j = 3
        while j <= len(String)-index:
            xx_String = String[index:j+index]
            j += 2
            m = 0
            while m < len(xx_String) // 2:
                if xx_String[m] != xx_String[len(xx_String) - m - 1]:
                    break
                m += 1
            else:
                dict = {}
                dict['name'] = xx_String
                dict['len'] = len(xx_String)
                list1.append(dict)
        index += 1

    if list1:
        list1.sort(key=lambda x : x['len'])
        for x in reversed(list1):
            if x['len'] < list1[len(list1)-1]['len']:
                list1.remove(x)
        return list1
    else:
        return False

def main():
    String = 'a35'
    ret = func(String)
    if ret:
        if len(ret) > 1:
            print('有多个最长回文字符串')
            for x in ret:
                print('字符串%s的最长回文字符串为: ' % String, x['name'], '  长度为: ', x['len'])
        else:
            for x in ret:
                print('字符串%s的最长回文字符串为: ' % String, x['name'], '  长度为: ', x['len'])
    else:
        print('没有回文字符串')



if __name__ == '__main__':
    main()