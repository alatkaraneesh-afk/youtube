import streamlit as st
import yt_dlp
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 1. DISGUISE: Changes the browser tab and icon
st.set_page_config(page_title="Advanced Calculus Review", page_icon="📐")
st.title("Resource Data Stream")
st.caption("Student Workspace - AP Statistics Project")

# 2. INPUT: Disguised as a source identifier
url = st.text_input("Enter Document Identifier (URL):", placeholder="Paste source link here...")

if url:
    try:
        # Check if it's a YouTube link
        if "youtube.com" in url or "youtu.be" in url:
            # yt-dlp fetches the video on the SERVER, bypassing iBoss DNS blocks
            ydl_opts = {'format': 'best[ext=mp4]', 'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                st.info("Fetching data from cloud archive...")
                info = ydl.extract_info(url, download=False)
                # st.video uses the direct stream, bypassing iframe-based blocks
                st.video(info.get('url'))
        else:
            # For general sites: Fetches raw HTML to bypass X-Frame-Options
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Fix relative links so images and styles load
            for tag in soup.find_all(['img', 'link', 'script', 'a']):
                attr = 'src' if tag.name in ['img', 'script'] else 'href'
                if tag.has_attr(attr):
                    tag[attr] = urljoin(url, tag[attr])
            st.components.v1.html(str(soup), height=800, scrolling=True)
            
    except Exception as e:
        st.error("Document not found in archive. Please check the identifier.")

# 3. DISGUISE: Notes section to look like you're working
st.divider()
st.text_area("Analysis Summary:", placeholder="Type your observations for the assignment here...")
st.button("Save to Gradebook")
