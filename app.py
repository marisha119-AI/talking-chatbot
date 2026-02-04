import streamlit as st

# Set up the page
st.set_page_config(page_title="My Chatbot", layout="wide")

# Method 1: Direct HTML String
# Paste your entire HTML code as a string here
html_string = """
<!DOCTYPE html>
<html>
<head>
    <!-- Your entire <head> section with CSS -->
</head>
<body>
    <!-- Your entire chatbot HTML body -->
</body>
</html>
"""

st.html(html_string, unsafe_allow_html=True)

# Method 2: Load from an HTML File (if you keep HTML separate)
# with open('chatbot_interface.html', 'r', encoding='utf-8') as f:
#     html_string = f.read()
# st.html(html_string, unsafe_allow_html=True)