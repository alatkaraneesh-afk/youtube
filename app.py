import streamlit as st
import requests

st.title("Private Web Proxy")

# Input for the website you want to visit
target_url = st.text_input("Enter URL (e.g., https://example.com):")

if target_url:
    try:
        # Fetch the content of the target website
        # We use headers to make the request look like it's coming from a real browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(target_url, headers=headers)
        
        # Display the content. Warning: This is a simple text/HTML view.
        # Complex sites with lots of JS may not load perfectly.
        st.code(f"Status Code: {response.status_code}")
        st.components.v1.html(response.text, height=800, scrolling=True)
        
    except Exception as e:
        st.error(f"Could not load site: {e}")
import streamlit as st
import streamlit.components.v1 as components

st.title("My Unblocked Video App")

# Your YouTube Embed Code with the Error 153 fix
video_html = """
<iframe width="100%" height="400" 
    src="https://youtube-nocookie.com" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen>
</iframe>
"""

# Render the HTML in your app
components.html(video_html, height=450)
