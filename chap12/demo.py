# encoding:utf-8

'''
需求：
    最近一周的气温变化
    星期：['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    气温：[30，30, 31, 30, 29, 31, 33]
'''

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

# 定义画布
fig, ans = plt.subplots(nrows=2, ncols=2, figsize=(15, 9))

weekday = np.array(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'])
timp = np.array([30, 30, 31, 30, 29, 31, 33])

shijian = np.array([10, 15, 6, 5, 60, 2, 2])
explode = (0, 0, 0, 0, 0.1, 0, 0)

# 折线图
ans[0, 0].plot(weekday, timp)

ans[0, 0].set_title("气温绘制折线图", fontsize=20)
# ans[0, 0].set_xlabel('日期', fontsize=15)
ans[0, 0].set_ylabel('气温', fontsize=15)
ans[0, 0].tick_params(axis='both', labelsize=10)

# plt.show()

# 散点图
ans[0, 1].scatter(weekday, timp)

ans[0, 1].set_title("气温绘制散点图", fontsize=20)
# ans[0, 1].set_xlabel('日期', fontsize=15)
ans[0, 1].set_ylabel('气温变化', fontsize=15)
ans[0, 1].tick_params(axis='both', which='major', labelsize=10)

# plt.show()

# 直方图
ans[1, 0].bar(weekday, timp)

ans[1, 0].set_title("气温绘制直方图", fontsize=20)
# ans[1, 0].set_xlabel('日期', fontsize=15)
ans[1, 0].set_ylabel('气温变化', fontsize=15)

# plt.show()

# 饼图
ans[1, 1].pie(shijian, explode=explode, labels=weekday, autopct='%1.1f%%',
              startangle=150, textprops={'fontsize': 10})

ans[1, 1].set_title("占用的时间", fontsize=20)

# plt.show()

# fig.tight_layout()

plt.show()