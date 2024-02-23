import pandas as pd

calendar_chart = {
    "data": [
        {"value": 236, "day": "2023-06-26"},
        {"value": 362, "day": "2017-05-02"},
        {"value": 220, "day": "2017-07-12"},
    ],
    "layout": {
        "title": "Calendar Heatmap",
        "type": "calendar",
        "height": 400,
        "width": 600,
        "from": "2023-06-26",
        "to": "2024-07-12",
        "emptyColor": "#eeeeee",
        "colors": ["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"],
        "margin": {"top": 40, "right": 40, "bottom": 40, "left": 40},
        "yearSpacing": 40,
        "monthBorderColor": "#ffffff",
        "dayBorderWidth": 2,
        "dayBorderColor": "#ffffff",
        "legends": [
            {
                "anchor": "bottom-right",
                "direction": "row",
                "translateY": 36,
                "itemCount": 4,
                "itemWidth": 42,
                "itemHeight": 36,
                "itemsSpacing": 14,
                "itemDirection": "right-to-left",
            }
        ],
    },
}


# list all dates from 2023-06-26 to 2024-07-12 in a list
dates = pd.date_range(start="2023-06-26", end="2024-07-12").tolist()
data_entry = [{"value": 236, "day": str(date)} for date in dates]
calendar_chart["data"] = data_entry