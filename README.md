# 选股票系统
***
`使用的库`
python2.7，
numpy，
panda，
tushare  
`项目逻辑`   
  程序使用tushare爬去基本面数据  
  然后根据基本面数据去爬取沪深A股过去一年的历史行情 
  https://github.com/kevinpop/ChinaStockInformaticaChese/blob/master/image01.png  
  先获取沪深A股票的所有code代码 
  然后通过[ts.get_hist_data()](http://tushare.org/trading.html#id2)获取分列过去一年的历史行情  
  https://github.com/kevinpop/ChinaStockInformaticaChese/blob/master/image02.png  
`项目文件说明`   
  [主要文件文件Demo.py](Demo.py)  
`外部API来源`  
  [Tushare来源](http://tushare.org "悬停显示")  
[回到顶部](#readme)	 
