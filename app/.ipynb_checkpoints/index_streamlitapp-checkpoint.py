import streamlit as st
import subprocess

# Set page config and load CSS
st.set_page_config(
    page_title="Project Description",
    page_icon=":rocket:",
    layout="wide"
)
st.markdown('<link rel="stylesheet" href="https://bootswatch.com/4/flatly/bootstrap.css">', unsafe_allow_html=True)

# Logo section
st.markdown('<div class="container-fluid text-center"><img class="mt-3" src="https://insat.rnu.tn/assets/images/logo_c.png" alt="INSAT Logo" style="width: 100px;"></div>', unsafe_allow_html=True)
st.markdown("---")

# Page content
st.title("Project Description")

# Description section
st.markdown("The objective of this project is to create a website that can predict text from speech extracted from a video. The project aims to automate the process of predicting and extracting text by analyzing lip movements in the provided video.")

# Card section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card"><div class="card-body"><h5 class="card-title">BENZAIED Saifeddine</h5><p class="card-text">Email: saifeddine.benzaied@insat.ucar.tn</p></div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><div class="card-body"><h5 class="card-title">GAIED Sadok</h5><p class="card-text">Email: sadok.gaied@insat.ucar.tn</p></div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><div class="card-body"><h5 class="card-title">FENNANI Jihen</h5><p class="card-text">Email: jihen.fennani@insat.ucar.tn</p></div></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card"><div class="card-body"><h5 class="card-title">ZNAIDI Chaima</h5><p class="card-text">Email: chaima.znaidi@insat.ucar.tn</p></div></div>', unsafe_allow_html=True)
 

# Button to run Streamlit app
st.markdown('<div class="container-fluid text-center">', unsafe_allow_html=True)
if st.button("Run Streamlit App"):
    # Execute the command in the terminal
    subprocess.Popen("streamlit run --server.port 8502 streamlitapp.py", shell=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer section
st.markdown("---")
st.markdown("For more information or to access the full content, please visit the Streamlit app.")
