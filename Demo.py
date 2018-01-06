#先抓取基本行情数据
import tushare as ts
import pandas as pd
import numpy as py

df = ts.get_stock_basics()
df.to_csv("StockNumberBasics.cvs")
DemoList = pd.read_cvs(“StockNumberBasics.cvs”)
display(DemoList.head())

#解决code项目前面0缺失
def demo(i):
    n = len(str(i))
    if n == 6:
        pass
    else:
        if n == 5:
            i = "0" + i
        else:
            if n == 4:
                i = "00"+i
            else:
                if n == 3:
                    i = "000" + i
                else:
                    if n == 2:
                        i = "0000" + i
                    else:
                        pass
    return i
#需要对错误信息进行处理
for i in DemoList.code:
    st = ts.get_hist_data(str(demo(str(i))))
    st.to_csv("Data/"+str(demo(str(i)))+".csv")
