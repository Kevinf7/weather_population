<template>
  <div class="site">
    <div class="site-main">
      <Weather/>
    </div>
    <footer class="footer">
      <div class="content has-text-centered">
        <img src="./assets/open_weather_logo.png" style="height:40px;"><br/>
        Weather data powered by OpenWeather<br/>
        Population data from <a href="https://worldpopulationreview.com/world-cities/">https://worldpopulationreview.com/world-cities/</a><br/>
        Website design by <a href="https://www.kevin7.net">kevin7.net</a>
      </div>
    </footer>
  </div>
</template>

<script>
import Weather from './components/Weather.vue'

export default {
  name: 'App',
  components: {
    Weather
  }
}
</script>

<style scoped>
  .site {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
  }
  .site-main {
    flex: 1 0 auto;
  }
</style>

<style lang="scss">
  @charset "utf-8";

  $primary: #84a9ac;
  $footer-background-color: #84a9ac;
  $section-padding: 2.5rem 1.5rem;

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
