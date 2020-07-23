<template>
  <div>
    <section class="section">
      <div class="content">
        <h1>Weather App by Population</h1>
        <p>What is the weather at the moment for the top 200 most populous cities in the world?</p>
      </div>

      <b-field style="display: inline-block;">
        <b-select v-model="selected_index">
          <option
            disabled
            value="-1">
            == Please select a city ==
          </option>
          <option
              v-for="(c, index) in cityList"
              :value="index"
              :key="index">
              {{ c.city }}, {{ c.country }}
          </option>
        </b-select>
      </b-field>
      <div style="display: inline-block; padding-left: 10px;">
        <b-button
          type="is-primary"
          @click="getCityWeather"
          :disabled="selected_index=='-1'">
          Submit
        </b-button>
      </div>

    </section>

    <section class="section" v-if="data.city != ''">
        <div class="columns">
          <div class="column is-three-fifths">
            <div class="container content">
              <h4 style="display: inline-block;">In {{ data.city }}, it is {{ data.time }}</h4>
              <img v-if="!isDay" src="../assets/moon.svg" width="20" style="margin-left:10px;"><br/><br/>

              <img style="vertical-align:middle;" :src="data.icon">            
              <div style="display: inline-block;">
                <span class="is-size-2">{{ data.temp }}</span>
                <span class="is-size-3"><sup>&deg;C</sup></span>
                <span class="is-size-2"> / Feels like {{ data.feelsLike }}</span>
                <span class="is-size-3"><sup>&deg;C</sup></span>
                <span class="is-size-2"> / {{ data.description }}</span>
              </div>
              
              <p>This city has a population of {{ data.population }}, 
                and is ranked {{ data.rank }}, most populous city in the world.</p> 

              <p><img
                src="../assets/person.svg"
                width="26"
                v-for="p in populationPerMil"
                :key="p" /></p>
              <p>(each person represents 100,000 people)</p>

              <b-loading 
                :is-full-page="false"
                :active="isLoading">
              </b-loading>

            </div>
          </div>
          <div class="column">
            <img :src="googleMapURL">
          </div>
        </div>
    </section>
  </div>
</template>

<script>
import CityList from '@/data/CityList.js'
import WeatherService from '@/services/WeatherService.js'
import ErrorNotifyMixin from '@/mixins/ErrorNotifyMixin.js'

export default {
  mixins: [ErrorNotifyMixin],
  data() {
    return {
      cityList: CityList.list,
      selected_index: '-1',
      isLoading: false,
      data: {
        city: '',
        temp: '',
        feelsLike: '',
        rawTime: '',
        time: '',
        icon: '',
        description: '',
        population: '',
        rank: '',
        lat: '',
        lon: ''
      }
    }
  },
  methods: {
    formatDateTime(dt) {
      let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
      let hour = dt.getUTCHours()
      let a_p = ''
      if (hour < 12) {
        a_p = 'AM'
      } else {
        a_p = 'PM'
      }
      if (hour == 0) {
        hour = 12
      }
      if (hour > 12) {
        hour = hour - 12;
      }
      let minute = dt.getUTCMinutes()
      minute = (minute < 10 ? '0' : '') + minute
      return days[dt.getUTCDay()] + ', ' + hour + ':' + minute + ' ' + a_p
    },
    getCityWeather() {
      this.isLoading = true
      WeatherService.getWeather(this.cityList[this.selected_index].id)
      .then(response => {
        console.log(response.data);
        let d = response.data
        /*convert from kelvin to celsius and round to 2 decimal places*/
        this.data.temp = Math.round((d.main.temp - 273.15) * 100) / 100 
        this.data.feelsLike = Math.round((d.main.feels_like - 273.15) * 100) / 100 
        this.data.icon = 'http://openweathermap.org/img/wn/' + d.weather[0].icon + '@2x.png'
        this.data.description = d.weather[0].description.charAt(0).toUpperCase() 
          + d.weather[0].description.slice(1)
        this.data.population = this.cityList[this.selected_index].population
        this.data.rank = this.cityList[this.selected_index].rank
        this.data.rawTime = new Date(Date.now() + (d.timezone * 1000))
        this.data.time = this.formatDateTime(this.data.rawTime)
        this.data.city = d.name
        this.data.lat = d.coord.lat
        this.data.lon = d.coord.lon
        this.isLoading = false
      })
      .catch(err => {
        this.showError(err.name + ': ' + err.message)
        this.isLoading = false
      })
    }
  },
  computed: {
    populationPerMil: function() {
      let pop = this.data.population.replace(/,/g, '')
      if (pop == '') {
        return 0
      }
      return Math.round(parseInt(pop,10)/1000000) * 10
    },
    isDay: function() {
      if (this.data.rawTime == '')
        return true
      let hours = this.data.rawTime.getUTCHours()
      return hours > 6 && hours < 19
    },
    googleMapURL: function() {
      return 'https://maps.googleapis.com/maps/api/staticmap?center=' + 
        this.data.lat + 
        '%2c%20' + 
        this.data.lon +
        '&zoom=5&size=400x400&key=' + process.env.VUE_APP_GM_API_KEY
    }
  }
}
</script>

<style scoped>

</style>
