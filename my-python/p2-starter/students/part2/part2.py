import json
#import plotly.express as px
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
    output = {}
    minLs = []
    maxLs = []
    datels = []
    rlminLs = []
    rlmaxLs = []
    rlminLssh = []
    rlmaxLssh = []

    with open(forecast_file, "r", encoding='utf8') as read_file:
        data = json.load(read_file) #load file

        for t in data['DailyForecasts']:
            dates = convert_date(t['Date'])
            datels.append(dates)
        
            mn = convert_f_to_c(t['Temperature']['Minimum']['Value'])
            minLs.append(mn)
        
            mx = convert_f_to_c(t['Temperature']['Maximum']['Value'])
            maxLs.append(mx)

            mnrl = convert_f_to_c(t['RealFeelTemperature']['Minimum']['Value'])
            rlminLs.append(mnrl)
        
            mxrl = convert_f_to_c(t['RealFeelTemperature']['Maximum']['Value'])
            rlmaxLs.append(mxrl)

            mnrlsh = convert_f_to_c(t['RealFeelTemperatureShade']['Minimum']['Value'])
            rlminLssh.append(mnrlsh)
        
            mxrlsh = convert_f_to_c(t['RealFeelTemperatureShade']['Maximum']['Value'])
            rlmaxLssh.append(mxrlsh)
        
        output = {
            "Dates": datels,
            "Mins": minLs,
            "Max": maxLs,
            "RealFeelTemperatureMins": rlminLs,
            "RealFeelTemperatureMax": rlmaxLs,
            "RealFeelTemperatureShadeMins": rlminLssh,
            "RealFeelTemperatureShadeMax": rlmaxLssh
        }
        #print(type(output))

    return output

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_10days.json"))


#plotting
df1 = process_weather("data/forecast_5days_a.json")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df1['Dates'], y=df1['Mins'], name='Daily Minimums',
                         line=dict(color='royalblue', width=4)))
fig1.add_trace(go.Scatter(x=df1['Dates'], y=df1['Max'], name = 'Daily Maximums',
                         line=dict(color='firebrick', width=4)))
fig1.add_trace(go.Scatter(x=df1['Dates'], y=df1['RealFeelTemperatureMins'], name = 'Real Feel Minimums',
                         line=dict(color='royalblue', width=4, dash = 'dash')))
fig1.add_trace(go.Scatter(x=df1['Dates'], y=df1['RealFeelTemperatureMax'], name = 'Real Feel Maximums',
                         line=dict(color='firebrick', width=4, dash = 'dash')))
fig1.add_trace(go.Scatter(x=df1['Dates'], y=df1['RealFeelTemperatureShadeMins'], name = 'Real Feel Shade Minimums',
                         line=dict(color='royalblue', width=4, dash = 'dot')))
fig1.add_trace(go.Scatter(x=df1['Dates'], y=df1['RealFeelTemperatureShadeMax'], name = 'Real Feel Shade Maximums',
                         line=dict(color='firebrick', width=4, dash = 'dot')))
fig1.update_layout(title='Daily Minimum and Maximum Temperature',
                   xaxis_title='Date',
                   yaxis_title='Temperature (°C)')                         
fig1.show()

df2 = process_weather("data/forecast_5days_b.json")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df2['Dates'], y=df2['Mins'], name='Daily Minimums',
                         line=dict(color='royalblue', width=4)))
fig2.add_trace(go.Scatter(x=df2['Dates'], y=df2['Max'], name = 'Daily Maximums',
                         line=dict(color='firebrick', width=4)))
fig2.add_trace(go.Scatter(x=df2['Dates'], y=df2['RealFeelTemperatureMins'], name = 'Real Feel Minimums',
                         line=dict(color='royalblue', width=4, dash = 'dash')))
fig2.add_trace(go.Scatter(x=df2['Dates'], y=df2['RealFeelTemperatureMax'], name = 'Real Feel Maximums',
                         line=dict(color='firebrick', width=4, dash = 'dash')))
fig2.add_trace(go.Scatter(x=df2['Dates'], y=df2['RealFeelTemperatureShadeMins'], name = 'Real Feel Shade Minimums',
                         line=dict(color='royalblue', width=4, dash = 'dot')))
fig2.add_trace(go.Scatter(x=df2['Dates'], y=df2['RealFeelTemperatureShadeMax'], name = 'Real Feel Shade Maximums',
                         line=dict(color='firebrick', width=4, dash = 'dot')))
fig2.update_layout(title='Daily Minimum and Maximum Temperature',
                   xaxis_title='Date',
                   yaxis_title='Temperature (°C)')                         
fig2.show()

df3 = process_weather("data/forecast_10days.json")
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=df3['Dates'], y=df3['Mins'], name='Daily Minimums',
                         line=dict(color='royalblue', width=4)))
fig3.add_trace(go.Scatter(x=df3['Dates'], y=df3['Max'], name = 'Daily Maximums',
                         line=dict(color='firebrick', width=4)))
fig3.add_trace(go.Scatter(x=df3['Dates'], y=df3['RealFeelTemperatureMins'], name = 'Real Feel Minimums',
                         line=dict(color='royalblue', width=4, dash = 'dash')))
fig3.add_trace(go.Scatter(x=df3['Dates'], y=df3['RealFeelTemperatureMax'], name = 'Real Feel Maximums',
                         line=dict(color='firebrick', width=4, dash = 'dash')))
fig3.add_trace(go.Scatter(x=df3['Dates'], y=df3['RealFeelTemperatureShadeMins'], name = 'Real Feel Shade Minimums',
                         line=dict(color='royalblue', width=4, dash = 'dot')))
fig3.add_trace(go.Scatter(x=df3['Dates'], y=df3['RealFeelTemperatureShadeMax'], name = 'Real Feel Shade Maximums',
                         line=dict(color='firebrick', width=4, dash = 'dot')))
fig3.update_layout(title='Daily Minimum and Maximum Temperature',
                   xaxis_title='Date',
                   yaxis_title='Temperature (°C)')                         
fig3.show()
