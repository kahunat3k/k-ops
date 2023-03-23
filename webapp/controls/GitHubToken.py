from email.policy import default
import uuid
import streamlit as st

from utils.git_hub import STGithub


def smart_tech_app():

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden ;}
        </style>
    """

    st.markdown(hide_menu_style, unsafe_allow_html=True)
    
    st.title('Access control')

    if 'id_session' not in st.session_state and 'token_repo' not in st.session_state:
     
        token_developer = st.text_input(label="Your personal token access: ")

        if token_developer:

            git_hub = STGithub(token=token_developer)

            if 'repos_loaded' not in st.session_state:
                
                with st.spinner('Waiting load repos...'):

                    st.session_state.repos_loaded =  git_hub.getrepos()

            select_repo = st.selectbox(label='Repositories', options=(st.session_state.repos_loaded))

            if select_repo in st.session_state.repos_loaded and select_repo != '':

                def login():

                    st.session_state.id_session = str(uuid.uuid4()).replace('-','')
                    st.session_state.token_repo = token_developer
                    st.session_state.user_name = git_hub.git_hub.get_user().name

                    return True


                if st.button(label='Go a head ' + str(git_hub.git_hub.get_user().name) ,on_click=login):

                    return True
    else:

        return False

# Init app
if __name__ == '__main__':
    
    smart_tech_app()
