# 一些公用转换方法
import datetime, time

# 数据库坐标转换成字符串格式
def intToCoordinate(integer_data):
    string_data = str(integer_data)
    if(len(string_data) > 6):
        string_data = string_data[:-6] + '.' + string_data[-6:]
    elif(len(string_data) == 6):
        string_data = '0.' + string_data
    elif(len(string_data) == 5):
        string_data = '0.0' + string_data
    elif(len(string_data) == 4):
        string_data = '0.00' + string_data
    elif(len(string_data) ==3):
        string_data = '0.000' + string_data
    
    return string_data

# 坐标转换成数据库格式
def CoordinateToInt(coordinate):
    str_data = coordinate.replace('.', '')
    float_data = coordinate.split('.')[1]
    if(len(float_data) == 5):
        str_data = str_data + '0'
    elif(len(float_data) == 4):
        str_data = str_data + '00'
    elif(len(str_data) == 3):
        str_data = str_data + '000'
    elif(len(str_data) == 2):
        str_data = str_data + '0000'
    elif(len(str_data) == 1):
        str_data = str_data + '00000'
    else:
        pass
    return int(str_data)

# 时间戳转正常时间格式
def timestampToDatetime(timestamp_val, format):
    # timestamp_val = int(timestamp_val)
    dateArray = datetime.datetime.utcfromtimestamp(timestamp_val)
    try:
        if(format == 'sec'):
            timestr = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        elif(format == 'min'):
            timestr = dateArray.strftime("%Y-%m-%d %H:%M")
        elif(format == 'hour'):
            timestr = dateArray.strftime("%Y-%m-%d %H")
        elif(format == 'date'):
            timestr = dateArray.strftime("%Y-%m-%d")
        return timestr
    except UnboundLocalError:
        print('转换失败，格式错误, 输出格式应为date,hour,min,sec')
        return timestamp_val