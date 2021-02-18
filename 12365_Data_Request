import requests
from bs4 import BeautifulSoup
import pandas as pd

# requests.get page data from 12365
def get_page_content(request_url):
    
    # headers for pretending browser
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text

    # make soup with specific paerse 'html.parser'
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

# parse information from the website
def analysis(soup):
    temp = soup.find('div',class_="tslb_b")
    
    # dataframe for saving information
    df = pd.DataFrame(columns = ['ID', 'Brand', 'Model', 'Type', 'Issues', 'Issues_Tag', 'Date', 'Status'])
    
    # for specific information with tags 'tr' -> 'td'
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        
        # parsing and assignment
        if len(td_list) > 0:
            ID, Brand, Model, Type, Issues, Issues_Tag, Date, Status = td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            
            temp['ID'], temp['Brand'], temp['Model'], temp['Type'], temp['Issues'], temp['Issues_Tag'], temp['Date'], temp['Status'] = ID, Brand, Model, Type, Issues, Issues_Tag, Date, Status
            df = df.append(temp,ignore_index=True)
            
            

                

    
    return df

page_num = 1
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'

result = pd.DataFrame(columns = ['ID', 'Brand', 'Model', 'Type', 'Issues', 'Issues_Tag', 'Date', 'Status'])

# iteration of 10 times  
for i in range(page_num):
    request_url = base_url+str(i+1)+'.shtml'
    soup = get_page_content(request_url)
    print(request_url)
    df = analysis(soup)
    print(df)
    result = result.append(df)
  
    
    
result.to_excel('C:/Users/lixiangwei/Desktop/12365auto.xlsx', index=False)


#%%
# parsing the details of complaints
for td in td_list:
    tag = {}
    span_list = soup.find_all('a')
    # print(span_list['href'])
    bw = td.select('span a')[0].string
    span_list_wt = td.find('span', class_='wt').get_text()
    if len(span_list) > 0:
        tag = span_list[0].text + span_list[1].text
        tag['tag'] = tag
            
        df = df.append(bw)
