<template>
  <div>
<!--
    <b-navbar is-active=True>
        <template slot="end">
            <b-navbar-item tag="div">
              <router-link to="/">Home</router-link> |
              <router-link to="/about">About</router-link>
            </b-navbar-item>
        </template>
    </b-navbar>-->

    <router-view/>
    <footer class="footer">
      <div class="content has-text-centered">
        <img src="./assets/open_weather_logo.png" style="height:40px;"><br/>
        Weather data powered by OpenWeather<br/>
        Population data from <a href="https://worldpopulationreview.com/world-cities/">https://worldpopulationreview.com/world-cities/</a>
      </div>
    </footer>
  </div>
</template>

<style lang="scss">
  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";

  $footer-background-color: #84a9ac;
  $section-padding: 2.5rem 1.5rem;

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
