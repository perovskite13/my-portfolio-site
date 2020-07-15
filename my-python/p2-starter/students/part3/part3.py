import json
import plotly.graph_objects as go
from datetime import datetime

#data extract
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    tempC = round(((temp_in_farenheit-32)/1.8 ),1)
    return tempC

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%d %B %Y')

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    temp = {}
    wt = []
    overallTs = []
    overallRFTs = []
    temps = []
    minLs = []
    maxLs = []

    with open(forecast_file, "r", encoding='utf8') as read_file:
        data = json.load(read_file) #load file
        for obj in data:
            overallT = obj["Temperature"]
            for key,value in overallT.items():
                overallTs.append(overallT["Metric"]["Value"])
            
            overallRFT = obj["RealFeelTemperature"]
            for key,value in overallRFT.items():
                overallRFTs.append(overallRFT["Metric"]["Value"])
            wt.append(obj["WeatherText"])
        
        lr = wt.count('Light rain')
        s = wt.count('Sunny')

        for t in data:
            temp = t["TemperatureSummary"]
            for key,value in temp.items():
                for k,v in value.items():
                    mn = value["Minimum"]["Metric"]["Value"]
                    minLs.append(mn)
                    mx = value["Maximum"]["Metric"]["Value"]
                    maxLs.append(mx)
                    for i,j in v.items():
                        tmp = v["Metric"]["Value"]
                        temps.append(tmp)
            
        #print(overallTs)
        #print(overallRFTs)
        #print(minLs)
        #print(maxLs)
        #print(wt)
        
        output = {
            "overallTs": overallTs,
            "overallRFTs": overallRFTs,
            "Mins": minLs,
            "Maxs": maxLs,
            "WeatherText": ['Light rain','Sunny'],
            "WeatherFreq": [lr,s]
        }

    return output

if __name__ == "__main__":
    print(process_weather("data/historical_6hours.json"))

#plotting
#boxplot
df1 = process_weather("data/historical_6hours.json")
fig1a = go.Figure()
fig1a.add_trace(go.Box(y=df1['overallTs'], name = "Temperature"))
fig1a.add_trace(go.Box(y=df1['overallRFTs'], name = "Real Feel Temperature"))
fig1a.update_layout(title='Boxplot comparison of Temperature and Real Feel Temperature',
                   xaxis_title='Variable',
                   yaxis_title='Temperature (°C)')        
fig1a.show()

#bar graph
fig1b = go.Figure()
fig1b.add_trace(go.Bar(x = df1['WeatherText'], y=df1['WeatherFreq'], name = "Weather"))
fig1b.update_layout(title='Frequency comparison of WeatherText',
                   xaxis_title='WeatherText Category',
                   yaxis_title='Count')        
fig1b.show()