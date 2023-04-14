class weapon:
    def __init__(self, name):
        self.name = name
        self.atk = None
        self.dfe = None
        self.speed = None
        # print(str(self.name))
        # print("初始攻击力为" + str(self.atk))
        # print("初始防御力为" + str(self.dfe))
        # print("初始速度为" + str(self.speed))

    def name(self):
        print(str(self.name))

    def wuqiatktiaozheng1(self, wuqiatk):
        self.atk = wuqiatk
        print("武器攻击力调整为" + str(self.atk))

    def wuqidfetiaozheng1(self, wuqidfe):
        self.dfe = wuqidfe
        print("武器防御力调整为" + str(self.dfe))

    def wuqispeedtiaozheng1(self, wuqispeed):
        self.speed = wuqispeed
        print("武器速度调整为" + str(self.speed))

    def info(self):
        print(str(self.name))
        print("武器攻击力" + str(self.atk))
        print("武器防御力" + str(self.dfe))
        print("武器速度" + str(self.speed))

class level:
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.upexp = 100

    def jinyan(self, exp):
        self.exp += exp

    def uplevel(self):
        while self.exp >= self.upexp:
            self.exp -= self.upexp
            self.level += 1
            self.upexp = self.level * 100

    def levelinfo(self):
        print("等级：", self.level)
        print("经验：", self.exp)
        print("升级所需经验：", self.upexp)

class hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.weapon = None
        self.hp = 100
        self.atk = 0
        self.dfe = 0
        self.speed = 10
        print("你好，我是" + self.name)
        print("初始攻击力为" + str(self.atk))
        print("初始防御力为" + str(self.dfe))
        print("初始速度为" + str(self.speed))
        print("初始武器为" + str(self.weapon))

    def atktiaozheng(self, atk0):
        self.atk = atk0
        print("已调整为" + str(self.atk))

    def dfetiaozheng(self, dfe0):
        self.dfe = dfe0
        print("已调整为" + str(self.dfe))

    def speaktiaozheng(self, speed0):
        self.speed = speed0
        print("已调整为" + str(self.speed))

    def hptiaozheng(self, hp0):
        self.hp = hp0
        print("已调整为" + str(self.hp))

    def zhuangbeiwuqi(self, weapon):
        self.weapon = weapon
        self.atk += weapon.atk
        self.dfe += weapon.dfe
        self.speed += weapon.speed
        print("已装备武器： ", weapon.name)

    def info(self):
        print("人物名字： ", self.name)
        print("血量： ", self.hp)
        print("攻击力： ", self.atk)
        print("防御力： ", self.dfe)
        print("速度： ", self.speed)
        print("武器： ", self.weapon.name)


