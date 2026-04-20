import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

# DISGUISE: Tab and Header
st.set_page_config(page_title="Data Archive - Research", page_icon="📂")
st.title("Academic Source Mirror")

# INPUT
target = st.text_input("Source URL:", placeholder="https://example.com")

if target:
    if not target.startswith("http"):
        target = "https://" + target
        
    try:
        # STEP 1: The server (Cloud) fetches the page, NOT your school computer.
        # This bypasses the local iBoss filter.
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = session.get(target, headers=headers, timeout=10)
        
        # STEP 2: Rewrite links so they don't break
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup.find_all(['a', 'img', 'link', 'script']):
            attr = 'href' if tag.name in ['a', 'link'] else 'src'
            if tag.has_attr(attr):
                # Makes links absolute (points to the real website)
                tag[attr] = urllib.parse.urljoin(target, tag[attr])

        # STEP 3: Inject the cleaned HTML directly.
        # This bypasses the "Firefox Can't Open This Page" error because
        # we are not "embedding" the site; we are displaying its code.
        st.components.v1.html(soup.prettify(), height=800, scrolling=True)

    except Exception as e:
        st.error(f"Access Denied: Resource is restricted or offline.")

# DISGUISE: Notes
st.divider()
st.text_area("Field Notes:", placeholder="Summarize your findings...")
