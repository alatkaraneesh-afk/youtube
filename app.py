import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import yt_dlp

# DISGUISE: Tab and Header
st.set_page_config(page_title="Advanced Calculus Review", page_icon="📐")
st.title("Resource Data Stream")
st.caption("Student Workspace - Semester 2 Project")

# INPUT
url = st.text_input("Enter Document Identifier (URL):", placeholder="Paste link here...")

if url:
    try:
        # Check if it's a Video (YouTube)
        if "youtube.com" in url or "youtu.be" in url:
            st.info("Streaming from cloud archive...")
            ydl_opts = {'format': 'best[ext=mp4]', 'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # st.video uses a direct stream, NO iframe. iBoss can't block this easily.
                st.video(info.get('url'))
        
        # General Website Proxy
        else:
            st.info("Mirroring site content...")
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            
            # BEAUTIFUL SOUP: This pulls the raw code and "cleans" it
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Fix relative links so images and styles still load
            for tag in soup.find_all(['img', 'link', 'script', 'a']):
                attr = 'src' if tag.name in ['img', 'script'] else 'href'
                if tag.has_attr(attr):
                    tag[attr] = urljoin(url, tag[attr])
            
            # Use raw markdown/HTML injection (NO IFRAME used here)
            st.markdown(str(soup), unsafe_allow_html=True)

    except Exception as e:
        st.error("Document not found. The server may be blocking the request.")

# DISGUISE: Notes section to look like schoolwork
st.divider()
st.text_area("Analysis Workspace:", placeholder="Type your findings for the assignment here...")
st.button("Save to Gradebook")
