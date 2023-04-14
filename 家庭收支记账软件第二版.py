name = {}                           # 用户名
jine = {}                           # 金额
qq = {}                             #
n1 = {}
n2 = {}
zz = {}
q = []
qqq = {}
chujin = ''
menu1 = '''
家庭收支记账软件
1，注册
2，登陆
0，退出
'''
while True:
    print(menu1)
    x = input('请输入功能：')
    if x == '1':
        print('开始注册')
        user1 = input('请输入名称： ')
        if user1 in name:
            print('用户已存在！')
        else:
            passwd1 = input('请输入密码： ')
            # passwd1.lower()
            # print(0)
            # print(name)
            name[user1] = passwd1
            while True:
                chujin: str = input('请输入初始金额： ')
                if '0' < chujin < '99999999999999999999':
                    user1: chujin
                    jine[user1] = chujin
                    n = 0
                    n1[user1] = n
                    print('注册成功！')
                    break
                else:
                    print('请重新输入')
                    continue
                #     chujin: str = input('请输入初始金额： ')
                #     chujin = chujin
    elif x == '2':
        user2 = input('请输入名称： ')
        passwd2 = input('请输入密码： ')
        # passwd2.lower()
        # print(b)
        # user0 = {user2: passwd2}
        if user2 in name:
            tt = name[user2]
            if tt == passwd2:
                print('登陆成功！欢迎您的使用。')
                menu2 = '''
                家庭收支记账软件
                1. 收支明细
                2. 登记收入
                3. 登记支出
                0. 退出系统
                '''
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
                            jj = jine[user2]
                            income = input('金额：')
                            remake = input('说明：')
                            if '0' < income < '99999999999999999999999':
                                y = float(jj) + float(income)
                                n = n1[user2] + 1  # 序号
                                n1[user2] = n
                                n2[user2] = n
                                jine[user2] = y
                                z = [n, '收入', y, income, remake]  # 序号、收支标记、账户金额、收支金额、说明
                                print('序号', n)
                                q.append(z)
                                nn = user2 + str(n)
                                qq[nn] = q
                                print("-----------------------收入明细---------------------------")
                                for i in qq[nn]:
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
                    elif x == "3":
                        # print("选择了3")
                        while True:
                            jj = jine[user2]
                            outcome = input('金额：')
                            remake = input('说明：')
                            if '0' < outcome < '99999999999999999999999':
                                y = float(jj) - float(outcome)
                                n = n1[user2] + 1  # 序号
                                n1[user2] = n
                                n2[user2] = n
                                jine[user2] = y
                                z = [n, '支出', y, outcome, remake]  # 序号、收支标记、账户金额、收支金额、说明
                                print('序号', n)
                                q.append(z)
                                nn = user2 + str(n)
                                qq[nn] = q
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
                    elif x == "0":
                        print("谢谢使用！")
                        break
                    else:
                        print("请重新输入")
            elif tt != passwd2:
                print('密码错误！')
        else:
            print('您还没有注册！')
    elif x == '0':
        print('感谢您的使用！')
        break
    else:
        print('请重新输入！')