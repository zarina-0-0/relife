import streamlit as st

# --- PAGE SETUP ---
main_page = st.Page(
    page="extra/main.py",
    title="Relife",
    icon=":material/home:",
    default=True
)

about_page = st.Page(
    page="extra/about_us.py",
    title="Our mission",
    icon=":material/account_circle:",
)

tables_page = st.Page(
    page="extra/accountings.py",
    title="Our accounting",
    icon=":material/bar_chart:",
)

nav = st.navigation(pages=[main_page, about_page, tables_page])
nav.run()