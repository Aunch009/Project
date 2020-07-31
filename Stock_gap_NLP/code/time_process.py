import pickle
import pandas as pd
df = pd.read_pickle('D:\Program_code\python\Code_test\stock_gap_NLP\Pickle\PTT_2020-01-04.pkl')
print(df)
for x in df['Date']:
    if x=='2019-01-02':
        print(x)