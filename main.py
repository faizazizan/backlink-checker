import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_backlinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        backlinks = []

        for link in links:
            href = link['href']
            if href.startswith('http'):
                backlinks.append(href)

        return backlinks
    except requests.RequestException as e:
        st.error(f"Error fetching the URL: {e}")
        return []

def main():
    st.title("Backlink Analyzer")

    url = st.text_input("Enter the URL of the page to analyze:")
    if st.button("Analyze"):
        if url:
            with st.spinner("Fetching backlinks..."):
                backlinks = fetch_backlinks(url)
                if backlinks:
                    st.subheader("Backlinks Found:")
                    for backlink in backlinks:
                        st.write(backlink)
                else:
                    st.write("No backlinks found or error occurred.")
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()
