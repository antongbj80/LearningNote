import requests
import pandas as pd
import csv
data = pd.read_excel('代码库/比赛/附件1操作数据.xlsx')#导入地址的csv文件
data = data['籍贯']#选择地址列
lis = []
def gaode():
    for i in data:
        para = {
            'key':'be1ef3f1d58d5bf0c07cda2bd21a90aa',
            'address':i,
        }
        url = 'https://restapi.amap.com/v3/geocode/geo?'
        req = requests.get(url,para)
        req = req.json()
        if req['infocode']=='10000':
            w = req['geocodes'][0]['formatted_address']
            z = req['geocodes'][0]['location']
            print(w)
            print(z)
            d = (w, z)
        else:
            print('查询不到')
        lis.append(d)

    t = ['位置','经纬度']
    with open('数据经纬度位置.csv', 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(t)
        writer.writerows(lis)
if __name__ == '__main__':
    gaode()

