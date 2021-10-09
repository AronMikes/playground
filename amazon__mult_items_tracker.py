import bs4, requests
from datetime import datetime

wishlist={'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems (English Edition, ebook)':'http://www.amazon.de/Hands-Machine-Learning-Scikit-Learn-TensorFlow-ebook/dp/B07XGF2G87/ref=sr_1_3',
      'Introduction to Machine Learning with Python: A Guide for Data Scientists (English Edition, ebook)':'http://www.amazon.de/Introduction-Machine-Learning-Python-Scientists-ebook/dp/B01M0LNE8C/ref=sr_1_2'}

def getAmazonPrice(productUrl):

    
    my_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137'}
    other_header={'User-Agent':'Opera/9.80 (Android; Opera Mini/8.0.1807/36.1609; U; en) Presto/2.12.423 Version/12.16'}

    res=requests.get(productUrl,headers=my_header)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text, 'html5lib') # last bit is the parser
    elems=soup.select('#buybox> div > table > tbody > tr.kindle-price > td.a-color-price.a-size-medium.a-align-bottom > span')
    return elems[0].text.strip()

trackerfile=open('Amazon Price Tracker.txt','a')

trackerfile.write('The prices as of '+ str(datetime.date(datetime.now()))+' are:\n')

for k, v in wishlist.items():
    #url_list=' '.join(list(wishlist.values()))
    price=getAmazonPrice(v)   #(' '.join(list(wishlist.values())))
    book=(k)
    trackerfile.write(f"\n{book}\ncosts: {price}\n")

trackerfile.close()
