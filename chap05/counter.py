#encoding:utf-8
'''
账户类：
属性：
    账号
    密码
    明细
    金额
方法：
    打印明细方法
    登记收入方法
    登记支出方法
    退出账户方法
'''

class Counter():
    def __init__(self, username, password):             # 用户注册时，会提供账号、密码
        self.username = username
        self.password = password
        self.detail_list = []
        self.total = 10000
        self.n = 0
        self.menu = self.username + '''，欢迎您！
--------------------家庭收支记账软件--------------------

                    1 收支明细

                    2 登记收入

                    3 登记支出

                    4 退出账户

--------------------------------------------------------'''

    def detail_print(self):
        if len(self.detail_list) == 0:                      # len(x) 计算 x 的长度
            print('您的账户还没有明细，请登记收入或支出。')
        else:
            print('--------------当前收支明细记录--------------')
            for i in self.detail_list:
                s = str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2]) + '\t' + str(i[3]) + '\t' + str(i[4])
                print(s)
            print('-----------------------------------------')

    def income_input(self):
        income = input("请输入收入金额：")
        remark = input("请输入收入说明：")
        print("成功登记收入")
        self.total = self.total + float(income)
        self.n = self.n + 1
        subdetail = [self.n, '收入', self.total, income, remark]
        self.detail_list.append(subdetail)

    def outcome_input(self):
        outcome = input("请输入支出金额：")
        remark = input("请输入支出说明：")
        print("成功登记支出")
        self.total = self.total - float(outcome)
        self.n = self.n + 1
        subdetail = [self.n, '支出', self.total, outcome, remark]
        self.detail_list.append(subdetail)

    def sys_quit(self):
        print('退出账号，欢迎下次继续使用！')

    def start(self):
        while True:
            print(self.menu)
            fun = input('请输入功能(选择1-4)：')
            if fun in ['1', '2', '3', '4']:
                if fun == '1':
                    self.detail_print()
                elif fun == '2':
                    self.income_input()
                elif fun == '3':
                    self.outcome_input()
                elif fun == '4':
                    self.sys_quit()
                    break
            else:
                print('您输入的功能代码有误，请重新输入！！！')



if __name__ == '__main__':              # 如果是在当前代码文件启动的话，就运行以下代码
    username = 'root'
    password = 'root'
    c = Counter(username, password)             # 按构造函数 def __init__(self, username, password) 要求输入 账号和密码，创建账户对象
    c.start()
    c.username
