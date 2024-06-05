import requests
import os

# URLs of the datasets
urls = {
    "confirmed": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    "recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
}

# Directory to save the data
data_dir = "data/"

# Create data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Download and save the datasets
for key, url in urls.items():
    response = requests.get(url)
    with open(f"{data_dir}time_series_covid19_{key}_global.csv", "wb") as file:
        file.write(response.content)

print("Data files have been downloaded successfully.")
