"""
A demo webapp to showecase steinway assembly overview.

Has two views, one for the floor overview and one for the piano production stage overview.

"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
# from streamlit_agraph.config import Config, ConfigBuilder
import nivo_chart as nc
# from graph import *
from heatmap import calendar_chart
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image;
img = Image.open('drawing.png')

def get_sheet_df(sheet_name):
    """
    Get a df from a google sheet

    """
    sheet_id = "1ETxOtf51_kOt5qVp2d-5wP7ihQMNgNe-qydSm3aVLJA"
    # sheet_name = "HH-M-135"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    piano_df = pd.read_csv(url)
    return piano_df


DEMO_DEPARTMENTS = ["Department1", "Department2", "Department3", "Department4", "Department5", "Department6"]
DEMO_FLOOR_NO_PIANOS = [10,4,13,21,2,3]
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

if 'overview' not in st.session_state:
    st.session_state['overview'] = 'building_view'

def disable_floor_view():
    """
    Disable the floor view and enable the piano view

    """
    st.session_state.overview = "floor_view"

# wide webapp with sidebar closed.P
st.set_page_config(
    page_title="Steinway Assembly Overview",
    page_icon="🎹",
    initial_sidebar_state="collapsed",
)

st.write("# Steinway Assembly Overview")
selected_view = option_menu(
    None,
    ["Overview","Department view", "Piano view"],
    icons=["pie-chart-fill","building", "database-fill"],
    orientation="horizontal",
)

if selected_view == "Overview":
    st.write("## Analytics")
    if st.session_state.overview == "building_view":
        # make a cloumns of 3 columns each with 2 floors as buttons, which take the whole width and height of the page
        cols = st.columns(3)
        i=1
        for col in cols:
            with col:
                for _ in range(2):
                    st.button(f"Department {i} \n ({DEMO_FLOOR_NO_PIANOS[i-1]} Pianos)", key=f"floor{i}", help=f"View floor {1}", use_container_width=True, on_click=disable_floor_view)
                    i+=1
    if st.session_state.overview == "floor_view":
        st.write("## Department view")
        # add a plotly plot with drawing.svg in the background
        fig = go.Figure()
        fig.add_layout_image(
            dict(
                x=0,
                sizex=1,
                y=1,
                sizey=1,
                xref="paper",
                yref="paper",
                opacity=1,
                layer="below",
                source=img,
            )
        )
        fig.update_xaxes(showgrid=False, zeroline=False, showline=False, showticklabels=False, range=[0, 1])
        fig.update_yaxes(showgrid=False, zeroline=False, showline=False, showticklabels=False, range=[0, 1])
        # add a green dot in the top left corner
        fig.add_trace(go.Scatter(x=[0], y=[0], mode="markers", marker=dict(color="green", size=20)))
        st.plotly_chart(fig, use_container_width=True)







elif selected_view == "Department view":
    st.write("## Department view")
    # add a dropdown to select the floor
    selected_floor = st.selectbox("Select floor", DEMO_DEPARTMENTS)
    st.write(f"Showing production for {selected_floor}")
    floor_df = get_sheet_df(selected_floor)
    st.write(floor_df.head())

elif selected_view == "Piano view":
    st.write("## Piano view")
    # add a searchable dropdown to select the piano serial number
    seleted_piano = st.selectbox("Select piano serial number", DEMO_SERIAL_NO)
    st.write(f"Showing production for {seleted_piano}")
    st.info(f"""
### Piano info
- **Serial number**: {seleted_piano}
- **Model**: Model M
- **Finish**: Ebony
- **Colour**: Purple
            """)
    floor_df = get_sheet_df(seleted_piano)
    st.write(floor_df.head())
    st.write("## Heatmap")
    nc.nivo_chart(data=calendar_chart["data"], layout=calendar_chart["layout"], key="calendar_chart")
