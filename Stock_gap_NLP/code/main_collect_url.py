from  open_url import *
from  process_wording import *
from  visual_data import *
from  date_of_stock import *
from  source_new import *
import datetime
from pythainlp.util import rank
import pandas as pd


def list_po(data):
        return [x for xs in data for x in xs]
        

if __name__ == '__main__':

        Set100=['AAV','ADVANC','AEONTS','AMATA','ANAN','AOT','AP','AWC','BANPU','BBL','BCH','BCP','BCPG','BDMS','BEC','BEM',
        'BGRIM','BH','BJC','BLAND','BPP','BTS','CBG','CENTEL','CHG','CK','CKP','COM7','CPALL','CPF','CPN','DELTA','DTAC',
        'EA','EGCO','EPG','ERW','ESSO','GFPT','GLOBAL','GPSC','GULF','GUNKUL','HANA','HMPRO','INTUCH','IRPC','IVL','JAS',
        'JMT','KBANK','KCE','KKP','KTB','KTC','LH','MAJOR','MBK','MEGA','MINT','MTC','ORI','OSP','PLANB','PRM','PSH','PSL',
        'PTG','PTT','PTTEP','PTTGC','QH','RATCH','ROBINS','RS','SAWAD','SCB','SCC','SGP','SIRI','SPALI','SPRC','STA','STEC',
        'SUPER','TASCO','TCAP','THAI','THANI','TISCO','TKN','TMB','TOA','TOP','TPIPP','TRUE','TTW','TU','TVO','WHA']
        stock_name_1=[]
        date_1=[]
        Title_1=[]
        p_1=[]
        l_1=[]
        Top10_1=['KBANK','PTT']
        for tag1 in Set100:
                stock_link = "https://stock.gapfocus.com/detail/" + tag1
                print("stock_link :",stock_link)
                soup1 = openhtml(stock_link)
                containers_1 = soup1.findAll("a")
                stock_name=[]
                dates=[]
                Title=[]
                p=[]
                l=[]
                for j,tag in enumerate(containers_1):
                        if  j>15 and tag["href"]!="#":
                                con = tag.text.strip()
                                z=con.split('\n')
                                # print(z)
                                try:
                                        stock_name.append(z[0])
                                        dates.append(z[1])
                                        Title.append(z[2])
                                        # print(y)
                                        # print(i,tag["href"])
                                        p.append(tag["href"])
                                        link_new=tag["href"].split('/')
                                        # print(link_new[2])
                                        l.append(link_new[2])
                                except:
                                        pass
        
                
                stock_name_1.append(stock_name)
                date_1.append(dates)
                Title_1.append(Title)
                p_1.append(p)
                l_1.append(l)
        
        stock=twolist_to_list(stock_name_1)
        # print([x for xs in stock_name_1 for x in xs])
        dat=twolist_to_list(date_1)
        Tit=twolist_to_list(Title_1)
        pp=twolist_to_list(p_1)
        ll=twolist_to_list(l_1)
        df = pd.DataFrame(list(zip(stock,dat,Tit, pp,ll)), 
        columns =['stock_name','date','Title', 'link','source'])
        print(df)
        date_now=date_to_date()
        # print(f'{date_now}')
        df.to_csv(r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\stock_link\\stock_'+f'{date_now}.csv')
        
        