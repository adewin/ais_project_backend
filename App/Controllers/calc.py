import numpy as np
from sklearn.cluster import DBSCAN
from math import *
import json


# 坐标字符串转换为ndarray数组
def get_data(point_str):
    points = point_str.split(';')
    points_list = []
    for point in points:
        point_x = float(point.split(',')[0])
        point_y = float(point.split(',')[1])
        point_list = [point_x, point_y]
        points_list.append(point_list)
    points_arr = np.array(points_list)
    return points_arr

# 距离函数
def get_distance(array_1, array_2):
    lon_a = array_1[0]
    lat_a = array_1[1]
    lon_b = array_2[0]
    lat_b = array_2[1]
    radlat1 = radians(lat_a)
    radlat2 = radians(lat_b)
    a = radlat1 - radlat2
    b = radians(lon_a) - radians(lon_b)
    s = 2 * asin(sqrt(pow(sin(a/2),2) + cos(radlat1) * cos(radlat2)*pow(sin(b/2),2)))
    earth_radius = 6378137
    s = s * earth_radius
    return s

# 计算dbscan
# 输入坐标数组，搜索范围， 最小样本
# 输出坐标点的簇分类（json格式）
def dbscan_calc(str, dis, min_points):
    points = str.split(';')
    points_list = []
    for point in points:
        point_x = float(point.split(',')[0])
        point_y = float(point.split(',')[1])
        point_list = [point_x, point_y]
        point_dict = {'lnglat': point_list }
        points_list.append(point_dict)

    data = get_data(str)
    dbscan = DBSCAN(eps=dis, min_samples=min_points, metric=get_distance).fit(data)
    value_list = dbscan.labels_.tolist()
    for point in points_list:
        index = points_list.index(point)
        point['value'] = value_list[index]
    return json.dumps(points_list)

# 计算dbscan的第二种方式，输出结果方便展示在highcharts图上
# 输入坐标数组，搜索范围， 最小样本
# 输出结果为按簇的value值分类的坐标点的集合（json格式）
def dbscan_calc2(str, dis, min_points):
    points = str.split(';')
    points_list = []
    for point in points:
        point_x = float(point.split(',')[0])
        point_y = float(point.split(',')[1])
        point_list = [point_x, point_y]
        point_dict = {'lnglat': point_list }
        points_list.append(point_dict)

    data = get_data(str)
    dbscan = DBSCAN(eps=dis, min_samples=min_points, metric=get_distance).fit(data)
    value_list = dbscan.labels_.tolist()
    value_set = list(set(value_list)) # value值的集合

    for point in points_list:
        index = points_list.index(point)
        point['value'] = value_list[index]
    # 将points_list 转换成 points_value_list
    # 按value划分坐标集合 [{'value': 0, lnglats:[[121.725004, 39.01172],[121.718138, 38.987173]...]}]
    points_value_list = []
    for value in value_set: #遍历value值
        points_value_dict = {} 
        points_value_dict = {'value': value}  #value——point字典添加value值
        lnglats_list = []
        for point in points_list:
            if(point['value'] == value):
                lnglats_list.append(point['lnglat'])
            points_value_dict['lnglats'] = lnglats_list
        points_value_list.append(points_value_dict)
    return json.dumps(points_value_list)

# 计算DSBSCAN， 输出结果方便显示在vue-bmap组件中
#
def dbscan_bmap(data, eps, minpts):
    data_float_list = []  
    for i in data:
        data_float = [float(i[0]), float(i[1])]
        data_float_list.append(data_float)

    data_arr = np.array(data_float_list)
    dbscan = DBSCAN(eps=eps, min_samples=minpts, metric=get_distance).fit(data_arr)
    cluster_list = dbscan.labels_.tolist()  # 簇的list
    cluster_set =  list(set(cluster_list))  # 簇的set集合
    
    res_dict_list = []
    for i in data_float_list:
        res = {'lnglat': i, 'cluster': cluster_list[data_float_list.index(i)]}
        res_dict_list.append(res)
    # 整理为适用于bmap的格式
    points_value_list = []
    for i in cluster_set:
        bmap_dict = {'value': i}
        lnglat_list = []
        for j in res_dict_list:
            if(j['cluster'] == i):
                lnglat_list.append({'lng': str(j['lnglat'][0]), 'lat': str(j['lnglat'][1])})
            bmap_dict['lnglat'] = lnglat_list
        points_value_list.append(bmap_dict)

    return points_value_list

