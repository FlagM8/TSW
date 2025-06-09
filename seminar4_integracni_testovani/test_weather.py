import pytest
import asyncio
from weather import WeatherClient

@pytest.mark.asyncio
async def test_weather_logging_with_spy(mocker):
    logger = mocker.spy(__import__("builtins"), "print") 

    class MockWeatherClient(WeatherClient):
        async def fetch_weather(self, city):
            print(f"Fetching weather for {city}")
            return {"temp": 20}

    client = MockWeatherClient()
    await client.fetch_all()

    assert logger.call_count == len(client.cities)
