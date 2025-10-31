import streamlit as st
from Helper.login import auth

if not st.user.is_logged_in:
    auth.login(st)



if st.user.is_logged_in:
    auth.logout(st)