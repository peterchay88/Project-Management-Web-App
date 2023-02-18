import streamlit as st

st.text("Known issues:\n"
        "When adding the first item it creates an extra blank space.\n"
        "When completing more than one item it will keep the last task completed but then complete the one after the "
        "last selected task\n"
        "If you are entering a a number followed by \".\" it will return a blank value (Ex: 23.)")