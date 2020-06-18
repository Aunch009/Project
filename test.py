from open_url import *
from process_wording import *
from visual_data import *
from date_of_stock import *
from source_new import *
from stock_yahoo import *
import pickle
from pythainlp.corpus import thai_stopwords
from pythainlp.corpus.common import thai_words
from pythainlp.tokenize import dict_trie, word_tokenize

def tokenize_text_list_test(ls):
    
    print("working on")
    li=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie']
    # li=['cfcut','newmm']
    custom_dict = set(thai_words())
    trie = dict_trie(dict_source=custom_dict)
    p,q=[],[]
    for x in li:
        start = time.process_time()
        if x=='deepcut' :
            g = list(
                chain.from_iterable([
                    pythainlp.tokenize.word_tokenize(l, engine=x) for l in ls
                ]))
        else:
            g = list(
                chain.from_iterable([
                    pythainlp.tokenize.word_tokenize(l, engine=x, custom_dict=trie) for l in ls
                ]))
        p.append(g)
        # print(g)
        tim=time.process_time() - start
        q.append(tim)  
    return p,q
    
def stop_sentences_filter(tokenized_texts_sentence):
    
    stop_sentences = set(('มูลค่าการซื้อขายล้านบาทปิดที่บาทเพิ่มขึ้นบาท','มูลค่าการซื้อขายล้านบาทปิดที่บาทลดลงบาท','ที่มา','–','กลยุทธ์การลงทุน','แนวรับ',
    'แนวต้าน','ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท','แนวโน้มตลาดหุ้นไทย',
    'ปัจจัยบวกปัจจัยลบ','หุ้นมีข่าว','หุ้นรายงานพิเศษ','จุดจุดจุด','–’–“”','ส่วนหลักทรัพย์ที่มีมูลค่าการซื้อขายสูงสุดหลักทรัพย์ได้แก่','’','…',
    'และหุ้นที่มีการขายสุทธิผ่านไทยเอ็นวีดีอาร์มากที่สุดอันดับแรกหากพิจารณาจากจำนวนหุ้นที่ขายสุทธิได้แก่',
    'และหุ้นที่มีการขายสุทธิผ่านไทยเอ็นวีดีอาร์มากที่สุดอันดับแรกหากพิจารณาจากมูลค่าที่ขายสุทธิได้แก่',
    'หุ้นที่มีการซื้อสุทธิผ่านไทยเอ็นวีดีอาร์มากที่สุดอันดับแรกหากพิจารณาจากมูลค่าที่ซื้อสุทธิได้แก่',
    # 'หมายเหตุ–ไม่รวมรายการขายชอร์ตของสมาชิกที่เป็นผู้ร่วมค้าหน่วยลงทุนหรือผู้ดูแลสภาพคล่องของหน่วยลงทุนของกองทุนรวมอีทีเอฟเพื่อบัญชีบริษัทประเภทเพื่อทำกำไรจากส่วนต่างของราคาหรือเพื่อดูแลสภาพคล่องแล้วแต่กรณี–รายการที่ชื่อย่อหลักทรัพย์ต่อด้วย“”หมายถึงข้อมูลธุรกรรมขายชอร์ตในเอ็นวีดีอาร์',
    'แนวโน้มตลาดหุ้นวันนี้','ตลาดหุ้นเอเชีย','เดินเกมกลยุทธ์บ่าย','แนวโน้มตลาดบ่าย','สรุปภาวะตลาดเช้า','ต่างชาติมีสถานะขายหมื่นลบค่าเงินบาทบาท','แนวรับบาทแนวต้านบาท','หุ้นแนะนำ','หุ้นแนะนำวันนี้',
    'บทวิเคราะห์วันนี้','ปัจจัยเฉพาะตัว','ตลาดหุ้นวานนี้','ประเด็นการลงทุน','ประเด็นสำคัญวันนี้','มูลค่าการซื้อขายล้านบาทปิดที่บาทราคาไม่เปลี่ยนแปลง',
    'คาดการณ์ตลาดหุ้นไทยวันนี้','ต่างชาติมีสถานะขายลบค่าเงินบาทบาท','หุ้นกดดัชนีวันนี้','หุ้นไทยภาคบ่ายปิดตลาดจุดลบจุดหรือ','แนวรับจุดแนวต้านสัดส่วนเงินสดพอร์ตหุ้น',
    'ปรับเพิ่มขึ้นจุดปิดภาคเช้าที่จุดด้วยมูลค่าการซื้อขายล้านบาท','ผู้สื่อข่าวรายงานว่าวานนี้มคจากข้อมูลการซื้อขายหุ้นรายวันผ่านไทยเอ็นวีดีอาร์ซึ่งเป็นดัชนีหนึ่งที่สะท้อนการซื้อขายของนักลงทุนต่างชาติพบว่าหุ้นที่มีการซื้อสุทธิมากที่สุดอันดับแรกหากพิจารณาจากจำนวนหุ้นที่ซื้อสุทธิได้แก่',
    'แลกเปลี่ยนขายบดอลลาร์','อัตราแลกเปลี่ยนของธนาคารกสิกรไทยเวลานดอลลาร์สหรัฐรับซื้อบาทขายบาท','ผู้สื่อข่าวรายงานว่าวานนี้ธคจากข้อมูลการซื้อขายหุ้นรายวันผ่านไทยเอ็นวีดีอาร์ซึ่งเป็นดัชนีหนึ่งที่สะท้อนการซื้อขายของนักลงทุนต่างชาติพบว่าหุ้นที่มีการซื้อสุทธิมากที่สุดอันดับแรกหากพิจารณาจากจำนวนหุ้นที่ซื้อสุทธิได้แก่',
    'หุ้นแนะนารายสัปดาห์','ผู้สื่อข่าวรายงานว่าดัชนีปิดตลาดวันนี้ที่ระดับจุดลบจุดหรือมูลค่าการซื้อขายหมื่นล้านบาท','หุ้นดันดัชนีเช้านี้','–’','ผู้สื่อข่าวรายงานว่าดัชนีช่วงเช้าปิดที่ระดับจุดเพิ่มขึ้นจุดหรือมูลค่าการซื้อขายหมื่นล้านบาท','หุ้นดันดัชนีวันนี้','หุ้นไทยภาคเช้าปิดที่จุดบวกจุดหรือ','หุ้นไทยเวลานดัชนีอยู่ที่จุดบวกจุดหรือ',
    'อัตราแลกเปลี่ยนของธนาคารกสิกรไทยเมื่อเวลานดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท','อัตราแลกเปลี่ยนขายบดอลลาร์','กลยุทธ์โดยมีจุดขายตัดขาดทุน','โดยมีจุดขายตัดขาดทุน','ทั้งนี้ข้อมูลที่มีการนำเสนอข้างต้นเป็นเพียงข้อแนะนำจากข้อมูลพื้นฐานเพื่อประกอบการตัดสินใจของนักลงทุนเท่านั้นและมิได้เป็นการชี้นำหรือเสนอแนะให้ซื้อหรือขายหลักทรัพย์ใดการตัดสินใจซื้อหรือขายหลักทรัพย์ใดของผู้อ่านไม่ว่าจะเกิดจากการอ่านบทความในเอกสารนี้หรือไม่ก็ตามล้วนเป็นผลจากการใช้วิจารณญาณของผู้อ่าน',
    'ผู้สื่อข่าวรายงานว่าดัชนีปิดตลาดวันนี้ที่ระดับจุดบวกจุดหรือมูลค่าการซื้อขายหมื่นล้านบาท','“”','โดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์','หมายถึงหุ้นทางกลยุทธ์ซึ่งอาจมีคำแนะนำต่างกับพื้นฐานหรือที่ไม่ได้อยู่ในการวิเคราะห์ของซึ่งนักลงทุนควรพิจารณาตั้งจุดตัดขาดทุนของราคาที่เข้าซื้อ','หุ้นกดดัชนีเช้านี้','ประเด็นสาคัญ','ผู้สื่อข่าวรายงานว่าดัชนีช่วงเช้าปิดที่ระดับจุดลดลงจุดหรือมูลค่าการซื้อขายหมื่นล้านบาท','หุ้นไทยภาคบ่ายปิดตลาดจุดบวกจุดหรือ','ดัชนี',
    'ตลาดหุ้นเมื่อวันศุกร์','ปรับลดลงจุดปิดภาคเช้าที่จุดด้วยมูลค่าการซื้อขายล้านบาท','ราคาปิดแนวรับแนวต้าน','ส่องหุ้น','หุ้นไทยภาคเช้าปิดที่จุดลบจุดหรือ','บรรยากาศการซื้อขายตลาดหลักทรัพย์ตลอดทั้งวันปิดลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','ปิดเช้าบวกแตะจุด','ปิดเช้าลบแตะจุด','ปิดตลาดหุ้นไทยเช้าเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท','ปิดตลาดหุ้นไทยเช้าลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','พร้อมให้แนวรับจุดส่วนแนวต้านจุด',
    'สำหรับการซื้อขายในตลาดหลักทรัพย์ตลอดช่วงเช้าที่ผ่านมาปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท','สำหรับการซื้อขายในตลาดหลักทรัพย์ตลอดทั้งวันที่ผ่านมาปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','หุ้นไทยเช้านี้เปิดตลาดเพิ่มขึ้นจุดแตะจุดด้วยมูลค่าการซื้อขายล้านบาท','หุ้นไทยปิดลบแตะจุด','หุ้นเปิดบวกจุดแตะจุด','ธค','ราคาปิด','หุ้นไทยเช้านี้เปิดตลาดลดลงจุดแตะจุดด้วยมูลค่าการซื้อขายล้านบาท','หุ้นเปิดลบจุดแตะจุด','–“”','ตลาดหุ้นไทยภาคเช้าปิดบวกจุดแตะจุดมูลค่าซื้อขายล้านบาท',
    'ตลาดหุ้นปิดลบจุดแตะจุดมูลค่าซื้อขายล้านบาท','บรรยากาศการซื้อขายตลาดหลักทรัพย์ตลอดทั้งวันปิดเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท','ส่วนหลักทรัพย์ที่มีมูลค่าการซื้อขายสูงสุดอันดันแรกได้แก่','หุ้นที่หุ้นในที่ยังปรับขึ้นน้อยนับจากต้นปีได้แก่','หุ้นไทยปิดบวกแตะจุด',
    '’’','ประเด็นสำคัญ','สรุปความเคลื่อนไหวของค่าเงินบาท','สำหรับการซื้อขายในตลาดหลักทรัพย์ตลอดช่วงเช้าที่ผ่านมาปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','สำหรับการซื้อขายในตลาดหลักทรัพย์ตลอดทั้งวันที่ผ่านมาปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท','หุ้นเด่นวันนี้ตามปัจจัยพื้นฐานสุโชติถิรวรรณรัตน์เลขทะเบียน',
    'หุ้นที่แนะนำก่อนหน้าเป้าบาทประเมินแนวรับบาทแนวต้านบาทบาทเป้าบาทประเมินแนวรับบาทแนวต้านบาทบาทเป้าพื้นฐานบาทประเมินแนวรับบาทแนวต้านบาทหากผ่านได้แนะนำบาทเป้าพื้นฐานบาทประเมินแนวรับบาทแนวต้านบาทบาทเป้าบาทประเมินแนวรับบาทแนวต้านบาทบาท','หุ้นไทยเวลานดัชนีอยู่ที่จุดลบจุดหรือ','อดิศักดิ์คำมูลต่อ','–คาดหุ้นเข้าหุ้นออก','แนวรับแนวต้าน','ราคาเหมาะสมบาท','ส่งผลให้ดัชนีปิดที่จุดจุดหมื่นลบต่างชาติลบสัญญา','สรุปความเคลื่อนไหวของตลาดหุ้นไทย','บาท','ปิดแนวรับแนวต้าน','มค','หุ้นเช้าปิดลบจุดวอลุ่มหมื่นล',
    'หุ้นแนะนำทางเทคนิค','ราคาเหมาะสม','สรุปภาวะตลาดหุ้นไทยวานนี้','–’–','·หุ้น','·หุ้นเด่นเดือนธค','…รอปัจจัยใหม่ผลประชุมและข้อตกลงการค้าก่อนธค','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันศุกร์ธคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','กลุ่มหุ้นแนะนำอื่น','แนวโน้มภาคบ่าย','ปิด','ผู้สื่อข่าวรายงานว่าวันศุกร์ที่ผ่านมามคจากข้อมูลการซื้อขายหุ้นรายวันผ่านไทยเอ็นวีดีอาร์ซึ่งเป็นดัชนีหนึ่งที่สะท้อนการซื้อขายของนักลงทุนต่างชาติพบว่าหุ้นที่มีการซื้อสุทธิมากที่สุดอันดับแรกหากพิจารณาจากจำนวนหุ้นที่ซื้อสุทธิได้แก่','พร้อมให้แนวต้านจุดแนวรับจุด'
    'ระบบ','เลือกทั่วไป','สรุปภาวะตลาดเงินตลาดทุนรายสัปดาห์วันที่ธันวาคม','สรุปภาวะตลาดหุ้นทองคาน้ามันวานนี้','สรุปภาวะตลาดหุ้นทองคำน้ำมันวานนี้','สัญญาณเทคนิค','อ่านข่าว','––','–––','–––––','’–','’’’','·ราคาปิดบาท','กพ','–ได้แก่ได้แก่','ตลาดหุ้นไทยทำปลายปี','ตลาดหุ้นปิดบวกจุดแตะจุดมูลค่าซื้อขายล้านบาท'
    'หุ้นแนะนำรายสัปดาห์','หุ้นแนะนำประจำสัปดาห์','ประมาณการ','ประเด็นสาคัญวันนี้','ประเด็นพิจารณาการลงทุน',
    'บริการนี้ไม่มีกำหนดยอดชำระขั้นต่ำสามารถชำระเงินได้สูงสุดบาทครั้งวันและไม่มีค่าธรรมเนียมโดยลูกค้าสามารถตรวจสอบยอดชำระสินค้าได้ทั้งสกุลบาทและสกุลเงินต่างเทศรวมถึงทราบอัตราแลกเปลี่ยนที่แน่นอนก่อนชำระเงินไม่ต้องกังวลเรื่องความผันผวนของค่าเงินและเมื่อทำรายการสำเร็จจะได้รับเป็นหลักฐานการชำระเงินรวมถึงสามารถเรียกดูประวัติการใช้จ่ายย้อนหลังได้ตลอดเวลาผ่าน',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้ามคที่ผ่านมาปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้ามคที่ผ่านมาปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้ามคที่ผ่านมาปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้าพยที่ผ่านมาปิดตลาดดัชนีปรับลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้าพยที่ผ่านมาปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้าธคที่ผ่านมาปิดตลาดดัชนีปรับลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้าธคที่ผ่านมาปิดตลาดดัชนีปรับเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์','บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้าธคที่ผ่านมาปิดตลาดดัชนีปรับเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยภาคเช้าธคที่ผ่านมาปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมามคปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมามคปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมามคปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมาธคปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมาธคปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมาธคปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าการซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมาธคปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมากพปิดตลาดดัชนีปรับตัวลดลงจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมากพปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์ส่วนอัตราแลกเปลี่ยนเงินบาทต่อดอลลาร์สหรัฐของธนาคารกสิกรไทยล่าสุดเมื่อเวลานมีดังนี้ดอลลาร์สหรัฐรับซื้อที่บาทขายออกบาท','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมากพปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาทโดยหลักทรัพย์ปรับเพิ่มขึ้นหลักทรัพย์ลดลงหลักทรัพย์ไม่เปลี่ยนแปลงหลักทรัพย์','บรรยากาศการลงทุนในตลาดหุ้นไทยตลอดทั้งวันที่ผ่านมากพปิดตลาดดัชนีปรับตัวเพิ่มขึ้นจุดแตะจุดมูลค่าซื้อขายล้านบาท',
    'บรรยากาศการลงทุนในตลาดหุ้นไทยเช้าวันนี้ธคเปิดทำการเมื่อเวลานดัชนีปรับตัวลเพิ่มขึ้นจุดแตะจุดด้วยมูลค่าการซื้อขายล้านบาท','–’“”','’“”','’’“”','‘','—','––––','สรุปภาวะตลาดหุ้นทองคำน้ำมันวันศุกร์','วิธี','เลือกอัปเดตซอฟต์แวร์','เลือกรายการอัปเดตซอฟต์แวร์','เลือกข้อมูลซอฟต์แวร์','เลือกเกี่ยวกับโทรศัพท์','เลือกเกี่ยวกับดูที่เวอร์ชันซอฟต์แวร์','ยังมีต่อ','ต่อบลเอเซียพลัส','ดูที่เวอร์ชัน','กรุงเทพธุรกิจออนไลน์ณเวลานการซื้อขายหลักทรัพย์ภาคเช้าวันศุกร์มคดัชนีอยู่ที่จุดปรับเพิ่มขึ้นจุดคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท',
    'กรุงเทพธุรกิจออนไลน์ณเวลานการซื้อขายหลักทรัพย์ภาคเช้าวันพฤหัสบดีธคดัชนีอยู่ที่จุดปรับเพิ่มขึ้นจุดคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันศุกร์มคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันพุธมคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันพุธธคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันพฤหัสบดีมคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท',
    'กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันพฤหัสบดีมคเวลานดัชนีปิดที่ระดับจุดปรับเพิ่มขึ้นจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันจันทร์มคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','“”ต้านจุดรับจุด','เด้งสลับย่อ','และเงินเยนของญี่ปุ่นอยู่ที่บาทต่อเยน','ระบบ','ยูโรอยู่ที่ระดับบาทต่อยูโร','ปอนด์อยู่ที่บาทต่อปอนด์','เข้าไปที่เมนูการตั้งค่า',
    'กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันจันทร์ธคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท','อันดับหลักทรัพย์ที่มีการซื้อขายสูงสุดคือ','ปิดที่บาทลดลง','กรุงเทพธุรกิจออนไลน์การซื้อขายหลักทรัพย์ภาคบ่ายวันอังคารธคเวลานดัชนีปิดที่ระดับจุดปรับลดลงจุดหรือคิดเป็นมูลค่าการซื้อขายทั้งสิ้นล้านบาท'
))
    # stop_sentence =set(stop_sentences)
    # print(tokenized_texts_sentence)
    filtered_sentence = [] 
    filtered_sentence = [w for w in tokenized_texts_sentence if not w in stop_sentences]
    return filtered_sentence
        

