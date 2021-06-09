# 导入相关库
import pandas as pd
import numpy as np
import math


# for循环处理文件
def processing_files():
    # 文件列表
    file_list = ['chemProdComnum', 'chemSaleComnum', 'class1Road', 'class2Road', 'classRoad',
                 'coalComnum', 'coalOutput', 'conArea', 'conOutput', 'ctrlCoalDeath', 'ctrlConDeath',
                 'ctrlFireDeath', 'ctrlIndotherlDeath', 'ctrlIndustryDeath', 'ctrlNoncoalDeath',
                 'ctrlTotalDeath', 'ctrlTrafficDeath', 'districtDiff', 'fireworksProdComnum',
                 'fireworksSaleComnum', 'gdp', 'heaveTractor', 'highRoad', 'indPop', 'lightTractor',
                 'majorAccident', 'motor', 'noncoalComnum', 'permPop', 'realCoalDeath', 'realConDeath',
                 'realFireDeath', 'realIndotherDeath', 'realIndustryDeath', 'realNoncoalDeath',
                 'realTotalDeath', 'realTrafficDeath', 'totalAccident', 'totalPop', 'totalRoad', 'totalUnit']
    data = pd.DataFrame(columns=['time', 'dis'] + file_list)
    # 处理文件
    for i in file_list:
        df = pd.read_csv('data\\' + i + '.csv',encoding="GB2312")
        data[i] = df.set_index('district').stack()

    # 处理索引
    time_list = []
    dis_list = []
    for item in data.index:
        dis_list.append(item[0])
        time_list.append(item[1])
    data['time'] = time_list
    data['dis'] = dis_list
    data.to_csv('数据.csv', encoding='utf-8_sig', index=False)


# 求平均差MAD
def MAD(list):
    list = np.array(list)
    ave = list.mean()
    mad = sum(np.abs(list - ave)) / len(list)
    return mad


# 倒置向量
def opposite(vector):
    vector = np.array(vector)
    return vector[::-1]


# 将向量由移k个位置
def shift(vector, k):
    vector = np.array(vector)
    return vector[k:]


# 创造20X10的矩阵
def create_mat():
    mat = np.arange(0, 200, 1)
    mat = mat.reshape(20, 10)
    return mat


# 斐波那契数列
def fibonacci(x):
    result_list = []
    a, b = 0, 1
    while x > 0:
        result_list.append(b)
        a, b = b, a + b
        x -= 1
    return result_list


# 正方形类
class Square(object):

    def __init__(self, location_x=0, location_y=0, length=1):
        self.location_x = location_x
        self.location_y = location_y
        self.length = length

    # 计算面积
    def calculated_area(self):
        return self.length*self.length

    # 计算两个正方形的距离
    def calculated_distance(self, x, y, length):
        distance = math.sqrt(math.pow(self.location_x-x, 2)+math.pow(self.location_y-y, 2))
        distance = distance - (self.length/2 + length/2)
        return distance

    def __str__(self):
        return 'this is a square'


if __name__ == '__main__':
    # 循环处理文件
    processing_files()
    # 临时向量
    a = [1, 2, 3, 4]
    print('MAD为：', MAD(a))
    print('转置后为：', opposite(a))
    print('右移两个元素后为', shift(a, 2))
    # 生成一个20X10的矩阵并将每一列倒置，然后每一列向右移3个元素
    mat = create_mat()
    new_mat = []
    for i in mat:
        i = opposite(i)
        i = shift(i, 3)
        new_mat.append(i)
    new_mat = np.mat(new_mat)
    print('新的矩阵为：')
    print(new_mat)
    # 项数太多内存会爆炸
    print('斐波那契数列前10项为：')
    print(fibonacci(10))
    b = Square()
    print(b)

















    # n = int(input('请输入'))
    # s = 0  # 总和
    # i = 0
    # flag = 0  # 标志位
    # while n > 0:
    #     i += 1
    #     if i % 2 != 0:
    #         if flag != 0:
    #             temp = -i
    #             flag = 0
    #         else:
    #             temp = i
    #             flag = 1
    #         s += temp
    #         n = n-1
    # print(s)
