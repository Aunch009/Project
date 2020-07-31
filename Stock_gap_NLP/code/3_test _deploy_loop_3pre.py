from open_url import *
from process_wording import *
from visual_data import *
from date_of_stock import *
from source_new import *
from stock_yahoo import *
import pickle
from pythainlp.corpus import thai_stopwords
from scipy.sparse import csr_matrix
import scipy.sparse


def tokenize_text_list_test(ls):
    
    print("working on")
    li=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie']
    # li=['cfcut','newmm']
    p,q=[],[]
    for x in li:
        start = time.process_time()
        g = list(
            chain.from_iterable([
                pythainlp.tokenize.word_tokenize(l, engine=x) for l in ls
            ]))
        p.append(g)
        # print(g)
        tim=time.process_time() - start
        q.append(tim)  
    return p,q



if __name__ == '__main__':
    
    
    Top10 =  ['INTUCH']
    # Top10 = ['INTUCH','TOP','BH','CPALL','KBANK']
    
    for tag in Top10:
        print(tag)
        # ppp=[]
        date=['2020-02-05','2020-02-06','2020-02-07']
        # date=['2020-02-05']
        store=[]
        for n,ddate in enumerate(date):
            ppp=[]
            for x in range(5):                              
                date_now = date_to_date()
                path=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Pickle\\'+f'{tag}.pkl'
                # path=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Pickle\\'+f'{tag}_2020-01-05.csv'

                print(path)
                
                df = pd.read_pickle(path)
                sort_data = df.sort_values('Date', inplace=False, ascending=False)
                # print(sort_data)
                sort_data.reset_index(inplace=True)
                # print(sort_data)
                # print(current)
                st = list(sort_data.Date)[-1].split('-')
                # print(st)
                start = datetime.date(int(st[0]), int(st[1]), int(
                    st[2])) - timedelta(days=5)
                print(start)
                endst = ddate.split('-')
                # print(st)
                end = datetime.date(int(endst[0]), int(endst[1]), int(
                    endst[2])) - timedelta(days=1)
                print(end)
            
                

                #Download historical data from yahoo.finance.com
                download_historicaldata(tag, start, end)

                #loading historical data csv file
                stocks = str(tag+ '.BK.csv')
                df1 = pd.read_csv(
                    'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\yahoo_finance\\' +
                    stocks)
                print(df1)
                df1['Diff'] = df1.Close.diff()
                df1['close_status'] = df1.Close.diff()
                # print(re)
                round2 = lambda x: status_stock(x)
                df1['close_status'] = pd.DataFrame(df1.close_status.apply(round2))
                # df1.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\yahoo_word.csv')
                # print(df1)
                add_date=pd.DataFrame({'Date':[ddate]})
                # print(add_date)
                df2=df1.append(add_date)
                # print(df2)
                re = df2.merge(df, on='Date')
                # re.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\merge_word.csv')
                # re.drop(['Unnamed: 0'], inplace=True, axis=1)
                print(re)
                
                path1 = 'D:\Program_code\python\Code_test\stock_gap_NLP\Token\\token_'+f'{tag}.pkl'
                print(path1)
                tokenized_texts_word = pd.read_pickle(path1)
                
                re1=re.copy()
                # sizey=len(re1)
                re1=re1[:-1]
                print(re1.close_status)
                # print(re1)
                # li=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie']
                li=['cfcut']
                list_token=[]
                for  method in li:
                    tokenized_te=tokenized_texts_word[method]
                    # print(tokenized_te)
                    vocabulary_ = {
                        v: k
                        for k, v in enumerate(set(chain.from_iterable(tokenized_te)))
                    }
                    f=pd.DataFrame(list( vocabulary_ .items()),columns=['word','ind'])
                    f.sort_values('ind', ascending=True).reset_index(inplace=True)
                    print(f)
                    f.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\word_index\word_'+f'{tag}_'+f'{method}.csv')
                    # print('vocabulary_:',len(vocabulary_))
                    
                    # print('vocabulary_:',vocabulary_)
                    X = text_to_bow(tokenized_te, vocabulary_ ,method)
                    

                    from sklearn.feature_extraction.text import TfidfTransformer
                    from sklearn.decomposition import TruncatedSVD
                    from sklearn.model_selection import cross_val_score
                    from sklearn import metrics
                    from sklearn.metrics import precision_score, recall_score
                    import matplotlib.pyplot as plt
                    from sklearn.metrics import plot_confusion_matrix
                    from sklearn.model_selection import train_test_split
                    from sklearn.neighbors import KNeighborsClassifier
                    from sklearn.linear_model import LogisticRegression
                    from sklearn.naive_bayes import GaussianNB
                    from sklearn import metrics
                    from sklearn.ensemble import GradientBoostingClassifier
                    from sklearn.ensemble import RandomForestClassifier
                    from sklearn.ensemble import AdaBoostClassifier
                    from sklearn.svm import SVC
                    from xgboost import XGBClassifier
                    # print(X)
                    # X.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\\'+f'{tag}_'+f'{method}.csv')

                    transformer = TfidfTransformer()
                    X_tfidf = transformer.fit_transform(X)
                    # print(X_tfidf)
                    X_data1=pd.DataFrame.sparse.from_spmatrix(X_tfidf)
                    X_data=X_data1.copy()
                    # X_data.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\word_TFIDF\\'+f'{tag}_'+f'{method}.csv')
                    X_1=pd.DataFrame.sparse.from_spmatrix(X)
                    # X_1.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\word_TFIDF\\X_'+f'{tag}_'+f'{method}.csv')
                    size=len(X_data.index)-3
                    X_data=X_data.drop(X_data.index[size])
                    X_data=X_data[:-3+n]
                    print('X_data',X_data)
                    X_data_csr=scipy.sparse.csr_matrix(X_data.values)
                    # print(X_data_csr)
                    # o=pd.DataFrame.sparse.from_spmatrix(X_data_csr)
                    # o.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\k.csv')

                    # X_data_test=X_data1.tail(3)
                    size=len(X_data.index)
                    X_data_test=X_data1[X_data1.index.isin([size])]
                    print('X_data_test',X_data_test)
                    # do=str(f'{method}')
                    co=scipy.sparse.csr_matrix(X_data_test.values)
                    # print(co)
                    scipy.sparse.save_npz('D:\Program_code\python\Code_test\stock_gap_NLP\Currentdate_csr\\'+f'{tag}_'+f'{method}_'+f'{ddate}_pre_'+f'{x}.npz', co)

                    
                    print('X_data_csr',X_data_csr.shape)
                    print('re1.close_status',len(re1.close_status))
                    x_train, x_test, y_train, y_test = train_test_split(X_data_csr,
                                                                        re1.close_status,
                                                                        test_size=0.2)
                    # x_train, x_test, y_train, y_test = train_test_split(X_data_csr,
                    #                                                     re.close_status,
                    #                                                     test_size=0.2,random_state=42)
                    # # print(x_test)
                    print('y_test:',len(y_test))
                    
                    algo = [[KNeighborsClassifier(), 'KNeighborsClassifier'],
                            [LogisticRegression(solver='lbfgs'), 'LogisticRegression'],
                            # [GaussianNB(), 'GaussianNB'],
                            [SVC(), 'SVM'],
                            [GradientBoostingClassifier(), 'GradientBoostingClassifier'],
                            [RandomForestClassifier(), 'RandomForestClassifier'],
                            [AdaBoostClassifier(), 'AdaBoostClassifier'],
                            [XGBClassifier(),'XGBClassifier']]
                    model_score = []
                    for a in algo:
                        model = a[0]
                        #Step2 : fit model
                        model.fit(x_train, y_train)
                        #step3:predict
                        filename = 'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\model\\'+f'{tag}_'+f'{method}_'+ f'{a[1]}_'+f'{ddate}_pre_'+f'{x}.sav'
                        pickle.dump(model, open(filename, 'wb'))
                        y_pre = model.predict(x_test)
                        #step4 :Score
                        score = model.score(x_test, y_test)
                        model_score.append([score, a[1]])
                        print(f'{a[1]}score={score}')
                        print(metrics.confusion_matrix(y_test, y_pre))
                        print(metrics.classification_report(y_test, y_pre))
                        report=metrics.classification_report(y_test, y_pre, output_dict=True)
                        mat = pd.DataFrame(report).transpose()
                        fn=str(a[1])
                        mat['stock']=tag
                        mat['function']=fn
                        mat['token']=method
                        mat['train']=len(y_train)
                        mat['test']=len(y_test)
                        mat['Pre_date']=ddate
                        mat['No_run']=x
                        # mat.columns=['parameter','f1-score', 'precision', 'recall', 'support', 'function']
                        mat.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\classification_report\\'+f'{tag}_{method}_{a[1]}_'+f'{ddate}_pre_'+f'{x}.csv')
                        # mat.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\classification_report\\'+f'{tag}_{date_now}_{method}_{a[1]}.csv')
                        np.set_printoptions(precision=2)
                        y_name=[x for x in list(y_test)]
                        # print(y_name)
                        class_names=removeDuplicates(y_name)
                        # class_names=y_test_names
                        disp = plot_confusion_matrix(a[0], x_test,y_test ,
                                            display_labels=class_names,
                                            cmap=plt.cm.Blues,
                                            normalize=None)
                        disp.ax_.set_title(a[1])
                        # plt.savefig('D:\Program_code\python\Code_test\stock_gap_NLP\confusion_matrix\\'+f'{tag}_{date_now}_{method}_{a[1]}.png')
                        # plt.savefig('D:\Program_code\python\Code_test\stock_gap_NLP\confusion_matrix\\'+f'{tag}_{method}_{a[1]}.png')
                        # # plt.show()
                        print('----------------------------' * 3)
                    print(model_score)
                    dscore = pd.DataFrame(model_score, columns=['score', 'Model Classifier']) 
                    dscore['token']=method
                    dscore['stock']=tag
                    dscore['word_method']='Normal'
                    dscore['train']=len(y_train)
                    dscore['test']=len(y_test)
                    dscore['Pre_date']=ddate
                    dscore['No_run']=x
                    # print(dscore)
                    print(dscore.sort_values('score', ascending=False))
                    dscore.sort_values('score', ascending=False).reset_index(inplace=True)
                    # dscore.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\classification_report_combine\\'+f'{tag}_{date_now}_{method}.csv')
                    dscore.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\classification_report_combine\\'+f'{tag}_{method}_'+f'{ddate}_pre_'+f'{x}.csv')
                    list_token.append(dscore)
                frame = pd.concat(list_token, axis=0, ignore_index=True)
                frame['No_run']=x
                frame1=frame.sort_values('score', ascending=False).reset_index()
                ppp.append(frame1)
                print(frame1)
                # print(frame1)
                print('frame1[:1]:',frame1[:1])
                lst=frame1[:1]


                ### predict test
                print(lst.loc[:,'score'])
                print(str(lst.loc[:,'token']),str(lst.loc[:,'Model Classifier']))
                eng=str(lst.loc[0,'token'])
                mol=str(lst.loc[0,'Model Classifier'])
                print('eng:',str(eng))
                print('mol:',str(mol))


            frame2 = pd.concat(ppp, axis=0, ignore_index=True)
            frame3=frame2.sort_values('score', ascending=False).reset_index()
            frame3.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\model_select\\'+f'{tag}_'+f'{ddate}_pre.csv')
            print(frame3)
            # print(frame1)
            print('frame3[:1]:',frame3[:1])
            lst=frame3[:1]
            print('lst:',lst)
            ### predict test
            print(lst.loc[:,'score'])
            print(str(lst.loc[:,'token']),str(lst.loc[:,'Model Classifier']))
            eng=str(lst.loc[0,'token'])
            mol=str(lst.loc[0,'Model Classifier'])
            run=str(lst.loc[0,'No_run'])
            print('eng:',str(eng))
            print('mol:',str(mol))
            print('run:',str(run))
            filename1 = 'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\model\\'+f'{tag}_'+f'{eng}_'+ f'{mol}_'+f'{ddate}_pre_'+f'{run}.sav'
            print(filename1)
            loaded_model = pickle.load(open(filename1, 'rb'))
            current=scipy.sparse.load_npz('D:\Program_code\python\Code_test\stock_gap_NLP\Currentdate_csr\\'+f'{tag}_'+f'{eng}_'+f'{ddate}_pre_'+f'{run}.npz')
            # print(current)
            result = loaded_model.predict(current) 
            print("predict:",result)
            lst['Pre_date']=ddate
            lst['result']=result
            print('lst:',lst)
            store.append(lst)
    frame4 = pd.concat(store, axis=0, ignore_index=True)
        # frame3=frame2.sort_values('score', ascending=False).reset_index()
    frame4.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\\result\\'+f'{tag}_pre.csv')
          
        
            