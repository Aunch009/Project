import pandas as pd
import glob
import os

def twolist_to_list(lis):
    b = []
    for xs in lis:
        for x in xs:
            b.append(x)
    return b
def remove_save_file(p,path):
    if os.path.exists(path):
        os.remove(path)
        p.to_csv(path)
    else:
        p.to_csv(path)

Top10 = ['AOT','SCB','ADVANC','PTT','BDMS','CPALL']
sumall=[]
for tag in Top10:
    print(tag)
    path = r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Token_time' # use your path
    all_files = glob.glob(path +'\\time_'+ f'{tag}*.csv')

    li = []
    path1='D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Token_time\\sum_'+f'{tag}.csv'
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        # print(df.T)
        # d=df.sum(axis = 0, skipna = True)
        p = pd.DataFrame(df.sum(axis = 0, skipna = True)).T
        p['stock']=tag
        p.drop(['Unnamed: 0'], inplace=True, axis=1)
        # print(p)
        remove_save_file(p,path1)
        # if os.path.exists(path1):
        #     os.remove(path1)
        #     p.to_csv(path1)
        # else:
        #     p.to_csv(path1)
    sum_all_files = glob.glob(path +'\\sum_'+f'{tag}.csv')
    sumall.append(sum_all_files)
sumall_link=twolist_to_list(sumall)

print(sumall)
sum_li = []
for filename in sumall_link:
    df1 = pd.read_csv(filename, index_col=None, header=0)
    sum_li.append(df1)
frame = pd.concat(sum_li, axis=0, ignore_index=True)
frame.drop(['Unnamed: 0'], inplace=True, axis=1)
print(frame)

path2=r'D:\\Master_Degree\\Project\\Classification_report\\Classification_method_time.csv'
remove_save_file(frame,path2)

# if os.path.exists(path2):
#     os.remove(path2)
#     frame.to_csv(path2)
# else:
#     frame.to_csv(path2)
    # frame.drop_duplicates()
    # # print(df)
    # frame.to_csv(r'D:\\Master_Degree\\Project\\Classification_report\\'+f'{tag}_Classification_method.csv')

# if os.path.exists('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv'):
#     os.remove('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')  
#     df.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')
# else: 
#     df.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv')
    
    


# frame.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combineall_2019-12-23.csv')