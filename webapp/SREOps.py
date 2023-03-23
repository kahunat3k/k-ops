import uuid
import streamlit as st
import streamlit_pydantic as sp

from PIL import Image

from model.main_page import MAINPAGE
from services.form_model import form_dyn
from utils.git_hub import STGithub
from utils.operations import ToolBox
from controls import GitHubToken

from diagram.aws.aws_resources import GraphView

def smart_tech_app():
    
    st.set_page_config(page_title='Infra as Code', layout='wide', initial_sidebar_state='auto')

    hide_menu_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden ;}
    </style>
    """

    st.markdown(hide_menu_style, unsafe_allow_html=True)

    st.markdown(hide_menu_style, unsafe_allow_html=True)
    

    git_hub = STGithub()
    toolbox = ToolBox()


    if 'id_session' not in st.session_state and 'token_repo' not in st.session_state:

        if not GitHubToken.smart_tech_app():

            return False

    else:

        st.sidebar.title('SREOps')
        st.sidebar.write('User \n' + st.session_state.user_name) 

        st.title('Infra as Code')

        providers = toolbox.byaml_2_dict(git_hub.getitemcontent('cloudP.yml','kahunat3k/k-ops'))

        cloud_provider = st.sidebar.selectbox('Providers', options=(providers['providers']))

        kind_apps = toolbox.byaml_2_dict(git_hub.getitemcontent(f"{cloud_provider}/kind_apps.yml",'kahunat3k/k-ops'))

        type_app = st.sidebar.selectbox('Type App',options=(kind_apps['type_apps']))
                
        selected = st.sidebar.multiselect(f"Choice {cloud_provider} Resources",options=(kind_apps[type_app]['resources']),default=None)

        def logout():
            st.session_state.__delattr__('id_session')
            st.session_state.__delattr__('token_repo')

            return True

        if st.sidebar.button(label='Logout',on_click=logout):

            st.session_state.token_repo = ''
            st.session_state.id_session = ''
 
            return False

        tabs = st.tabs(['Project Specification','Json result','Preview'])
        
        data_json = [] 
        
        with st.form(key="main_form"):
        
            with tabs[0]:
                
                # Main Tab
                with st.expander(label='Application data',expanded=False):

                    data_main = sp.pydantic_input(key='data_main', model=MAINPAGE)
                                
                    if data_main:

                        # st.json(data_main)
                        
                        data_json.append({'main' : data_main})
        

                if selected != None :

                    with st.spinner('Wait for it...'):

                        for item in selected:

                            result_form = form_dyn(cloud=cloud_provider, resource=item.lower())

                            data_json.append(result_form)
            
            submit_button_main = st.form_submit_button(label='Submit')
        
        with tabs[1]:
            
            st.json(data_json)

        # For debug propose
        # 'Session inspect', st.session_state

        if selected != []:

            make_preview = GraphView()

            make_preview.make_diagram(cloud=cloud_provider,resources=selected,data_json=data_json)

            with tabs[2]:

                    aws_img = Image.open('aws.png')

                    st.image(aws_img)


# Init app
if __name__ == '__main__':
    
    result = smart_tech_app()

