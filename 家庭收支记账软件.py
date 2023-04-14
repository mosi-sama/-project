menu2 = '''
家庭收支记账软件
1. 收支明细
2. 登记收入
3. 登记支出
4. 退出系统
'''
chujin = 10000
n = 0
q = []
while True:
    print(menu2)
    x = input("选择功能：")
    if x == "1":
        # print("选择了1")
        print("-----------------------收入明细---------------------------")
        for i in q:
            s = (str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]))
            print(s)
        print("-----------------------收入明细---------------------------")

    elif x == "2":
        # print("选择了2")
        while True:
            income = input('金额：')
            remake = input('说明：')
            if '0' < income < '9999999999':
                y = chujin + float(income)
                n = n + 1  # 序号
                chujin = y
                z = [n, '收入', y, income, remake]  # 序号、收支标记、账户金额、收支金额、说明
                print('序号', n)
                q.append(z)
                print("-----------------------收入明细---------------------------")
                for i in q:
                    s = (str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]))
                    print(s)
                print("-----------------------收入明细---------------------------")
                while True:
                    ex = input('退出请按0，继续请按1：')
                    if ex == '0':
                        break
                    elif ex == '1':
                        print('序号', n+1)
                        break
                    else:
                        print("请重新输入")
                if ex == '0':
                    break
            else:
                print("请重新输入")

    elif x == "3":
        # print("选择了3")
        while True:
            outcome = input('金额：')
            remake = input('说明：')
            if '0' < outcome < '9999999999':
                y = chujin - float(outcome)
                n = n + 1  # 序号
                chujin = y
                z = [n, '支出', y, outcome, remake]  # 序号、收支标记、账户金额、收支金额、说明
                print('序号', n)
                q.append(z)
                print("-----------------------收入明细---------------------------")
                for i in q:
                    s = (str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]))
                    print(s)
                print("-----------------------收入明细---------------------------")
                while True:
                    ex = input('退出请按0，继续请按1：')
                    if ex == '0':
                        break
                    elif ex == '1':
                        print('序号', n + 1)
                        break
                    else:
                        print("请重新输入")
                if ex == '0':
                    break
            else:
                print("请重新输入")
    elif x == "4":
        print("谢谢使用！")
        break
    else:
        print("请重新输入")

