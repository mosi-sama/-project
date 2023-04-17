# encoding:utf-8
import re
path = r"C:\Users\Hasee\Documents\mypython课件\chap07\07章.Python " \
       r"正则表达式与异常处理（含第5次作业参考代码+第6次作业要求）\实训报告06\案例@03-【实验7.1】电商商品关键数据提取 rawdata.txt"
path_date = r"C:\Users\Hasee\Documents\mypython课件\chap07\07章.Python " \
            r"正则表达式与异常处理（含第5次作业参考代码+第6次作业要求）\实训报告06\整合的数据.txt"
with open(file=path_date, mode='a', encoding='utf-8') as z:
    with open(file=path, mode='r', encoding='utf-8') as f:
        fr = f.readlines()
        for i in fr:
            pattern_sku = re.compile('data-sku="(\d+)"')
            sku = re.findall(pattern_sku, i)[0]
            pattern_price = re.compile('<em>￥</em><i>(.+?)</i>')
            price = re.findall(pattern_price, i)[0]
            pattern_promo_words = re.compile('<em>(.+?)</em>')
            promo_words = re.findall(pattern_promo_words, i)[1]
            pattern_peizhi = re.compile('<span class="attr"><b>(.+?)</b>')
            peizhi = re.findall(pattern_peizhi, i)
            pattern_data_tips0 = re.compile('data-tips="京东自营，品质保障">(.+?)</i>')
            pattern_data_tips1 = re.compile('style="border-color:#4d88ff;color:#4d88ff;">(.+?)</i>')
            pattern_data_tips2 = re.compile('data-tips="该商品是当季新品">(.+?)</i>')
            data_tips0 = re.findall(pattern_data_tips0, i)
            data_tips1 = re.findall(pattern_data_tips1, i)
            data_tips2 = re.findall(pattern_data_tips2, i)
            x = [str(sku), str(price), str(promo_words), str(peizhi), str(data_tips0),
                 str(data_tips1), str(data_tips2)]
            z.write(str(x) + '\n')