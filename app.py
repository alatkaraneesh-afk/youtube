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
