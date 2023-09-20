<template>
  <div>
    <label for="choice">Choose Rock, Paper or Scissors: </label>
    <select v-model="choice">
      <option value="rock">Rock</option>
      <option value="paper">Paper</option>
      <option value="scissors">Scissors</option>
    </select>
    <button @click="update">Submit</button>

    <!-- 根据当前的状态转移概率预测下一状态。 -->
    <div>Prediction: {{ prediction }}</div>

    <!-- 根据当前状态和预测状态，选择一个动作。 -->
    <div>Strategy(AI的选择): {{ strategy }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      choice: 'rock',
      prediction: '',
      strategy: '',
    };
  },
  methods: {
    async update() {
      //console.log('Choice: ' + this.choice)
      // Update the state
      await axios.post('http://127.0.0.1:8000/update/', { current_state: this.choice });

      // Get the prediction and strategy
      const response = await axios.get('http://127.0.0.1:8000/predict/');
      this.prediction = response.data.prediction;
      this.strategy = response.data.strategy;
    },
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f0f0f0;
}
</style>
