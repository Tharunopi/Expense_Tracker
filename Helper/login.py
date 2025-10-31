import streamlit

class auth:
    @staticmethod
    def login(st:streamlit):
        st.header("Login", divider="rainbow")
        st.button("Google Login", on_click=st.login)
    
    @staticmethod
    def logout(st:streamlit):
        st.button("Logout", on_click=st.logout)