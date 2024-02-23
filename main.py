"""
A demo webapp to showecase steinway assembly overview.

Has two views, one for the floor overview and one for the piano production stage overview.

"""

import streamlit as st
from streamlit_option_menu import option_menu


DEMO_FLOORS = ["Floor 1", "Floor 2", "Floor 3", "Floor 4", "Floor 5"]
DEMO_SERIAL_NO = [
    "St-M-135",
    "St-D-235",
    "St-M-203",
    "St-D-456",
    "St-M-789",
    "St-D-987",
    "St-M-246",
    "St-D-789",
    "St-M-357",
    "St-D-159",
]
DEMO_SERIAL_NO.sort()
# wide webapp with sidebar closed.P
st.set_page_config(
    page_title="Steinway Assembly Overview",
    page_icon="🎹",
    initial_sidebar_state="collapsed",
)

st.write("# Steinway Assembly Overview")
selected_view = option_menu(
    None,
    ["Floor view", "Piano view"],
    icons=["bulding", "database-fill"],
    orientation="horizontal",
)


if selected_view == "Floor view":
    st.write("## Floor view")
    # add a dropdown to select the floor
    selected_floor = st.selectbox("Select floor", DEMO_FLOORS)
    st.write(f"Showing production for {selected_floor}")

else:
    st.write("## Piano view")
    # add a searchable dropdown to select the piano serial number
    seleted_piano = st.selectbox("Select piano serial number", DEMO_SERIAL_NO)
