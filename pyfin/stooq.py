import pandas as pd


def stooq(code,step):
    url = 'https://stooq.com/q/a2/d/?s='+code+'&i='+step
    df=pd.read_csv(url,skiprows=1,sep=',',names=['date', 'e', 'open', 'high', 'low', 'close', 'volumen', 'volumen3m', 'flag'])
    
    df.drop('e', inplace=True, axis=1)
    df['date']= pd.to_datetime(df['date'],format='%Y%m%d')
    
    return(df)