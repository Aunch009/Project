from open_url import *
from process_wording import *
from visual_data import *
from date_of_stock import *
from source_new import *
from stock_yahoo import *
import pickle

if __name__ == '__main__':
    #     Top10_1=['KBANK','PTTEP']
    # #     ,'AOT','ADVANC','IVL','PTTEP','SCB','INTUCH','PTTGC','GULF']
    # #### collect data
    #     stock_name_1,date_1,Title_1,p_1,l_1=[],[],[],[],[]
    #     for tag in Top10_1:
    #         stock_link = "https://stock.gapfocus.com/detail/" + tag
    #         print("stock_link :",stock_link)
    #         soup1 = openhtml(stock_link)
    #         containers_1 = soup1.findAll("a")
    #         stock_name,dates,Title,p,l=[],[],[],[],[]
    #         for i,tag in enumerate(containers_1):
    #             if  i>15 and tag["href"]!="#":
    #                 con = tag.text.strip()
    #                 z=con.split('\n')
    #                 # print(z)
    #                 try:
    #                     stock_name.append(z[0])
    #                     dates.append(z[1])
    #                     Title.append(z[2])
    #                     # print(tag["href"])
    #                     p.append(tag["href"])
    #                     link_new=tag["href"].split('/')
    #                     l.append(link_new[2])
    #                 except:
    #                     pass
    #         # print(len(dates))
    #         # print(p)
    #         stock_name_1.append(stock_name)
    #         date_1.append(dates)
    #         Title_1.append(Title)
    #         p_1.append(p)
    #         l_1.append(l)
    #     stock=twolist_to_list(stock_name_1)
    #     dat=twolist_to_list(date_1)
    #     Tit=twolist_to_list(Title_1)
    #     pp=twolist_to_list(p_1)
    #     ll=twolist_to_list(l_1)
    #     df1 = pd.DataFrame(list(zip(stock,dat,Tit, pp,ll)),
    #     columns =['stock_name','date','Title', 'link','source'])
    #     date_now=date_to_date()
    #     # df1.to_csv(r'D:\Program_code\python\Code_test\stock_gap_NLP\stock_test_'+f'{date_now}.csv')
    dataframe = pd.read_csv(
        'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv'
    )
    # print(df)

    # Top10 = ['PTT']
    #ICT_SET100
    Top10 = ['CPALL']
    # Top10 = ['BCH','BDMS','BH','CHG']
    # Top10 = ['BANPU','BCP','BCPG','BGRIM','BPP','CKP','EA','EGCO','ESSO','GPSC','GULF','GUNKUL','IRPC','PTG','PTT','PTTEP','RATCH','SGP','SPRC','SUPER','TOP','TPIPP','TTW']
    # Top10 = ['BBL','KBANK','KKP','KTB','SCB','TCAP','TISCO','TMB']
    # Top10 = ['AEONTS','JMT','KTC','MTC','SAWAD','THANI']
    # Top10 = ['BBL','KKP','KTB','SCB','TCAP','TISCO','TMB']
    # Top10 = ['ADVANC','DTAC','INTUCH','JAS','TRUE']
    # Top10 = ['AOT','SCB','ADVANC','PTT','BDMS','CPALL']
    # Top10 = ['PTT','AOT','CPALL','ADVANC','SCC','PTTEP','SCB','KBANK','BDMS','BBL']
    
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
                    # g3.append([(dm, [row['link']])])

                elif row['source'] == 'www.innnews.co.th':
                    g4.append([(dm, innnews(row['link']))])
                    # g4.append([(dm, [row['link']])])
                    # print(s)
            #         # elif link_new[2]=='mgronline.com':
            #         #         mgronline(tag["href"])
                elif row['source'] == 'www.posttoday.com':
                    g6.append([(dm, posttoday(row['link']))])
                    # g6.append([(dm, [row['link']])])
                    # print(u)
                # elif row['source'] == 'www.thunhoon.com':
                #     g7.append([(dm, thunhoon(row['link']))])
                #     # g7.append([(dm, [row['link']])])

            #                 # print(v)
                elif row['source'] == 'www.kaohoon.com':
                    # print('www.kaohoon.com:',row['link'])
                    g8.append([(dm, kaohoon(row['link']))])
                    # g8.append([(dm, [row['link']])])

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
        # print('p=', p)
        # print('q=', q)
        # print('r=', r)
        # print('s=', s)
        # print('u=', u)
        # print('v=', v)
        # print('w=', w)
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

       