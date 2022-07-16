import pandas as pd


def stooq(code,step):
    url = 'https://stooq.com/q/a2/d/?s='+code+'&i='+step
    df=pd.read_csv(url,skiprows=1,sep=',',names=['date', 'e', 'open', 'high', 'low', 'close', 'volumen', 'volumen3m', 'flag'])
    
    df.drop('e', inplace=True, axis=1)
    df['date']= pd.to_datetime(df['date'],format='%Y%m%d')
    
    return(df)


def stooq_pln(code,curr):
    
    df = stooq(code)
    
    fx = stooq((curr+'pln').lower())
    
    result = df.set_index('date').join(fx.set_index('date'), rsuffix='_fx')
    
    result['close_pln']=result['close']*result['close_fx']
    
    return result