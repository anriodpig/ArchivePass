# password merge tool
# 增量式添加并去重
# 以src.txt为基准，合并add.txt中的非重复项输出到out.txt
# 编码：UTF-8


import time

if __name__ == '__main__':

    s = open("src.txt", mode='r', encoding='utf-8')
    a = open("add.txt", mode='r', encoding='utf-8')

    sl = s.readlines()
    al = a.readlines()

    s.close()
    a.close()

    run = 0
    dup = 0
    # 增量添加
    for i in al:
        if i not in sl:
            sl.append(i)
            run = run + 1
            if run % 500 == 0:
                print('PASS-1 | Added: ' + str(run) + '  Dup: ' + str(dup))
        else:
            dup = dup + 1
            # print(dup)
    fl = []

    run = 0
    dup = 0

    # 去重添加
    for j in sl:
        if j not in fl:
            fl.append(j)
            run = run + 1
            if run % 500 == 0:
                print('PASS-2 | Processed: ' + str(run) + '  Dup: ' + str(dup))
        else:
            dup = dup + 1
            # print(dup)

    fp = open("out.txt", mode="w", encoding='utf-8')

    fp.writelines(fl)
    fp.close()

    print("Done")
