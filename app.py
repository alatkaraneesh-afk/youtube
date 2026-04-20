import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# DISGUISE: Changes title to look like a science tool
st.set_page_config(page_title="Chemical Formula Database", page_icon="🧪")
st.title("Molecular Research Tool")
st.caption("Secure Portal for Academic Research")

target_url = st.text_input("Source Identifier (URL):", placeholder="https://example.com")

if target_url:
    try:
        # Protocol check
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url
            
        st.info("Mirroring resource from cloud archive...")
        
        # The Server (not your computer) fetches the page, bypassing local iBoss DNS blocks
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(target_url, headers=headers, timeout=15)
        
        # Rewrite links using BeautifulSoup to fix relative paths
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup.find_all(['img', 'link', 'script', 'a']):
            attr = 'src' if tag.name in ['img', 'script'] else 'href'
            if tag.has_attr(attr):
                tag[attr] = urljoin(target_url, tag[attr])

        # Display cleaned HTML directly to bypass X-Frame-Options
        st.components.v1.html(str(soup), height=800, scrolling=True)
        
    except Exception as e:
        st.error("Document not found in archive. Please check the identifier.")

# DISGUISE: Notes section to look busy
st.divider()
st.text_area("Analysis Workspace:", placeholder="Enter your field notes here for grading...")
