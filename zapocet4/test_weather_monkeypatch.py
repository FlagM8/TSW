import pytest
import asyncio
from weather import WeatherClient

@pytest.mark.asyncio
async def test_fetch_weather_monkeypatch(monkeypatch):
    async def mock_fetch_weather(self, city):
        return {"temp": 42, "city": city}

    monkeypatch.setattr(WeatherClient, "fetch_weather", mock_fetch_weather)

    client = WeatherClient()
    data = await client.fetch_all()

    for city in client.cities:
        assert data[city]["temp"] == 42
