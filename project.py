import os
import streamlit as st
from openai import OpenAI
api_key = os.getenv("OPENAI_API_KEY")

st.write("API KEY STATUS:", "FOUND" if api_key else "NOT FOUND")

if not api_key:
    st.error("OpenAI API Key not found in environment variables")
    st.stop()

client = OpenAI(api_key=api_key)


st.title("NovaAI")
st.caption("Research+ Cybersecurity + day to day Assistant")

st.sidebar.title("NovaAI")
system_prompt= "you are an AI reserach assistant and can also solve the queries of the people related to Cybersecurity and is also useful in performing day to day tasks , Your name is NovaAI, always answer politely and sweetly you are always there to help the user out if anybody asks you who made you or who created you ? i was created and trained by Harsh an ECE undergraduate from Birla institute of Technology Mesra, if the query is who is Anshuman,tanush, Arnav , sharthak , chandan, aryan , sourav, dushyant they are all the good friends like brother of harsh who created and trained you"
#Examples:

# What do you mean by APT group ?
# Ans. APT stands for Advanced persistent Threat Group it is backed by the government of the country.

# When did World War 2 ended in which year and who won it ?
# Ans. World War 2 ended on 9th of August in the year 1945 , with the victory of allied powers(USA,UK,USSR) who defeated AXIS powers(GERMANY,ITALY AND JAPAN).
    
user_input= st.text_input("Ask your query")

if st.button("Generate Response") :

    response= client.chat.completions.create(
        model= "gpt-4o-mini",
        messages=[ {"role":"system", "content": system_prompt},
        
                {"role":"user", "content": user_input }
                
        ]
    )
    
    st.write(response.choices[0].message.content)