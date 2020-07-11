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
    string = json.dumps(forecast_file) #convert to string
    data = json.loads(string) #convert to dict
    return data

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_10days.json"))


##5 days a

minOfmin = 100
maxOfmax = 0
sumMin = 0
sumMax = 0
minLs = []
maxLs = []
datels = []

with open("data/forecast_5days_a.json", "r", encoding='utf8') as read_file:
    read = json.load(read_file) #load file
    data = process_weather(read)

with open("forecast_5days_a_output.txt", "w", encoding='utf8') as write_file:
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

    write_file.write(f"{len(datels)} Day Overview\n")
    write_file.write(f"    The lowest temperature will be {format_temperature(minOfmin)}, and will occur on {dateMin}.\n")
    write_file.write(f"    The highest temperature will be {format_temperature(maxOfmax)}, and will occur on {dateMax}.\n")
    write_file.write(f"    The average low this week is {format_temperature(meanLows)}.\n")
    write_file.write(f"    The average high this week is {format_temperature(meanHighs)}.\n \n")


    for t in data['DailyForecasts']:
        date = convert_date(t['Date'])
        minT = convert_f_to_c(t['Temperature']['Minimum']['Value'])
        maxT = convert_f_to_c(t['Temperature']['Maximum']['Value'])

        write_file.write(f"--------{date}--------\n")
        write_file.write(f"Minimum Temperature: {format_temperature(minT)} \n")
        write_file.write(f"Maximum Temperature: {format_temperature(maxT)} \n")
        write_file.write(f"Daytime: {t['Day']['LongPhrase']} \n")
        write_file.write(f"    Chance of rain: {t['Day']['RainProbability']}% \n")
        write_file.write(f"Nighttime: {t['Night']['LongPhrase']} \n")
        write_file.write(f"    Chance of rain: {t['Night']['RainProbability']}% \n \n")


##5 days b
minOfmin = 100
maxOfmax = 0
sumMin = 0
sumMax = 0
minLs = []
maxLs = []
datels = []

with open("data/forecast_5days_b.json", "r", encoding='utf8') as read_file:
    read = json.load(read_file) #load file
    data = process_weather(read)

with open("forecast_5days_b_output.txt", "w", encoding='utf8') as write_file:
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

    write_file.write(f"{len(datels)} Day Overview\n")
    write_file.write(f"    The lowest temperature will be {format_temperature(minOfmin)}, and will occur on {dateMin}.\n")
    write_file.write(f"    The highest temperature will be {format_temperature(maxOfmax)}, and will occur on {dateMax}.\n")
    write_file.write(f"    The average low this week is {format_temperature(meanLows)}.\n")
    write_file.write(f"    The average high this week is {format_temperature(meanHighs)}.\n \n")


    for t in data['DailyForecasts']:
        date = convert_date(t['Date'])
        minT = convert_f_to_c(t['Temperature']['Minimum']['Value'])
        maxT = convert_f_to_c(t['Temperature']['Maximum']['Value'])

        write_file.write(f"--------{date}--------\n")
        write_file.write(f"Minimum Temperature: {format_temperature(minT)} \n")
        write_file.write(f"Maximum Temperature: {format_temperature(maxT)} \n")
        write_file.write(f"Daytime: {t['Day']['LongPhrase']} \n")
        write_file.write(f"    Chance of rain: {t['Day']['RainProbability']}% \n")
        write_file.write(f"Nighttime: {t['Night']['LongPhrase']} \n")
        write_file.write(f"    Chance of rain: {t['Night']['RainProbability']}% \n \n")

##10 days
minOfmin = 100
maxOfmax = 0
sumMin = 0
sumMax = 0
minLs = []
maxLs = []
datels = []

with open("data/forecast_10days.json", "r", encoding='utf8') as read_file:
    read = json.load(read_file) #load file
    data = process_weather(read)

with open("forecast_10days_output.txt", "w", encoding='utf8') as write_file:
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

    write_file.write(f"{len(datels)} Day Overview\n")
    write_file.write(f"    The lowest temperature will be {format_temperature(minOfmin)}, and will occur on {dateMin}.\n")
    write_file.write(f"    The highest temperature will be {format_temperature(maxOfmax)}, and will occur on {dateMax}.\n")
    write_file.write(f"    The average low this week is {format_temperature(meanLows)}.\n")
    write_file.write(f"    The average high this week is {format_temperature(meanHighs)}.\n \n")


    for t in data['DailyForecasts']:
        date = convert_date(t['Date'])
        minT = convert_f_to_c(t['Temperature']['Minimum']['Value'])
        maxT = convert_f_to_c(t['Temperature']['Maximum']['Value'])

        write_file.write(f"--------{date}--------\n")
        write_file.write(f"Minimum Temperature: {format_temperature(minT)} \n")
        write_file.write(f"Maximum Temperature: {format_temperature(maxT)} \n")
        write_file.write(f"Daytime: {t['Day']['LongPhrase']} \n")
        write_file.write(f"    Chance of rain: {t['Day']['RainProbability']}% \n")
        write_file.write(f"Nighttime: {t['Night']['LongPhrase']} \n")
        write_file.write(f"    Chance of rain: {t['Night']['RainProbability']}% \n \n")
