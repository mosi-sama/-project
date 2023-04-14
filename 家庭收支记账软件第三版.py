from 家庭收支记账软件类方法配置 import zhanghao
ttk = zhanghao()
while True:
    print(ttk.menu01)
    x = input('请输入功能： ')
    if x in ['1', '2', '3']:
        if x == '1':
            u = input('请输入名字： ')
            ttk.username01(u)
            u = zhanghao()
            u.mm()
            u.chujin()
        if x == '2':
            try:
                # noinspection PyUnboundLocalVariable
                u.denlu()
            except NameError:
                print('您还没有注册，请使用功能1注册！')
                continue
            if True:
                while True:
                    print(u.menu02)
                    x = input('请输入功能： ')
                    if x in ['1', '2', '3', '4']:
                        if x == '1':
                            u.liebiao()
                        if x == '2':
                            u.shouru()
                        if x == '3':
                            u.zhicu()
                        if x == '4':
                            u.sys_quit()
                            break
                    else:
                        print('请重新输入！')
        if x == '3':
            u.sys_quit()
            break
    else:
        print('其他功能还没有开发哦！请重新输入。')