if __name__ == '__main__':
    
    # dataframe = pd.read_csv(
    #     'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\combine.csv'
    # )
    # print(df)
    # Top10 = ['AEONTS','JMT','KTC','MTC','SAWAD','THANI']
    # Top10 = ['BH','CPALL','TOP']
    Top10 = ['CPALL']
    # Top10 = ['TISCO','TMB']
    # Top10 = ['BBL','KKP','KTB','SCB','TCAP','TISCO','TMB']
    # Top10 = ['BANPU','BCP','BCPG','BGRIM','BPP','CKP','EA','EGCO','ESSO','GPSC','GULF','GUNKUL','IRPC','PTG','PTT','PTTEP','RATCH','SGP','SPRC','SUPER','TOP','TPIPP','TTW']

    # Top10 = ['DTAC','INTUCH','JAS','TRUE']
    # Top10 = ['AOT','SCB','ADVANC','PTT','BDMS']

    # Top10 = ['PTT','AOT','CPALL','ADVANC','SCC','PTTEP','SCB','KBANK','BDMS','BBL']
    # p, q, r, s, u, v, w = {}, {}, {}, {}, {}, {}, {}
    # # f1,f2,f3,f4,f6,f7,f8={},{},{},{},{},{},{}
    # g1, g2, g3, g4, g6, g7, g8 = [], [], [], [], [], [], []
    for tag in Top10:
        print(tag)
        
        date_now = date_to_date()
        path=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Pickle\\'+f'{tag}.pkl'
        # path=r'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Pickle\\'+f'{tag}_2020-01-05.csv'

        print(path)
        # if os.path.exists(path):
        #     os.remove(path)
        #     df.to_pickle(path)
        # else:
        #     df.to_pickle(path)
        df = pd.read_pickle(path)
        sort_data = df.sort_values('Date', inplace=False, ascending=False)
        # print(sort_data)
        sort_data.reset_index(inplace=True)
        # print(sort_data)
        st = list(sort_data.Date)[-1].split('-')
        # print(st)
        start = datetime.date(int(st[0]), int(st[1]), int(
            st[2])) - timedelta(days=5)
        print(start)
        end = sort_data.Date[0]
        print(end)
        

        #Download historical data from yahoo.finance.com
        # download_historicaldata(tag, start, end)
        download_historicaldata(tag, start, '2020-02-04')

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
        #### add current date
        add_currentdate=pd.DataFrame({'Date':['2020-02-05','2020-02-06','2020-02-07']})
        # print(add_date)
        df2=df1.append(add_currentdate)
        re = df2.merge(df, on='Date')
        # re = df1.merge(df, on='Date')
        # re.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\merge_word.csv')
        # re.drop(['Unnamed: 0'], inplace=True, axis=1)
        print(re)
        #reference :https://tupleblog.github.io/deepcut-classify-news/
        re['Text'] = re.Text.map(stop_sentences_filter)
        # re.to_csv(r'D:\Program_code\python\Code_test\stock_gap_NLP\CPALL_senten.csv')
        print(re)
        tokenized_texts = re.Text.map(tokenize_text_list_test)
        print(tokenized_texts)
        ## datf = pd.DataFrame(list(tokenized_texts),columns=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie'])
        ##datf1 = pd.DataFrame(list(time),columns=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie'])
        datf = pd.DataFrame(list(tokenized_texts),columns=['Word','time'])

        tokenized_texts_word = pd.DataFrame(list(datf['Word']),columns=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie'])
        tokenized_texts_word.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\Token\\token_'+f'{tag}.csv')      
        tokenized_texts_word.to_pickle('D:\Program_code\python\Code_test\stock_gap_NLP\Token\\token_'+f'{tag}.pkl')      
        # tokenized_texts_word.to_pickle('D:\Program_code\python\Code_test\stock_gap_NLP\Token\\token_'+f'{tag}_'+'3pre.pkl')      
        # tokenized_texts_word.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\Token\\token_'+f'{tag}_' +'3pre.csv')      

        tokenized_time = pd.DataFrame(list(datf['time']),columns=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie'])
        tokenized_time['word_method']='Normal'
        # tokenized_time.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\Token_time\\time_'+f'{tag}_' +'3pre.csv')
        # tokenized_time.to_pickle('D:\Program_code\python\Code_test\stock_gap_NLP\Token_time\\time_'+f'{tag}_'+'3pre.pkl')
        tokenized_time.to_pickle('D:\Program_code\python\Code_test\stock_gap_NLP\Token_time\\time_'+f'{tag}.pkl')
        tokenized_time.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\Token_time\\time_'+f'{tag}.csv')

        # tokenized_texts = re.Text.map(tokenize_text_list_test1)
        # tokenized_texts.to_csv(r'D:\Program_code\python\Code_test\stock_gap_NLP\test6.csv')

        # print(tokenized_texts)
        # print(tokenized_texts.shape)
        # print(tokenized_texts)
        # print(re)
        # file = 'D:\Program_code\python\Code_test\stock_gap_NLP\Token\PTT_2019-12-25_'+f'{tag}.pkl'
        # with open(file, 'wb') as handle:
        #     pickle.dump(tokenized_texts, handle, protocol=pickle.HIGHEST_PROTOCOL)
        # with open(file, 'rb') as handle:
        #     tokenized_texts = pickle.load(handle)
        # stop_words = set(thai_stopwords()) 
        # print(tokenized_texts.shape)
        # filtered_sentence = [] 
        # for r, tokens in enumerate(tokenized_texts):
        #     filtered_sentence = [w for w in tokens if not w in stop_words] 
        #     print(filtered_sentence)
        # size=len(re.close_status)-1
        # re=re.drop(re.index[size])
        # print(re.shape)
        # li=['cfcut','deepcut','etcc','longest','multi_cut','newmm','ssg','tcc','trie']
        # for  method in li:
        #     tokenized_te=tokenized_texts_word[method]
        #     # print(tokenized_te)
        #     vocabulary_ = {
        #         v: k
        #         for k, v in enumerate(set(chain.from_iterable(tokenized_te)))
        #     }
            
        #     # print('vocabulary_:',len(vocabulary_))
            
        #     # print('vocabulary_:',vocabulary_)
        #     X = text_to_bow(tokenized_te, vocabulary_)
        #     # print(X.shape)
        #     # tokenizer = text_to_bow(tokenized_texts, vocabulary_)
        #     # print(X)
        #     # file = 'D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\Token\\'+f'{tag}_' +f'{date_now}.pkl'
        #     # file = 'D:\Program_code\python\Code_test\stock_gap_NLP\Token\PTT_2019-12-25.pkl'
        #     # # with open(file, 'wb') as handle:
        #     # #     pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
        #     # with open(file, 'rb') as handle:
        #     #     X = pickle.load(handle)
        #     # re['Text'] = text_to_bow(tokenized_texts, vocabulary_)
        #     # print(re)
        #     # re.to_pickle('Tokenize_KBANK.pkl')


        #     # print('X.shape:', X.shape)

        #     from sklearn.feature_extraction.text import TfidfTransformer
        #     from sklearn.decomposition import TruncatedSVD
        #     from sklearn.model_selection import train_test_split, cross_val_score
        #     from sklearn.linear_model import LogisticRegression
        #     from sklearn import metrics
        #     from sklearn.metrics import precision_score, recall_score
        #     import matplotlib.pyplot as plt
        #     from sklearn.metrics import plot_confusion_matrix
            
        #     transformer = TfidfTransformer()
        #     X_tfidf = transformer.fit_transform(X)
        #     # print('xshape:' ,X.shape )
        #     # print('re.close_statusshape',re.close_status.shape)

        #     # print('x:' ,X )
        #     # print('X_tfidf:' ,X_tfidf )
        #     # print('re.close_status',re.close_status)
        #     x_train, x_test, y_train, y_test = train_test_split(X_tfidf,
        #                                                         re.close_status,
        #                                                         test_size=0.,random_state=42)
        #     # print(x_test)
        #     # print(y_test)
        #     from sklearn.model_selection import train_test_split
        #     from sklearn.neighbors import KNeighborsClassifier
        #     from sklearn.linear_model import LogisticRegression
        #     from sklearn.naive_bayes import GaussianNB
        #     from sklearn import metrics
        #     from sklearn.ensemble import GradientBoostingClassifier
        #     from sklearn.ensemble import RandomForestClassifier
        #     from sklearn.ensemble import AdaBoostClassifier
        #     from sklearn.svm import SVC
        #     from xgboost import XGBClassifier

        #     algo = [[KNeighborsClassifier(), 'KNeighborsClassifier'],
        #             [LogisticRegression(solver='lbfgs'), 'LogisticRegression'],
        #             # [GaussianNB(), 'GaussianNB'],
        #             [SVC(), 'SVM'],
        #             [GradientBoostingClassifier(), 'GradientBoostingClassifier'],
        #             [RandomForestClassifier(), 'RandomForestClassifier'],
        #             [AdaBoostClassifier(), 'AdaBoostClassifier'],
        #             [XGBClassifier(),'XGBClassifier']]
        #     model_score = []
        #     for a in algo:
        #         model = a[0]
        #         #Step2 : fit model
        #         model.fit(x_train, y_train)
        #         #step3:predict
        #         y_pre = model.predict(x_test)
        #         #step4 :Score
        #         score = model.score(x_test, y_test)
        #         model_score.append([score, a[1]])
        #         print(f'{a[1]}score={score}')
        #         print(metrics.confusion_matrix(y_test, y_pre))
        #         print(metrics.classification_report(y_test, y_pre))
        #         report=metrics.classification_report(y_test, y_pre, output_dict=True)
        #         mat = pd.DataFrame(report).transpose()
        #         fn=str(a[1])
        #         mat['function']=fn
        #         mat['token']=method
        #         # mat.columns=['parameter','f1-score', 'precision', 'recall', 'support', 'function']
        #         mat.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\classification_report\\'+f'{tag}_{method}_{a[1]}.csv')
        #         # mat.to_csv('D:\\Program_code\\python\\Code_test\\stock_gap_NLP\\classification_report\\'+f'{tag}_{date_now}_{method}_{a[1]}.csv')
        #         np.set_printoptions(precision=2)
        #         y_name=[x for x in list(y_test)]
        #         # print(y_name)
        #         class_names=removeDuplicates(y_name)
        #         # class_names=y_test_names
        #         disp = plot_confusion_matrix(a[0], x_test,y_test ,
        #                             display_labels=class_names,
        #                             cmap=plt.cm.Blues,
        #                             normalize=None)
        #         disp.ax_.set_title(a[1])
        #         # plt.savefig('D:\Program_code\python\Code_test\stock_gap_NLP\confusion_matrix\\'+f'{tag}_{date_now}_{method}_{a[1]}.png')
        #         plt.savefig('D:\Program_code\python\Code_test\stock_gap_NLP\confusion_matrix\\'+f'{tag}_{method}_{a[1]}.png')
        #         # # plt.show()
        #         print('----------------------------' * 3)
        #     print(model_score)
        #     dscore = pd.DataFrame(model_score, columns=['score', 'Model Classifier']) 
        #     dscore['token']=method
        #     dscore['stock']=tag
        #     dscore['word_method']='Normal'
        #     # print(dscore)
        #     print(dscore.sort_values('score', ascending=False))
        #     dscore.sort_values('score', ascending=False).reset_index(inplace=True)
        #     # dscore.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\classification_report_combine\\'+f'{tag}_{date_now}_{method}.csv')
        #     dscore.to_csv('D:\Program_code\python\Code_test\stock_gap_NLP\classification_report_combine\\'+f'{tag}_{method}.csv')
