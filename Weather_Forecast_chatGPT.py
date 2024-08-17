import customtkinter as CTk 
import tkinter as tk



import requests 
import random

# Initialize the main application window
root = CTk.CTk()
frame = CTk.CTkFrame(root)
frame.grid(row=0, column=5, rowspan=8, sticky="nsew")
frame.grid_rowconfigure(8, weight=1)
root.title("Weather Forecast")


# Function to fetch and update weather data
def func_button():
    city = enter_location.get()
    key = 'a589a47f46d12b5779c999170965e20b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

    try:
        res = requests.get(url)
        data = res.json()
        
        # Extract weather data
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        precipitation = random.randint(0, 100)  # Using random value for demonstration
        
        # Update labels with fetched data
        Temp_label.configure(text=f"Temperature: {temp}°C")
        Humidity_label.configure(text=f"Humidity: {humidity}%")
        WindSpeed_label.configure(text=f"Wind Speed: {wind_speed} km/h")
        Pressure_label.configure(text=f"Pressure: {pressure} hPa")
        Precipitation_label.configure(text=f"Precipitation: {precipitation}%")
    
    except Exception as e:
        # Handle any errors (e.g., city not found, network issues)
        Temp_label.config(text="Temperature: N/A")
        Humidity_label.config(text="Humidity: N/A")
        WindSpeed_label.config(text="Wind Speed: N/A")
        Pressure_label.config(text="Pressure: N/A")
        Precipitation_label.config(text="Precipitation: N/A")

# Initial values for weather data
temp = 20
humidity = 10
wind_speed = 10
pressure = 29
precipitation = random.randint(0, 100)

# Create and place widgets using customtkinter
Location_label = CTk.CTkLabel(frame, text="Location:", font=("Arial", 15))
Temp_label = CTk.CTkLabel(frame, text=f"Temperature: {temp}°C", font=("Arial", 15))
Humidity_label = CTk.CTkLabel(frame, text=f"Humidity: {humidity}%", font=("Arial", 15))
WindSpeed_label = CTk.CTkLabel(frame, text=f"Wind Speed: {wind_speed} km/h", font=("Arial", 15))
Pressure_label = CTk.CTkLabel(frame, text=f"Pressure: {pressure} hPa", font=("Arial", 15))
Precipitation_label = CTk.CTkLabel(frame, text=f"Precipitation: {precipitation}%", font=("Arial", 15))
button_search = CTk.CTkButton(frame, text='Search', font=("Arial", 15), command=func_button)
enter_location = CTk.CTkEntry(frame, font=("Arial", 15))

# Arrange widgets using grid layout
Location_label.grid(row=1, column=2, padx=20, pady=10)
enter_location.grid(row=1, column=3, padx=20, pady=10)
button_search.grid(row=1, column=4, padx=20, pady=10)
Temp_label.grid(row=3, column=0, padx=20, pady=10)
Humidity_label.grid(row=4, column=0, padx=20, pady=10)
WindSpeed_label.grid(row=5, column=0, padx=20, pady=10)
Pressure_label.grid(row=6, column=0, padx=20, pady=10)
Precipitation_label.grid(row=7, column=0, padx=20, pady=10)

# Start the main event loop
root.mainloop()
