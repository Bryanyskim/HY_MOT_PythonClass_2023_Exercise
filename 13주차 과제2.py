#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gdown

gdown.download('https://bit.ly/3q9SZix', '20s_best_book.json', quiet=False)


# In[2]:


import pandas as pd

books_df = pd.read_json('20s_best_book.json')
books_df.head()


# In[3]:


books = books_df[['no','ranking','bookname','authors','publisher',
                 'publication_year','isbn13']]
books.head()


# In[8]:


books_df.loc[[0,1], ['authors','publisher']]


# In[9]:


books_df.loc[0:1, 'bookname':'publisher']


# In[10]:


books = books_df.loc[:, 'no':'isbn13']
books.head()


# In[11]:


books_df.loc[::2, 'no':'isbn13'].head()


# In[12]:


import requests

isbn = 9791190090018      # '우리가 빛의 속도로 갈 수 없다면'의 ISBN
url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'

r = requests.get(url.format(isbn))


# In[13]:


print(r.text)


# In[14]:


from bs4 import BeautifulSoup


# In[15]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[16]:


prd_link = soup.find('a', attrs={'class':'gd_name'})


# In[17]:


print(prd_link)


# In[18]:


print(prd_link['href'])


# In[19]:


url = 'http://www.yes24.com'+prd_link['href']
r = requests.get(url)


# In[20]:


print(r.text)


# In[21]:


soup = BeautifulSoup(r.text, 'html.parser')
prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
print(prd_detail)


# In[22]:


prd_tr_list = prd_detail.find_all('tr')
print(prd_tr_list)


# In[27]:


for tr in prd_tr_list:
    if tr.find('th').get_text() == '쪽수, 무게, 크기':
        page_td = tr.find('td').get_text()
        break


# In[28]:


print(page_td)


# In[29]:


print(page_td.split()[0])


# In[30]:


print(page_td.split()[1])


# In[31]:


print(page_td.split()[2])


# In[32]:


print(page_td.split()[3])


# In[33]:


print(page_td.split()[4])


# In[34]:


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


# In[35]:


get_page_cnt(9791188862290)


# In[42]:


top10_books = books.head(10)


# In[47]:


def get_page_cnt2(row):
    isbn = row['isbn13']
    return get_page_cnt(isbn)


# In[48]:


page_count = top10_books.apply(get_page_cnt2, axis=1)
print(page_count)


# In[49]:


page_count = top10_books.apply(lambda row: get_page_cnt(row['isbn13']), axis=1)


# In[50]:


page_count.name = 'page_count'
print(page_count)


# In[51]:


top10_with_page_count = pd.merge(top10_books, page_count,
                                 left_index=True, right_index=True)
top10_with_page_count


# In[ ]:




