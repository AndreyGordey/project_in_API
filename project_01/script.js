
import fetch from 'node-fetch'; // Убедитесь, что вы установили node-fetch

async function getWeather(city, apiKey) {
    const url = "http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric;"

    try {
        const response = await fetch(url);
        
        if (response.ok) {
            const data = await response.json();
            const cityName = data.name;
            const temperature = data.main.temp;
            const weatherDescription = data.weather[0].description;
            
            console.log(`Погода в городе ${cityName}:`);
            console.log(`Температура: ${temperature}°C`);
            console.log(`Описание: ${weatherDescription}`);
        } else {
            console.log("Ошибка при получении данных о погоде:", response.status);
        }
    } catch (error) {
        console.error("Произошла ошибка:", error);
    }
}

(async () => {
    const apiKey = "fa46cb5a3781329ffe73701682ff8fbd"; // Введите свой API-ключ здесь
    const city = prompt("Введите название города: "); // Замените на подходящий способ ввода
    await getWeather(city, apiKey);
})();
