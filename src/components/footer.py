import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/MxYqC09j/Qazim-Signature-Logo.png"
    
    st.markdown(f""" 
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content: center; align-items: center;">
        <span style="font-size: 18px; font-weight: bold; line-height: 27px; margin: 0; color: white">
                Created with ❤️ by
            </span>
        <img src='{logo_url}' style='height: 27px; width: auto; object-fit: contain; display: block;' />
        </div>
        
                """, unsafe_allow_html=True)