# encoding:utf-8
# noinspection PyUnboundLocalVariable
class zhanghao():
    yonghu_biao = []
    mima_biao = []
    def __init__(self):
        self.username = None  # 用户名
        self.password = None  # 用户密码
        self.jine = None  # 初始金额
        # self.yonghu_biao = []  # 用户记录
        # self.mima_biao = []  # 密码记录
        self.jine_biao = []  # 初始金额记录
        self.jilu_biao = []  # 收支记录
        self.yonghu_jilu_biao = []
        self.yonghu_jilu_biao2 = []#
        self.n = 0  # 初始记录序号
        self.x = 0
        self.menu01 = '''
        --------------------家庭收支记账软件-----------------------
                            1 注册账号
                            2 登录账号
                            3 退出系统
        --------------------------------------------------------
        '''
        self.menu02 = '''欢迎您！
        --------------------家庭收支记账软件-----------------------
                            1 收支明细
                            2 登记收入
                            3 登记支出
                            4 退出账户
        --------------------------------------------------------
        '''

    def username01(self, username):
        self.username = username

        zhanghao.yonghu_biao.append(self.username)

    def mm(self):
        global length_after
        length_after = len(zhanghao.mima_biao)
        while True:
            length_before = len(zhanghao.mima_biao)
            passwd = input('请输入密码（仅支持0到10个字节！）： ')
            if len(passwd) > 10:
                print('请重新输入！仅支持0到10个字节！')
            else:
                while True:
                    passwd01 = input('请再次输入密码： ')
                    if passwd01 == passwd:
                        self.password = passwd
                        zhanghao.mima_biao.append(self.password)
                        length_after = len(zhanghao.mima_biao)
                        print('密码确认完毕！')
                        break
                    else:
                        print('请重新输入！')
            if length_before < length_after:
                break

    def chujin(self):
        while True:
            try:
                jine = int(input("请输入一个整数："))
                self.jine = jine
                self.jine_biao.append(self.jine)
                print('输入成功！')
                print('成功注册!欢迎您的使用！')
                break
            except ValueError:
                print("输入无效，请重新输入一个整数。")

    def denlu(self):
        while True:
            name = input('输入用户名： ')
            try:
                zhanghao.yonghu_biao.index(name)
            except ValueError:
                print('您还没有注册，请使用功能1注册！')
            if name in zhanghao.yonghu_biao:
                xx = zhanghao.yonghu_biao.index(name)
                passwd = input('请输入密码： ')
                if passwd == zhanghao.mima_biao[xx]:
                    print('登陆成功！')
                    break
                else:
                    print('账号或者密码错误！请重新输入！')

    def liebiao(self):

        if len(self.jilu_biao) == 0:
            print("还没有记录哟！")
        else:
            while True:
                t = (self.username, self.n)
                o = self.yonghu_jilu_biao.index(t)
                h = self.yonghu_jilu_biao[o]
                if h == t:
                    o += 1
                    for i in self.yonghu_jilu_biao2[:o]:
                        print(i)
                    break


            # while True:
            #
            #     if self.yonghu_jilu_biao[self.x][0] == username:
            #         # o = self.yonghu_jilu_biao[self.x]
            #         # h = self.yonghu_jilu_biao.index(o)
            #         # z = self.yonghu_jilu_biao[h]
            #         # k = self.yonghu_jilu_biao2.append(str(z[1]))
            #         for i in k:
            #             print(i)
            #         try:
            #             self.yonghu_jilu_biao[self.x]
            #         except IndexError:
            #             break
            #         self.x = + 1
            #     else:
            #         self.x = + 1
            #
            #     try:
            #         self.yonghu_jilu_biao[self.x]
            #     except IndexError:
            #         break
                # print('--------------当前收支明细记录--------------')
                # for i in o[1]:
                #     s = str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2]) + '\t' + str(i[3]) + '\t' + str(i[4])
                #     print(s)
                # print('-----------------------------------------')

    def shouru(self):
        income = input("请输入收入金额：")
        remark = input("请输入收入说明：")
        print("成功登记收入")
        self.jine = self.jine + float(income)
        self.n = self.n + 1
        subdetail = [self.n, '收入', self.jine, income, remark]
        self.jilu_biao.append(subdetail)
        t = (self.username, self.n)
        self.yonghu_jilu_biao.append(t)
        self.yonghu_jilu_biao2.append(subdetail)

    def zhicu(self):
        outcome = input("请输入支出金额：")
        remark = input("请输入支出说明：")
        print("成功登记支出")
        self.jine = self.jine - float(outcome)
        self.n = self.n + 1
        subdetail = [self.n, '支出', self.jine, outcome, remark]
        self.jilu_biao.append(subdetail)
        t = (self.username, self.n)
        self.yonghu_jilu_biao.append(t)
        self.yonghu_jilu_biao2.append(subdetail)

    def sys_quit(self):
        print('谢谢使用。')
