import resource
from tkinter import Image
import uuid
import streamlit as st
import streamlit_pydantic as sp

from PIL import Image

from model.main_page import MAINPAGE
from services.form_model import form_dyn
from utils.git_hub import STGithub
from utils.operations import ToolBox

from diagram.aws.aws_resources import GraphView

def smart_tech_app():

    git_hub = STGithub()
    toolbox = ToolBox()

    providers = toolbox.byaml_2_dict(git_hub.getitemcontent('cloudP.yml','kahunat3k/k-ops/yaml/yaml')

    #st.set_page_config(page_title='Infra as Conde', layout='wide', initial_sidebar_state='auto')

    if 'id_session' not in st.session_state:

        st.session_state.id_session = str(uuid.uuid4()).replace('-','')

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden ;}
        </style>
    """

    st.markdown(hide_menu_style, unsafe_allow_html=True)
    
    st.sidebar.title('SREOps')

    st.title('Request new infrastructure')

    cloud_provider = st.sidebar.selectbox('Providers', options=(providers['providers']))

    kind_apps = toolbox.byaml_2_dict(git_hub.getitemcontent(f"{cloud_provider}/kind_apps.yml",'kahunat3k/k-ops/yaml'))

    type_app = st.sidebar.selectbox('Type App',options=(kind_apps['type_apps']))
             
    selected = st.sidebar.multiselect(f"Choice {cloud_provider} Resources",options=(kind_apps[type_app]['resources']),default=None)
    
    tabs = st.tabs(['Project Specification','Json result','Preview'])
    
    data_json = [] 
    
    with tabs[0]:
        
        # Main Tab
        with st.expander(label='Application data',expanded=False):
            
            with st.form(key='main_page'):
                    
                data_main = sp.pydantic_input(key='data_main', model=MAINPAGE)

                submit_button_main = st.form_submit_button(label='Submit')
                            
                if data_main:

                    st.json(data_main)
                    
                    data_json.append({'main' : data_main})
    

        if selected != None:

            with st.spinner('Wait for it...'):

                for item in selected:

                    result_form = form_dyn(cloud=cloud_provider, resource=item.lower())

                    data_json.append(result_form)
        
    with tabs[1]:
        
        st.json(data_json)

    # For debug propose
    #'Session inspect', st.session_state

    if selected != []:

        make_preview = GraphView()

        make_preview.make_diagram(cloud=cloud_provider,resources=selected,data_json=data_json)

        with tabs[2]:

                aws_img = Image.open('aws.png')

                st.image(aws_img)

st.set_page_config(page_title='Infra as Conde', layout='wide', initial_sidebar_state='auto')

# Init app
if __name__ == '__main__':
    
    smart_tech_app()
