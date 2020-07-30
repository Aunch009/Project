import pandas as pd
import glob
import os

path = r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\stock_link' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(frame)
frame.drop(['Unnamed: 0'], inplace=True, axis=1)
df = frame.drop_duplicates()
print(df)
# df.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')

if os.path.exists('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv'):
    os.remove('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')  
    df.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')
else: 
    df.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')
    
    


# frame.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combineall_2019-12-23.csv')