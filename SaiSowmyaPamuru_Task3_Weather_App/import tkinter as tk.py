import tkinter as tk
from tkinter import messagebox
import requests


API_KEY = "a2e009af39e896fe8e93a83d3194529b"


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror(
            "Error",
            "Please enter a city name."
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror(
                "Error",
                "City not found."
            )
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=
            f"Temperature: {temperature}°C\n\n"
            f"Humidity: {humidity}%\n\n"
            f"Weather: {weather.title()}\n\n"
            f"Wind Speed: {wind_speed} m/s"
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Unable to fetch weather data."
        )


root = tk.Tk()
root.title("Weather App")
root.geometry("550x500")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 22, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
)
title_label.pack(pady=20)

city_label = tk.Label(
    root,
    text="Enter City Name",
    font=("Arial", 12),
    bg="#f4f6f8"
)
city_label.pack()

city_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)
city_entry.pack(pady=10)

search_button = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    bg="#3498db",
    fg="white",
    font=("Arial", 12, "bold")
)
search_button.pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#f4f6f8",
    justify="center"
)
result_label.pack(pady=30)

footer_label = tk.Label(
    root,
    text="Developed by Sai Sowmya Pamuru",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="gray"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()