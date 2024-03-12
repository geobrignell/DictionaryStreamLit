import streamlit as st
import requests
import json

st.write("# :rainbow[Pretty Dictionary]")
st.markdown('''
    :red[A] :orange[free] :green[online] :blue[dictionary,] :violet[just]
    :red[for] :orange[you].''')


word = st.text_input("Enter your favourite word:")
st.write("#")
st.write(f"### {word}")
st.write("----------------------------------")



try:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    resp = requests.get(url)
    info = resp.json()


    definitions = info[0]["meanings"]

    for desc in definitions:
        st.write(f"Part of speech : {desc['partOfSpeech']}")
        st.write(f"Definintion : {desc['definitions'][0]['definition']}")   
        st.write("----------------------------------")

except:
    st.write("Please enter a valid word")