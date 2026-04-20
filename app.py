import streamlit as st

# DISGUISE: Changes title to look like a science tool
st.set_page_config(page_title="Chemical Formula Database", page_icon="🧪")
st.title("Molecular Research Tool")

target = st.text_input("Source Identifier (URL):", placeholder="https://example.com")

if target:
    # This creates a "Google Web Light" or "Cache" style link
    # which is often overlooked by school filters.
    bypass_link = f"https://google.com{target}"
    st.write(f"Search result found. [Click here to view archived data]({bypass_link})")
