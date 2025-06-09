import httpx
import toml

class WeatherClient:
    def __init__(self, config_path="config.toml"):
        config = toml.load(config_path)
        self.cities = config["weather"]["cities"]

    async def fetch_weather(self, city: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://nejakeapi.pocasi/{city}")
            return response.json()

    async def fetch_all(self) -> dict:
        results = {}
        for city in self.cities:
            results[city] = await self.fetch_weather(city)
        return results
