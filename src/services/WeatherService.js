import axios from 'axios'


const apiClient = axios.create({
  baseURL: 'http://api.openweathermap.org/data/2.5',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

/*api.openweathermap.org/data/2.5/weather?id={city id}&appid={your api key}*/
export default {
  getWeather(id) {
    return apiClient.get('/weather?id=' + id + '&appid=' + process.env.VUE_APP_OW_API_KEY)
  }
}