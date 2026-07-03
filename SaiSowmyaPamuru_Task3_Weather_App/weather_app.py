import tkinter as tk
from tkinter import messagebox
import requests


API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"


def get_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror(
            "Input Error",
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

        if str(data.get("cod")) != "200":

            messagebox.showerror(
                "Error",
                "City not found or API issue."
            )
            return

        city_name = data["name"]
        country = data["sys"]["country"]

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        # Weather Icons

        if weather.lower() == "clear":
            icon = "☀️"

        elif weather.lower() == "clouds":
            icon = "☁️"

        elif weather.lower() in ["rain", "drizzle"]:
            icon = "🌧️"

        elif weather.lower() == "thunderstorm":
            icon = "⛈️"

        else:
            icon = "🌍"

        result = (
            f"{icon} {city_name}, {country}\n\n"
            f"Temperature : {temp} °C\n"
            f"Feels Like  : {feels_like} °C\n"
            f"Humidity    : {humidity}%\n"
            f"Pressure    : {pressure} hPa\n"
            f"Wind Speed  : {wind_speed} m/s\n"
            f"Condition   : {description.title()}"
        )

        result_label.config(text=result)

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Unable to fetch weather data.\n{e}"
        )


def clear_data():

    city_entry.delete(0, tk.END)

    result_label.config(text="")


# Main Window

root = tk.Tk()

root.title("Weather App")

root.geometry("600x550")

root.configure(bg="#eef5ff")

root.resizable(False, False)


# Title

title_label = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Arial", 24, "bold"),
    bg="#eef5ff",
    fg="#2c3e50"
)

title_label.pack(pady=20)


# City Input

city_label = tk.Label(
    root,
    text="Enter City Name",
    font=("Arial", 12),
    bg="#eef5ff"
)

city_label.pack()

city_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)

city_entry.pack(pady=10)


# Buttons Frame

button_frame = tk.Frame(
    root,
    bg="#eef5ff"
)

button_frame.pack(pady=10)


search_button = tk.Button(
    button_frame,
    text="Get Weather",
    command=get_weather,
    bg="#3498db",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)

search_button.grid(row=0, column=0, padx=10)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_data,
    bg="#7f8c8d",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)

clear_button.grid(row=0, column=1)


# Result

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#eef5ff",
    justify="left"
)

result_label.pack(pady=30)


# Footer

footer_label = tk.Label(
    root,
    text="Developed by Sai Sowmya Pamuru",
    font=("Arial", 9),
    bg="#eef5ff",
    fg="gray"
)

footer_label.pack(side="bottom", pady=10)

root.mainloop()
