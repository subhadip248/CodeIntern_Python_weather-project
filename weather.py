from rich import print
from rich.console import Console
from rich.table import Table
import requests

console = Console()

API_KEY = "7f0f9385007c3750fd260083a6d1b2b7"  # Paste your OpenWeather API Key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print(f"[bold red]❌ Invalid city name![/bold red]")
        return

    table = Table(title=f"🌤️ Weather Report — {city.title()}", title_style="bold cyan")
    table.add_column("Parameter", style="yellow")
    table.add_column("Value", style="green")

    table.add_row("Temperature (°C)", str(data["main"]["temp"]))
    table.add_row("Humidity (%)", str(data["main"]["humidity"]))
    table.add_row("Wind Speed (m/s)", str(data["wind"]["speed"]))
    table.add_row("Description", data["weather"][0]["description"].title())

    console.print(table)

def main():
    print("\n[bold blue]🌍 Real-Time Weather App[/bold blue]")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
