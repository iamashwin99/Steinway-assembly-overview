"""
A demo webapp to showecase steinway assembly overview.

Has two views, one for the floor overview and one for the piano production stage overview.

"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd



def get_sheet_df(sheet_name):
    """
    Get a df from a google sheet

    """
    sheet_id = "1ETxOtf51_kOt5qVp2d-5wP7ihQMNgNe-qydSm3aVLJA"
    # sheet_name = "HH-M-135"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    piano_df = pd.read_csv(url)
    return piano_df

DEMO_FLOORS = ["Floor1", "Floor2", "Floor3", "Floor4", "Floor5"]
DEMO_SERIAL_NO = [
    "HH-M-135",
    "NY-D-235",
    "HH-M-203",
    "NY-D-456",
    "HH-M-789",
    "NY-D-987",
    "HH-M-246",
    "NY-D-789",
    "HH-M-357",
    "NY-D-159",
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
    icons=["building", "database-fill"],
    orientation="horizontal",
)


if selected_view == "Floor view":
    st.write("## Floor view")
    # add a dropdown to select the floor
    selected_floor = st.selectbox("Select floor", DEMO_FLOORS)
    st.write(f"Showing production for {selected_floor}")
    floor_df = get_sheet_df(selected_floor)
    st.write(floor_df.head())

else:
    st.write("## Piano view")
    # add a searchable dropdown to select the piano serial number
    seleted_piano = st.selectbox("Select piano serial number", DEMO_SERIAL_NO)
    st.write(f"Showing production for {seleted_piano}")
    floor_df = get_sheet_df(seleted_piano)
    st.write(floor_df.head())
