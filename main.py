import streamlit as st
from annotated_text import annotated_text

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>SKEJ Advertising</h1>",
            unsafe_allow_html=True)
st.markdown("---")

# --- Zone --- #
st.markdown("<h3 style='text-align: center;'>Zone</h3>",
            unsafe_allow_html=True)
zones = ["Zone 1", "Zone 2", "Zone 3", "Zone 4"]
zones_amount = {"Zone 1": 75, "Zone 2": 75, "Zone 3": 75, "Zone 4": 75}

zone_selected = st.selectbox("Select Zone", zones)
st.markdown("---")

# --- Months --- #
st.markdown("<h3 style='text-align: center;'>Months</h3>",
            unsafe_allow_html=True)
month_col, month_discount_section = st.columns([2.5, 1])
with month_col:
    months_selected = st.selectbox("Number of Months", range(1, 7))
with month_discount_section:
    st.table({"Months": ["4-5 Months", "6 Months"],
             "Discount": ["20%", "30%"]})

if months_selected < 4:
    months_discount = 0

elif months_selected < 6:
    months_discount = 20
    month_color = "#afa"
else:
    months_discount = 30
    month_color = "#afa"
st.markdown("---")

# --- Displays --- #
st.markdown("<h3 style='text-align: center;'>Displays</h3>",
            unsafe_allow_html=True)
screen_col, screen_discount_section = st.columns([2.5, 1])
with screen_col:
    screens_selected = int(st.number_input(
        "Number of Displays", min_value=1, max_value=25))
with screen_discount_section:
    st.table({"Displays": ["5-9", "10-15", "16-25"],
             "Discount": ["10%", "15%", "25%"]})

if screens_selected < 5:
    screen_discount = 0
    screen_color = "#faa"
elif screens_selected <= 9:
    screen_discount = 10
    screen_color = "#faa"
elif screens_selected <= 15:
    screen_discount = 15
else:
    screen_discount = 25
st.markdown("---")

# --- Final Price --- #
st.markdown("<h3 style='text-align: center;'>Final Price</h3>",
            unsafe_allow_html=True)
final_price = zones_amount[zone_selected] \
    * (months_selected * (100 - months_discount)/100) \
    * (screens_selected * (100 - screen_discount)/100)

# Color
month_color = "#afa"
final_price_color = "#afa"
screen_color = "#afa"
if months_selected < 4:
    month_color = "#faa"
if screens_selected < 5:
    screen_color = "#faa"

annotated_text(
    (f"{zones_amount[zone_selected]} CAD", "Zone Amount", "#afa"),
)
annotated_text(
    " x ",
    (f"{months_selected} x  {100-months_discount}% ", "month rate", month_color),
)
annotated_text(
    " x ",
    (f"{screens_selected} x  {100-screen_discount}% ", "display rate", screen_color),
)
annotated_text(
    " = ",
    (f"{round(final_price, 2)} CAD", "", final_price_color)
)