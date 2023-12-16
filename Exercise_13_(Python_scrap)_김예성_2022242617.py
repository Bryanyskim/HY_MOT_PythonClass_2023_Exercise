#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gdown


# In[2]:


import gdown

gdown.download('https://bit.ly/3GisL6J', 'ns_book4.csv', quiet=False)


# In[3]:


import pandas as pd

ns_book4 = pd.read_csv('ns_book4.csv', low_memory=False)
ns_book4.head()


# In[4]:


ns_book4.info()


# In[5]:


ns_book4.info(memory_usage='deep')


# In[6]:


ns_book4.isna().sum()


# In[7]:


ns_book4.loc[0, '도서권수'] = None
ns_book4['도서권수'].isna().sum()


# In[8]:


ns_book4.head(2)


# In[9]:


ns_book4.loc[0, '도서권수'] = 1
ns_book4 = ns_book4.astype({'도서권수':'int32', '대출건수': 'int32'})
ns_book4.head(2)


# In[10]:


ns_book4.loc[0, '부가기호'] = None
ns_book4.head(2)


# In[11]:


import numpy as np

ns_book4.loc[0, '부가기호'] = np.nan
ns_book4.head(2)


# In[12]:


set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = ''

ns_book4['세트 ISBN'].isna().sum()


# In[13]:


set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
ns_book4.loc[set_isbn_na_rows, '세트 ISBN']


# In[14]:


set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = ''


# In[15]:


ns_book4


# In[16]:


set_isbn_na_rows = ns_book4['세트 ISBN'].isna()
ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = ''

ns_book4['세트 ISBN'].isna().sum()


# In[17]:


ns_book4.fillna('없음').isna().sum()


# In[18]:


ns_book4


# In[19]:


ns_book4['부가기호'].fillna('없음').isna().sum()


# In[20]:


ns_book4.fillna({'부가기호':'없음'}).isna().sum()


# In[21]:


ns_book4.replace([np.nan, '2021'], ['없음', '21']).head(2)


# In[22]:


ns_book4.replace({np.nan: '없음', '2021': '21'}).head(2)


# In[23]:


ns_book4.replace({'부가기호': np.nan}, '없음').head(2)


# In[24]:


ns_book4.replace({'부가기호': {np.nan: '없음'}, '발행년도': {'2021': '21'}}).head(2)


# In[25]:


ns_book4.replace({'발행년도': {'2021': '21'}})[100:102]


# In[26]:


ns_book4.replace({'발행년도': {r'\d\d(\d\d)': r'\1'}}, regex=True)[100:102]


# In[27]:


