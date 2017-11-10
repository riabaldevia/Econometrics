
import pyfolio as pf
stock_rets = pf.utils.get_symbol_rets('WTW')
pf.create_returns_tear_sheet(stock_rets, live_start_date='2015-1-1')


Entire data start date: 2001-11-16
Entire data end date: 2017-11-07
In-sample months: 157
Out-of-sample months: 34
                        All In-sample Out-of-sample
Annual return          4.4%     -0.3%         28.6%
Cumulative returns    98.1%     -3.3%        104.8%
Annual volatility     54.4%     38.3%         99.1%
Sharpe ratio           0.32      0.18          0.67
Calmar ratio           0.05     -0.00          0.34
Stability              0.19      0.00          0.44
Max drawdown         -95.4%    -76.8%        -84.8%
Omega ratio            1.08      1.04          1.19
Sortino ratio          0.55      0.27          1.33
Skew                   7.84      1.21          6.86
Kurtosis             240.08     52.81        114.12
Tail ratio             1.04      1.04          1.10
Daily value at risk   -6.8%     -4.8%        -12.2%
Alpha                  0.11      0.01          0.49
Beta                   0.75      0.68          1.60

Worst drawdown periods Net drawdown in %  Peak date Valley date Recovery date  \
0                                  95.44 2011-05-26  2015-07-09           NaT   
1                                  70.41 2007-10-04  2009-03-03    2011-02-17   
2                                  34.35 2002-10-24  2004-05-13    2005-06-16   
3                                  33.59 2005-08-03  2006-08-11    2007-08-08   
4                                  16.13 2002-08-20  2002-09-24    2002-10-16   

Worst drawdown periods Duration  
0                           NaN  
1                           881  
2                           691  
3                           526  
4                            42 


#Bayesian analysis

