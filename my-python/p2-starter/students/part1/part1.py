import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    tempC = round(((temp_in_farenheit-32)/1.8 ),1)
    return tempC


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = round(total/num_items,1)
    return mean

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    output = ""
    minOfmin = 100
    maxOfmax = 0
    sumMin = 0
    sumMax = 0
    minLs = []
    maxLs = []
    datels = []

    with open(forecast_file, "r", encoding='utf8') as read_file:
        data = json.load(read_file) #load file

        for t in data['DailyForecasts']:
            dates = t['Date']
            datels.append(dates)
        
            mn = convert_f_to_c(t['Temperature']['Minimum']['Value'])
            minLs.append(mn)

            if mn < minOfmin:
                minOfmin = mn
                dateMin = convert_date(t['Date'])
            sumMin = sumMin + mn
        
            mx = convert_f_to_c(t['Temperature']['Maximum']['Value'])
            maxLs.append(mx)

            if mx > maxOfmax:
                maxOfmax = mx
                dateMax = convert_date(t['Date'])
            sumMax = sumMax + mx

        meanLows = calculate_mean(sumMin,len(minLs))
        meanHighs = calculate_mean(sumMax,len(maxLs))

        output+= (f"{len(datels)} Day Overview\n")
        output+= (f"    The lowest temperature will be {format_temperature(minOfmin)}, and will occur on {dateMin}.\n")
        output+= (f"    The highest temperature will be {format_temperature(maxOfmax)}, and will occur on {dateMax}.\n")
        output+= (f"    The average low this week is {format_temperature(meanLows)}.\n")
        output+= (f"    The average high this week is {format_temperature(meanHighs)}.\n\n")


        for t in data['DailyForecasts']:
            date = convert_date(t['Date'])
            minT = convert_f_to_c(t['Temperature']['Minimum']['Value'])
            maxT = convert_f_to_c(t['Temperature']['Maximum']['Value'])

            output+= (f"-------- {date} --------\n")
            output+= (f"Minimum Temperature: {format_temperature(minT)}\n")
            output+= (f"Maximum Temperature: {format_temperature(maxT)}\n")
            output+= (f"Daytime: {t['Day']['LongPhrase']}\n")
            output+= (f"    Chance of rain:  {t['Day']['RainProbability']}%\n")
            output+= (f"Nighttime: {t['Night']['LongPhrase']}\n")
            output+= (f"    Chance of rain:  {t['Night']['RainProbability']}%\n\n")
    return output

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_10days.json"))

with open("forecast_5days_a_output.txt", "w", encoding='utf8') as write_file:
    write_file.write(process_weather("data/forecast_5days_a.json"))

with open("forecast_5days_b_output.txt", "w", encoding='utf8') as write_file:
    write_file.write(process_weather("data/forecast_5days_b.json"))

with open("forecast_5days_10days_output.txt", "w", encoding='utf8') as write_file:
    write_file.write(process_weather("data/forecast_10days.json"))


