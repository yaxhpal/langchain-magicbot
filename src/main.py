import streamlit as st

st.title('This is Magic Bot')
guide = st.sidebar.selectbox('Select the guide', [
    ('Salesforce', "sf"),
    ('Zoho', "zoho"),
    ("SMS Magic API", "smsmagic")
])
print(guide)

