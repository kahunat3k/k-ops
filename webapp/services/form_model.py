import streamlit as st
import streamlit_pydantic as sp
from  importlib import import_module

import os

from utils.data_model import DynModel

def form_dyn(cloud:str,resource:str) -> dict:
    
    dynmodel = DynModel(id_session=st.session_state.id_session, resource_name=resource)
    
    dynmodel.load_schema()

    dynmodel.gen_datamodel()

    datamodel = getattr(import_module(f"model.{st.session_state.id_session}_{resource}"), resource.upper())
    
    # Expander Block
    with st.expander(label=f"{cloud.upper()} {resource.upper()}"):
            
        data_form = sp.pydantic_input(key=f"data_{resource}",model=datamodel)

        # submit_button = st.form_submit_button(label="Submit")                

        if data_form:
            
            #st.json(data_form)

            os.remove(f"./webapp/model/{st.session_state.id_session}_{resource}.py")

            return {resource : data_form}
