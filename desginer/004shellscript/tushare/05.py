# -*- coding:utf-8 -*-
# Author: ycg000344
# 基本面数据

from sqlalchemy import create_engine
import tushare as ts

engine = create_engine('mysql://admin:Admin123!@www.wm.org:3306/stockquotation?charset=UTF8')

# 501
# 股票列表
# code,代码
# name,名称
# industry,所属行业
# area,地区
# pe,市盈率
# outstanding,流通股本(亿)
# totals,总股本(亿)
# totalAssets,总资产(万)
# liquidAssets,流动资产
# fixedAssets,固定资产
# reserved,公积金
# reservedPerShare,每股公积金
# esp,每股收益
# bvps,每股净资
# pb,市净率
# timeToMarket,上市日期
# undp,未分利润
# perundp, 每股未分配
# rev,收入同比(%)
# profit,利润同比(%)
# gpr,毛利率(%)
# npr,净利润率(%)
# holders,股东人数
df = ts.get_stock_basics()
df.to_sql('t_stock_basics',engine)

#502
# 业绩报告（主表）
# 按年度、季度获取业绩报表数据。
# code,代码
# name,名称
# esp,每股收益
# eps_yoy,每股收益同比(%)
# bvps,每股净资产
# roe,净资产收益率(%)
# epcf,每股现金流量(元)
# net_profits,净利润(万元)
# profits_yoy,净利润同比(%)
# distrib,分配方案
# report_date,发布日期
# 获取2017年第4季度的业绩报表数据
df = ts.get_report_data(2017,4)
df.to_sql('t_report_data',engine)

# 503
# 盈利能力
# code,代码
# name,名称
# roe,净资产收益率(%)
# net_profit_ratio,净利率(%)
# gross_profit_rate,毛利率(%)
# net_profits,净利润(万元)
# esp,每股收益
# business_income,营业收入(百万元)
# bips,每股主营业务收入(元)
# 获取2017年第4季度的业绩报表数据
df = ts.get_profit_data(2017,4)
df.to_sql('t_profit_data',engine)

# 504
# 营运能力
# code,代码
# name,名称
# arturnover,应收账款周转率(次)
# arturndays,应收账款周转天数(天)
# inventory_turnover,存货周转率(次)
# inventory_days,存货周转天数(天)
# currentasset_turnover,流动资产周转率(次)
# currentasset_days,流动资产周转天数(天)
# 获取2017年第4季度的业绩报表数据
df = ts.get_operation_data(2017,4)
df.to_sql('t_operation_data',engine)

# 505
# 成长能力
# code,代码
# name,名称
# mbrg,主营业务收入增长率(%)
# nprg,净利润增长率(%)
# nav,净资产增长率
# targ,总资产增长率
# epsg,每股收益增长率
# seg,股东权益增长率
# 获取2017年第4季度的业绩报表数据
df = ts.get_growth_data(2017,4)
df.to_sql('t_growth_data',engine)

# 506
# 偿债能力
# code,代码
# name,名称
# currentratio,流动比率
# quickratio,速动比率
# cashratio,现金比率
# icratio,利息支付倍数
# sheqratio,股东权益比率
# adratio,股东权益增长率
# 获取2017年第4季度的业绩报表数据
df = ts.get_debtpaying_data(2017,4)
df.to_sql('t_debtpaying_data',engine)

# 507
# 现金流量
# code,代码
# name,名称
# cf_sales,经营现金净流量对销售收入比率
# rateofreturn,资产的经营现金流量回报率
# cf_nm,经营现金净流量与净利润的比率
# cf_liabilities,经营现金净流量对负债比率
# cashflowratio,现金流量比率
# 获取2017年第4季度的业绩报表数据
df = ts.get_cashflow_data(2017,4)
df.to_sql('t_cashflow_data',engine)