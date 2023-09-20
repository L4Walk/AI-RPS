<template>
  <div id="app">
    <RockPaperScissors />
  </div>
</template>

<script>
import RockPaperScissors from './components/RockPaperScissors.vue';

export default {
  name: 'App',
  components: {
    RockPaperScissors,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
