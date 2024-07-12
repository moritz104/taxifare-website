import streamlit as st
import datetime
import requests

'''
# TaxiFareModel Frontend
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

st.markdown("""

    ### Please enter the following information:
""")

pickup_lon = st.text_input(label="pickup longitude")
pickup_lat = st.text_input(label="pickup latitude")
dropoff_lon = st.text_input(label="dropoff longitude")
dropoff_lat = st.text_input(label="dropoff latitude")
passenger_count = st.number_input(label="Passenger count", min_value=1, max_value=10)
date = st.date_input("What day do you need a ride?", datetime.date(2019, 7, 6), format="YYYY-MM-DD" )
time = st.time_input("What time?", datetime.time(8, 45))
button = st.button("Get fare", type="primary")

para_dict = {"pickup_datetime": f'{date} {time}',
             "pickup_longitude": pickup_lon,
             "pickup_latitude": pickup_lat,
             "dropoff_longitude": dropoff_lon,
             "dropoff_latitude": dropoff_lat,
             "passenger_count": passenger_count
            }

url = "https://taxifare.lewagon.ai/predict"

if button:
    call_result = requests.get(url, params=para_dict).json()
    call_result['fare']

#params = f"??pickup_datetime={date}%2019:18:00&pickup_longitude={pickup_lon}&pickup_latitude={pickup_lat}&dropoff_longitude={dropoff_lon}&dropoff_latitude={dropoff_lon}&passenger_count={passenger_count}"

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
