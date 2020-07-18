import json
import plotly.graph_objects as go
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#define functions
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
    """Converts raw weather data into structured dictionary.
    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A dictionary containing the processed and formatted weather data.
    """
    #get filename str
    strfile = str(forecast_file.split("_")[1])
    strfile = strfile.split(".")[0]

    #declare variables
    output = {}
    temp = {}
    wt = []
    dates = []
    overallTs = []
    overallRFTs = []
    temps = []
    minOfmin = 100
    maxOfmax = 0
    minLs = []
    maxLs = []
    sumRain24 = 0
    daytimeCount = 0
    maxOfuv = 0

    #extract data
    with open(forecast_file, "r", encoding='utf8') as read_file:
        data = json.load(read_file) #load file
        for obj in data:
            date = convert_date(obj["LocalObservationDateTime"])

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
                    if mn < minOfmin:
                        minOfmin = mn
                        groupMin = key
                    minLs.append(mn)

                    mx = value["Maximum"]["Metric"]["Value"]
                    if mx > maxOfmax:
                        maxOfmax = mx
                        groupMax = key
                    maxLs.append(mx)
                    
                    for i,j in v.items():
                        tmp = v["Metric"]["Value"]
                        temps.append(tmp)
        for p in data:
            precip = p["PrecipitationSummary"]
            for key,value in precip.items():
                rain24 = precip["Past24Hours"]["Metric"]["Value"]
                sumRain24 = sumRain24 + rain24

        for d in data:
            daytime = d["IsDayTime"]
            if(daytime == True):
                daytimeCount = daytimeCount + 1
        
        for u in data:
            uv = u["UVIndex"]
            if uv > maxOfuv:
                maxOfuv = uv

        output = {
            "File": strfile,
            "Date": date,
            "DaylightHour": daytimeCount,
            "MaxUV": maxOfuv,
            "MinsGroup": [groupMin, minOfmin],
            "MaxGroup": [groupMax, maxOfmax],
            "Rain24mm": sumRain24,
            "overallTs": overallTs,
            "overallRFTs": overallRFTs,
            "Mins": minLs,
            "Maxs": maxLs,
            "WeatherText": ['Light rain','Sunny'],
            "WeatherFreq": [lr,s]
        }
    return output

def summarise_weather(process_dict):
    """Summarise the dictionary of data into meaningful text.
    Args:
        process_dict: A dictionary of data extracted and formatted with process_weather function.
    Returns:
        A meaningful summary on the data dictionary.
    """
    #declare
    summary = ""

    mingroup = process_dict['MinsGroup'][0]
    maxgroup = process_dict['MaxGroup'][0]

    #summarise
    summary += (f"----------------------------- {process_dict['Date']} -----------------------------\n")
    summary += (f"------------------- Summary for the past {process_dict['File']} ------------------- \n")
    summary += (f"Minimum temperature of {process_dict['MinsGroup'][1]}{DEGREE_SYBMOL} occurred in the {process_dict['MinsGroup'][0]}. \n")
    summary += (f"Maximum temperature of {process_dict['MaxGroup'][1]}{DEGREE_SYBMOL} occurred in the {process_dict['MaxGroup'][0]}. \n")
    summary += (f"The amount of precipitation that fell in the past {process_dict['File']} is {process_dict['Rain24mm']} mm. \n")
    summary += (f"The number of daylight hours in the past {process_dict['File']} is {process_dict['DaylightHour']} hours. \n")
    summary += (f"The maximum UV index for the past {process_dict['File']} is {process_dict['MaxUV']}. \n")
    summary += ("\n")
    summary += (f"------------------------------- (>^.^)>^ -------------------------------\n")

    return summary


# if __name__ == "__main__":
#     print(process_weather("data/historical_24hours_a.json"))

def plot_weather(process_dict):
    #plotting
    #boxplot
    fig1a = go.Figure()
    fig1a.add_trace(go.Box(y=process_dict['overallTs'], name = "Temperature"))
    fig1a.add_trace(go.Box(y=process_dict['overallRFTs'], name = "Real Feel Temperature"))
    fig1a.update_layout(title=f"Boxplot comparison of Temperature and Real Feel Temperature on {process_dict['Date']} for the past {process_dict['File']}",
                   xaxis_title='Variable',
                   yaxis_title='Temperature (°C)')        
    fig1a.show()

    #bar graph
    fig1b = go.Figure()
    fig1b.add_trace(go.Bar(x = process_dict['WeatherText'], y=process_dict['WeatherFreq'], name = "Weather"))
    fig1b.update_layout(title=f"Frequency comparison of WeatherText on {process_dict['Date']} for the past {process_dict['File']}",
                   xaxis_title='WeatherText Category',
                   yaxis_title='Count')        
    fig1b.show()


with open("historical_6hours_summary.txt", "w", encoding='utf8') as write_file:
    write_file.write(summarise_weather(process_weather("data/historical_6hours.json")))
plot_weather(process_weather("data/historical_6hours.json"))

with open("historical_24hours_a_summary.txt", "w", encoding='utf8') as write_file:
    write_file.write(summarise_weather(process_weather("data/historical_24hours_a.json")))
plot_weather(process_weather("data/historical_24hours_a.json"))

with open("historical_24hours_b_summary.txt", "w", encoding='utf8') as write_file:
    write_file.write(summarise_weather(process_weather("data/historical_24hours_b.json")))
plot_weather(process_weather("data/historical_24hours_b.json"))