ns_book4.replace({'발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]

#원본은 바뀌지 않는 것임


# In[28]:


ns_book4.replace({'저자': {r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]


# In[29]:


ns_book4.replace({
                  '저자': {r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}
                 }, regex=True)[100:102]


# In[30]:


ns_book4.replace({
                  '저자': {r'(.*)\s\(지은이\)\,(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}
                 }, regex=True)[100:102]


# In[31]:


ns_book4['발행년도'].str.contains('1988').sum()


# In[32]:


ns_book4


# In[33]:


ns_book4['발행년도'].str.contains('1988').sum()


# In[34]:


ns_book4['발행년도'].str.contains('1988')


# In[35]:


ns_book4['발행년도'].str.contains('1988').sum()


# In[36]:


invalid_number = ns_book4['발행년도'].str.contains('\D', na=True)
print(invalid_number.sum())
ns_book4[invalid_number].head()


# In[37]:


invalid_number = ns_book4['발행년도'].str.contains('\D', na=True)


# In[38]:


invalid_number = ns_book4['발행년도'].str.contains('\D', na=True)
print(invalid_number.sum())


# In[39]:


ns_book4[invalid_number].head()


# In[40]:


ns_book5 = ns_book4.replace({'발행년도':r'.*(\d{4}).*'}, r'\1', regex=True)
ns_book5[invalid_number].head()


# In[41]:


ns_book5


# In[42]:


unkown_year = ns_book5['발행년도'].str.contains('\D', na=True)
print(unkown_year.sum())
ns_book5[unkown_year].head()


# In[43]:


ns_book5.loc[unkown_year, '발행년도'] = '-1'
ns_book5 = ns_book5.astype({'발행년도': 'int32'})


# In[44]:


ns_book5['발행년도'].gt(4000).sum()


# In[45]:


dangun_yy_rows = ns_book5['발행년도'].gt(4000)


# In[46]:


dangun_yy_rows = ns_book5['발행년도'].gt(4000)
ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333


# In[47]:


dangun_year = ns_book5['발행년도'].gt(4000)
print(dangun_year.sum())
ns_book5[dangun_year].head(2)


# In[48]:


ns_book5.loc[dangun_year, '발행년도'] = -1


# In[49]:


old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900)
ns_book5[old_books]


# In[50]:


ns_book5.loc[old_books, '발행년도'] = -1


# In[51]:


ns_book5['발행년도'].eq(-1).sum()


# In[52]:


d = {"name": "혼자 공부하는 데이터 분석"}

print(d['name'])


# In[53]:


import json


# In[54]:


d_str = json.dumps(d, ensure_ascii=False)
print(d_str)


# In[55]:


print(type(d_str))


# In[56]:


d2 = json.loads(d_str)

print(d2['name'])


# In[57]:


print(type(d2))


# In[58]:


d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022}')

print(d3['name'])
print(d3['author'])
print(d3['year'])


# In[59]:


d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", "author": ["박해선","홍길동"],                   "year": 2022}')

print(d3['author'][1])


# In[60]:


d4_str = """
[
  {"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022},
  {"name": "혼자 공부하는 머신러닝+딥러닝", "author": "박해선", "year": 2020}
]
"""
d4 = json.loads(d4_str)

print(d4[0]['name'])


# In[61]:


import pandas as pd

pd.read_json(d4_str)


# In[62]:


type(pd.read_json(d4_str))


# In[63]:


pd.DataFrame(d4)


# In[64]:


x_str = """
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""


# In[65]:


import xml.etree.ElementTree as et

book = et.fromstring(x_str)


# In[66]:


print(type(book))


# In[67]:


print(book.tag)


# In[68]:


book_childs = list(book)

print(book_childs)


# In[69]:


name, author, year = book_childs

print(name.text)
print(author.text)
print(year.text)


# In[70]:


name = book.findtext('name')
author = book.findtext('author')
year = book.findtext('year')

print(name)
print(author)
print(year)


# In[71]:


x2_str = """
<books>
    <book>
        <name>혼자 공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name>혼자 공부하는 머신러닝+딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>
"""


# In[72]:


books = et.fromstring(x2_str)

print(books.tag)


# In[73]:


for book in books.findall('book'):
    name = book.findtext('name')
    author = book.findtext('author')
    year = book.findtext('year')

    print(name)
    print(author)
    print(year)
    print()


# In[79]:


get_ipython().system('pip3 install --upgrade pandas')


# In[80]:


get_ipython().system('pip3 install --upgrade pip')


# In[81]:


import requests


# In[84]:


url = "http://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"


# In[85]:


r = requests.get(url)


# In[86]:


data = r.json()

print(data)


# In[87]:


data


# In[88]:


data['response']['docs']


# In[89]:


books = []
for d in data['response']['docs']:
    books.append(d['doc'])


# In[90]:


books = [d['doc'] for d in data['response']['docs']]


# In[91]:


books


# In[92]:


books_df = pd.DataFrame(books)

books_df


# In[93]:


books_df.to_json('20s_best_book.json')


# In[94]:


import gdown

gdown.download('https://bit.ly/3q9SZix', '20s_best_book.json', quiet=False)


# In[95]:


import pandas as pd

books_df = pd.read_json('20s_best_book.json')
books_df.head()


# In[96]:


books = books_df[['no','ranking','bookname','authors','publisher',
                 'publication_year','isbn13']]
books.head()


# In[97]:


books_df.loc[[0,1], ['bookname','authors']]


# In[98]:


books_df.loc[0:1, 'bookname':'authors']


# In[99]:


books = books_df.loc[:, 'no':'isbn13']
books.head()


# In[100]:


books_df.loc[::2, 'no':'isbn13'].head()


# In[101]:


import requests

isbn = 9791190090018      # '우리가 빛의 속도로 갈 수 없다면'의 ISBN
url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
r = requests.get(url.format(isbn)


# In[102]:


print(r.text)


# In[104]:


from bs4 import BeautifulSoup


# In[105]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[106]:


prd_link = soup.find('a', attrs={'class':'gd_name'})


# In[107]:


print(prd_link)


# In[108]:


print(prd_link['href'])


# In[109]:


url = 'http://www.yes24.com'+prd_link['href']
r = requests.get(url)


# In[110]:


print(r.text)


# In[111]:


soup = BeautifulSoup(r.text, 'html.parser')
prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
print(prd_detail)


# In[112]:


prd_tr_list = prd_detail.find_all('tr')
print(prd_tr_list)


# In[113]:


for tr in prd_tr_list:
    if tr.find('th').get_text() == '쪽수, 무게, 크기':
        page_td = tr.find('td').get_text()
        break


# In[114]:


print(page_td)


# In[115]:


print(page_td.split()[0])


# In[116]:


def get_page_cnt(isbn):
    # Yes24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser')   # HTML 파싱
    # 검색 결과에서 해당 도서를 선택합니다.
    prd_info = soup.find('a', attrs={'class':'gd_name'})
    if prd_info == None:
        return ''
    # 도서 상세 페이지를 가져옵니다.
    url = 'http://www.yes24.com'+prd_info['href']
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # 상품 상세정보 div를 선택합니다.
    prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
    # 테이블에 있는 tr 태그를 가져옵니다.
    prd_tr_list = prd_detail.find_all('tr')
    # 쪽수가 들어 있는 th를 찾아 td에 담긴 값을 반환합니다.
    for tr in prd_tr_list:
        if tr.find('th').get_text() == '쪽수, 무게, 크기':
            return tr.find('td').get_text().split()[0]
    return ''


# In[117]:


get_page_cnt(9791190090018)


# In[118]:


top10_books = books.head(10)


# In[119]:


def get_page_cnt2(row):
    isbn = row['isbn13']
    return get_page_cnt(isbn)


# In[121]:


page_count = top10_books.apply(get_page_cnt2, axis=1)
print(page_count)


# In[122]:


page_count = top10_books.apply(lambda row: get_page_cnt(row['isbn13']), axis=1)


# In[123]:


page_count.name = 'page_count'
print(page_count)


# In[124]:


top10_with_page_count = pd.merge(top10_books, page_count,
                                 left_index=True, right_index=True)
top10_with_page_count


# In[125]:


df1 = pd.DataFrame({'col1': ['a','b','c'], 'col2': [1,2,3]})
df1


# In[126]:


df2 = pd.DataFrame({'col1': ['a','b','d'], 'col3': [10,20,30]})
df2


# In[127]:


pd.merge(df1, df2, on='col1')


# In[128]:


pd.merge(df1, df2, how='left', on='col1')


# In[129]:


pd.merge(df1, df2, how='right', on='col1')


# In[130]:


pd.merge(df1, df2, how='outer', on='col1')


# In[131]:


pd.merge(df1, df2, left_on='col1', right_on='col1')


# In[132]:


pd.merge(df1, df2, left_on='col2', right_index=True)


# In[ ]:




