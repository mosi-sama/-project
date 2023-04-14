#encoding:utf-8

'''
系统功能分析：
    1. 系统功能
        注册功能
        登录功能
        退出系统
    2. 账户功能
        打印明细
        登记收入
        登记支出
        退出账户

关键问题分析：
    操作不同账号，账号间各不影响
    要求：实现不同账号的创建与相关数据的存储及调用
    方案：创建 不同的账户对象
            创建不同账户对象的基础是什么？  类 （ 通过类创建对象 ）

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

from counter import Counter             # 从文件 counter.py 导入模块 Counter

# 实现系统功能（参考第 3 次作业）
main_menu = '''
--------------------家庭收支记账软件--------------------

                    1 注册账号

                    2 登录账号

                    3 退出系统

--------------------------------------------------------
'''
counter_list = []                               # 账户对象列表，用来存储账户对象，每个元素是 账户对象
while True:
    # 获取当前所有的 账号 和 密码
    username_list = [i.username for i in counter_list]   # 列表生成式 遍历账户对象列表，获取账号。 i 是 账户对象， i.username 访问对象属性 username
    password_list = [i.password for i in counter_list]
    print(main_menu)
    main_fun = input('请输入功能(选择1-3)：')
    if main_fun in ['1', '2', '3']:
        if main_fun == '1':
            # print('1 注册账号')
            username = input('请输入用户名称：')
            password = input('请输入用户密码：')
            # 需要注册账号
            '''
            判断账号是否存在
                如果账号存在，则提醒用户：账号已存在
                如果账号不存在，则创建新账户对象
            '''
            if username in username_list:                                   # 判断用户输入的账号 username 是否在 账号列表内
                print('账号已存在')
            else:
                counter_list.append(Counter(username, password))            # 将 新创建的账户对象 放入 账户对象列表
                print('已成功注册账号' + username)
        elif main_fun == '2':
            # print('2 登录账号')
            username = input('请输入用户名称：')
            password = input('请输入用户密码：')
            # 需启动账号
            '''
            判断 账号是否存在：
                如果账号存在，则判断密码是否正确
                    如果密码正确，则启动账号 .start()
                    如果密码不正确，则提醒用户： 账号或密码不正确
                如果账号不存在，则提醒用户：账号不存在
            
            关键点：确保 账号、密码、账户对象，处于同一个位置（下标）
            '''
            if username in username_list:                       # 注意：账号 和 密码 必须是同一个账户对象
                # 获取账号 在 账户对象列表 位置
                counter_index = username_list.index(username)       # username_list.index(username) 获取 username 在 username_list 的位置（下标）
                # password = password_list[counter_index]           # 获取到 username 相应位置的 密码
                if password == password_list[counter_index]:
                    counter_list[counter_index].start()             # 获取到 username 相应位置的 账户对象
                else:
                    print('账号或密码不正确')
            else:
                print('账号不存在')
        else:
            # print('3 退出系统')
            isquit = input('确认是否退出(Y/N)：')
            if isquit.lower() == 'y':               # isquit.lower()  将 isquit 转为 小写
                break
    else:
        print('您输入的功能代码有误，请重新输入！！！')


# 实现账户功能（思考如何通过实现 账户类 来创建不同的账号，从而实现操作）


























'''
实验步骤：
    1. 看本文件，理解软件实现的思路
    2. 看实验手册，理解软件实现的操作
    3. 回到本文件，编码实现
'''








