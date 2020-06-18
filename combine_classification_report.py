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
# Top10 = ['CPALL']
# Top10 = ['ADVANC','DTAC','INTUCH','JAS','TRUE','CPALL','BBL','KBANK','KKP','KTB','SCB','TCAP','TISCO','TMB']
# Top10 = ['ADVANC','DTAC','INTUCH','JAS','TRUE','CPALL','BBL','KBANK','KKP','KTB','SCB','TCAP','TISCO','TMB','BANPU','BCP','BCPG','BGRIM','BPP','CKP','EA','EGCO','ESSO','GPSC','GULF','GUNKUL','IRPC','PTG','PTT','PTTEP','RATCH','SGP','SPRC','SUPER','TOP','TPIPP','TTW','BCH','BDMS','BH','CHG']
Top10 = ['BH','CPALL','INTUCH','KBANK','TOP']

# Top10 = ['AOT','SCB','ADVANC','PTT','BDMS','CPALL']
k=[]
for tag in Top10:
    print(tag)
    path = r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\classification_report_combine' # use your path

    all_files = glob.glob(path +'\\'+ f'{tag}_*.csv') # method: normal
    # all_files = glob.glob(path +'\\'+ f'stopword_{tag}_*.csv')# method:stopword
    
    k.append(all_files)
# path = r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\classification_report_combine' # use your path
# all_files = glob.glob(path +'\\'+ '*.csv')
# print(k)
p=twolist_to_list(k)
print(p)
print(len(p))
li = []

for filename in p:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
# print(li)
frame = pd.concat(li, axis=0, ignore_index=True)
frame.drop(['Unnamed: 0'], inplace=True, axis=1)
frame.drop_duplicates()
# print(frame)
path1=r'D:\\Master_Degree\\Project\\Classification_report\\Classification_method.csv'# method: normal
# path1=r'D:\\Master_Degree\\Project\\Classification_report\\stopword_Classification_method.csv'# method:stopword
remove_save_file(frame,path1)
    # print(df)
os.remove(r'D:\\Master_Degree\\Project\\Classification_report\\Classification_method.csv')
frame.to_csv(r'D:\\Master_Degree\\Project\\Classification_report\\Classification_method.csv')


    
    


# frame.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combineall_2019-12-23.csv')