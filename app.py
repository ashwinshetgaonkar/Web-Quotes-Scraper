import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup

topic_list_df=pd.read_csv('topics_list.csv')

# st.markdown("### Welcome!")

st.title('Quotes Scraper')
st.markdown('---')
topic_names=topic_list_df['Topic Name'].to_list()

st.markdown('#### Select the topic on which you want to see Quotes:')
option = st.selectbox(
     '',
      topic_names
)
# st.markdown('---')

# st.write('You selected:', option)

topic_url=topic_list_df.loc[topic_list_df['Topic Name']==option,'Topic URL'].to_list()
# st.write('visit:', topic_url[0])

st.write(f'Quotes on {option} are as follows:')
st.markdown('---')

response=requests.get(topic_url[0])
soup=BeautifulSoup(response.text,'html.parser')
quotes_selection_class='grid-item qb clearfix bqQt'
quotes_tags=soup.find_all('div',{'class':quotes_selection_class})

quotes = []
for i in range(len(quotes_tags)):
    quote = {}
    # extract the quote
    # print(i)
    quote_tag = quotes_tags[i].find('a', class_='b-qt')
    quote['Quote'] = quote_tag.text.strip()
    # extract the author
    author = quotes_tags[i].find('a', class_='bq-aut')
    quote['Author'] = author.text.strip()

    quotes.append(quote)

quotes_df=pd.DataFrame(quotes).sample(frac=1.0)
df=quotes_df.head(10)
for row in df.itertuples():
    _,quote,author=row
    st.write(quote)
    st.write('by ',author)
    st.markdown('---')

    # st.text(quote)
# st.dataframe(quotes_df.head(10))


