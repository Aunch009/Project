from open_url import *
from process_wording import *
from visual_data import *
from date_of_stock import *
from source_new import *
from stock_yahoo import *
import pickle

if __name__ == '__main__':
   
    dataframe = pd.read_csv(
        'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv'
    )
    
    Top10 = ['INTUCH']
    # Top10 = ['INTUCH','TOP','BH','CPALL','KBANK']
    
    
    for tag in Top10:
        print(tag)
        p, q, r, s, u, v, w = {}, {}, {}, {}, {}, {}, {}
        g1, g2, g3, g4, g6, g7, g8 = [], [], [], [], [], [], []
        for index, row in dataframe.iterrows():
            # print(tag,row['stock_name'])
            if tag == row['stock_name']:
                print(row['stock_name'], row['date'], row['link'])
                dm1 = row['date'].split()
                if dm1[1]=='Jan' or dm1[1]=='Feb'or dm1[1]=='Mar':
                    dm = date_month_2020(dm1[0], dm1[1])
                else:
                    dm = date_month_2019(dm1[0], dm1[1])
                dm = str(dm)
                print(dm)
                ### Date
                if row['source'] == 'www.bangkokbiznews.com':
                    #     # print(row['stock_name'],row['date'],row['link'])
                    g1.append([(dm, bangkokbiznews(row['link']))])
                    # g1.append([(dm, [row['link']])])
                elif row['source'] == 'www.hooninside.com':
                    g2.append([(dm, hooninside(row['link']))])
                    # g2.append([(dm, [row['link']])])
                elif row['source'] == 'www.hoonsmart.com':
                    g3.append([(dm, hoonsmart(row['link']))])
                    

                elif row['source'] == 'www.innnews.co.th':
                    g4.append([(dm, innnews(row['link']))])
                   
                elif row['source'] == 'www.posttoday.com':
                    g6.append([(dm, posttoday(row['link']))])
                                
                elif row['source'] == 'www.kaohoon.com':
                    g8.append([(dm, kaohoon(row['link']))])
                    

        list_1 = tuple_merge(g1)
        p.update(list_1)
        list_2 = tuple_merge(g2)
        q.update(list_2)
        list_3 = tuple_merge(g3)
        r.update(list_3)
        list_4 = tuple_merge(g4)
        s.update(list_4)
        list_6 = tuple_merge(g6)
        u.update(list_6)
        list_7 = tuple_merge(g7)
        v.update(list_7)
        list_8 = tuple_merge(g8)
        w.update(list_8)
        
        dd = combine_dict(p, q, r, s, u, v, w)
        df = pd.DataFrame({k: [v] for k, v in dd.items()}).T
        df = df.reset_index()
        df.columns = ['Date', 'Text']
        date_now = date_to_date()
        path1=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Pickle\\'+f'{tag}.pkl'
        # path1=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP_NLP\\Pickle\\'+f'{tag}_' +f'{date_now}.pkl'
        path=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Pickle\\'+f'{tag}.csv'
        # path=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP_NLP\\Pickle\\'+f'{tag}_' +f'{date_now}.csv'

        if os.path.exists(path):
            os.remove(path)
            df.to_csv(path)
        else:
            df.to_csv(path)

        if os.path.exists(path1):
            os.remove(path1)
            df.to_pickle(path1)
        else:
            df.to_pickle(path1)

       