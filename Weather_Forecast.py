#calling libraries
import tkinter as tk 
import requests 
import random


root = tk.Tk()
frame =tk.Frame(root)
frame.grid(row=0, column=5, rowspan=8, sticky="nsew")
frame.grid_rowconfigure(8, weight=1)
root.title("Weather Forecast")
root.geometry("800x470")

#function 
def func_button ():

    city = enter_location.get()
    key = 'a589a47f46d12b5779c999170965e20b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

    res = requests.get(url)
    data = res.json()
    
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    

    Location_label.config(text = "Location: ", font=("Arial", 15))
    Temp_label.config(text = f"Temperature: {temp}°C" , font=("Arial", 15) )
    Humidity_label.config(text = f"Humidity: {humidity}%" , font=("Arial", 15))
    WindSpeed_label.config(text = f"Wind Speed: {wind_speed}km/h" , font=("Arial", 15))
    Pressure_label.config(text = f"Pressure: {pressure}hPa" , font=("Arial", 15))
    
  
#variables
temp = 20
humidity = 10
wind_speed = 10
pressure = 29
precipitation = random.randint(0,100)

Location_label = tk.Label(frame, text = "Location: ", font=("Arial", 15))
Temp_label = tk.Label(frame, text = f"Temperature: {temp}°C" , font=("Arial", 15) )
Humidity_label = tk.Label(frame, text = f"Humidity: {humidity}%" , font=("Arial", 15))
WindSpeed_label = tk.Label(frame, text = f"Wind Speed: {wind_speed}km/h" , font=("Arial", 15))
Pressure_label = tk.Label(frame, text = f"Pressure: {pressure}hPa" , font=("Arial", 15))
Precipitation_label = tk.Label(frame, text = f"Precipitation: {precipitation}%" , font=("Arial", 15))
button_search = tk.Button(frame, text='search' , font=("Arial", 15) ) 
enter_location = tk.Entry(frame , font=("Arial", 15) ) 

# grid
Location_label.grid(row=1, column=2, padx=20, pady=10)
enter_location.grid(row=1, column=3, padx=20, pady=10)
button_search.grid(row=1, column=4, padx=20, pady=10)
Temp_label.grid(row=3, column=0, padx=20, pady=10)
Humidity_label.grid(row=4, column=0, padx=20, pady=10)
WindSpeed_label.grid(row=5, column=0, padx=20, pady=10)
Pressure_label.grid(row=6, column=0, padx=20, pady=10)
Precipitation_label.grid(row=7, column=0, padx=20, pady=10)


 


button_search.config(command=func_button )    


root.mainloop()