"""
邢不行-股票量化入门训练营
邢不行微信：xbx9585
Day2：如何获取股票的实时价格
"""
import pandas as pd
from urllib.request import urlopen  # python自带爬虫库


# =====神奇的网址
# 返回一个股票的数据：http://hq.sinajs.cn/list=sz000001，修改股票代码。交易时间获取数据。
# 返回一串股票的数据：http://hq.sinajs.cn/list=sh600000,sz000002,sz300001
# 正常网址：https://finance.sina.com.cn/realstock/company/sh600000/nc.shtml
# 从各类财经网站爬去数据，需要一定的爬虫知识


# =====构建网址
# 正常股票：sh600000 sz000002，退市股票：sh600002 sz000003、停牌股票、除权股票、上市新股、
url = "http://hq.sinajs.cn/list=sh601985,sz002190,sz002351,sh601633,sz002271,sh600036,sh603160,sz003816,sz002230,sz000333"  # 注意是英文逗号


# =====抓取数据
# 需要电脑联网
content = urlopen(url).read().decode('gbk')  # 使用python自带的库，从网络上获取信息


# =====将数据转换成DataFrame
data_line = content.strip().split('\n')  # 去掉文本前后的空格、回车等。每行是一个股票的数据
data_line = [i.replace('var hq_str_', '').split(',') for i in data_line]
df = pd.DataFrame(data_line, dtype='float')


# =====对DataFrame进行整理
df[0] = df[0].str.split('="')
df['stock_code'] = df[0].str[0].str.strip()
df['stock_name'] = df[0].str[-1].str.strip()
df['candle_end_time'] = pd.to_datetime(df[30] + ' ' + df[31])  # 股票市场的K线，是普遍以当跟K线结束时间来命名的

rename_dict = {1: 'open', 2: 'pre_close', 3: 'close', 4: 'high', 5: 'low', 6: 'buy1', 7: 'sell1',
                8: 'amount', 9: 'volume', 32: 'status'}  # 自己去对比数据，会有新的返现
df.rename(columns=rename_dict, inplace=True)
df['status'] = df['status'].str.strip('";')
df = df[['stock_code', 'stock_name', 'candle_end_time', 'open', 'high', 'low', 'close', 'pre_close', 'amount', 'volume',
          'buy1', 'sell1', 'status']]
print(df)


# =====保存数据
df.to_csv('liu_stock_data.csv', index=False)


# =====打卡作业
# 任意选取10只股票，获取其最新数据，将数据保存到csv文件，发送到课程群。发送“day2作业打卡”并@助教


# =====打卡福利
# 赠送一份完整股票历史数据



