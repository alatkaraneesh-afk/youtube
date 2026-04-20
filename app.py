import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# 1. DISGUISE
st.set_page_config(page_title="Global Economic Database", page_icon="🌐")
st.title("Resource Mirror & Data Viewer")
st.caption("Secure Portal for Academic Research")

# 2. INPUT
target_url = st.text_input("Enter Database URL:", placeholder="https://example.com")

if target_url:
    try:
        # If no protocol is provided, add https
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url
            
        st.info("Mirroring resource...")
        
        # The Server (not your computer) fetches the page
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(target_url, headers=headers, timeout=10)
        
        # Use BeautifulSoup to fix links so they stay inside the proxy
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Rewriting relative URLs for images/styles so they load through the proxy
        for tag in soup.find_all(['img', 'link', 'script', 'a']):
            attr = 'src' if tag.name in ['img', 'script'] else 'href'
            if tag.has_attr(attr):
                # Joins the relative path with the original site URL
                tag[attr] = urljoin(target_url, tag[attr])

        # Display the "cleaned" HTML
        # This bypasses X-Frame-Options because it's just raw code now
        st.components.v1.html(str(soup), height=800, scrolling=True)
        
    except Exception as e:
        st.error(f"Error accessing database: {e}")

# 3. DISGUISE
st.divider()
st.text_area("Analysis Workspace:", placeholder="Enter your field notes here...")
