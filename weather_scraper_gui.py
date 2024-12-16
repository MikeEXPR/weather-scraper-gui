import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    api_key = "YOUR_API"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found. Please try again.")
            return

        # Extract data
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()

        # Update the labels
        weather_result.config(
            text=f"Weather in {city}:\nTemperature: {temperature}°F\nHumidity: {humidity}%\nDescription: {description}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Weather Scraper")
root.geometry("400x300")
root.resizable(False, False)

# Title
tk.Label(root, text="Weather Scraper", font=("Helvetica", 16, "bold")).pack(pady=10)

# Input Field
tk.Label(root, text="Enter City Name:").pack()
city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

# Fetch Button
tk.Button(root, text="Fetch Weather", command=get_weather).pack(pady=10)

# Result Display
weather_result = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
weather_result.pack(pady=10)

# Run the App
root.mainloop()