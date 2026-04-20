import streamlit as st
import streamlit.components.v1 as components

# 1. DISGUISE: Changes the browser tab title and icon
st.set_page_config(page_title="AP History - Primary Source Analysis", page_icon="📝")

# 2. DISGUISE: Page header looks like schoolwork
st.title("Primary Source Video Analysis")
st.caption("Student Workspace - Semester 2 Project")

# 3. INPUT: Disguised as a source lookup
source_url = st.text_input("Enter Document/Source URL:", placeholder="Paste link here...")

if source_url:
    # Logic to convert YouTube links to an unblocked proxy (Invidious)
    if "youtube.com" in source_url or "youtu.be" in source_url:
        # Extract the Video ID
        if "v=" in source_url:
            video_id = source_url.split("v=")[1].split("&")[0]
        else:
            video_id = source_url.split("/")[-1]

        # Use a high-quality Invidious proxy (less likely to be blocked than youtube-nocookie)
        proxy_url = f"https://tux.rs{video_id}"

        st.info("Loading educational resource from archive...")
        
        # The Embed: Includes the fix for Error 153
        components.html(f"""
            <iframe src="{proxy_url}" 
                    width="100%" height="450" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    referrerpolicy="no-referrer"
                    allowfullscreen>
            </iframe>
        """, height=480)
    else:
        # For non-YouTube sites, tries a standard iframe
        components.iframe(source_url, height=600, scrolling=True)

# 4. DISGUISE: A notes section to look busy
st.divider()
st.subheader("Analysis Notes")
st.text_area("Observations:", placeholder="Type your analysis here for grading...")
st.button("Save Draft")
