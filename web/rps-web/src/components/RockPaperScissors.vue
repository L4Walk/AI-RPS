<template>
<div>
  <img src="../assets/blueshirt.png">
  <h1>AI小游戏-剪刀石头布</h1>
  <div class="choices">
      <img @click="makeChoice('rock')" :class="{ selected: userChoice === 'rock' }" src="../assets/rock.png" alt="Rock" >
      <img @click="makeChoice('paper')" :class="{ selected: userChoice === 'paper' }" src="../assets/paper.png" alt="Paper" >
      <img @click="makeChoice('scissors')" :class="{ selected: userChoice === 'scissors' }" src="../assets/scissors.png" alt="Scissors" >
  </div>
  <button @click="update">Play</button>

  <h2>第{{ round }}轮的比赛结果</h2>
  <!-- 根据当前的状态转移概率预测下一状态。
  <div>Prediction: {{ prediction }}</div>
  -->
  <!-- 根据当前状态和预测状态，选择一个动作。 -->
  <div>Strategy(AI的选择): {{ strategy }}</div>
  <div v-if="strategy !== null">
      <img v-if="strategy === ''" src="../assets/gif.gif" alt="Loading">
      <img v-if="strategy === 'rock'" src="../assets/rock.png" alt="Rock">
      <img v-if="strategy === 'paper'" src="../assets/paper.png" alt="Paper">
      <img v-if="strategy === 'scissors'" src="../assets/scissors.png" alt="Scissors">
  </div>



  <!-- 根据当前状态和预测状态，选择一个动作。 -->
  <div>比赛结果: {{ result }}</div>

  <div v-if="result">
      <img v-if="result === 'You win!'" src="win.png" alt="Win">
      <img v-if="result === 'Computer wins!'" src="lose.png" alt="Lose">
      <img v-if="result === 'It s a tie!'" src="tie.png" alt="Tie">
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userChoice: null,
      choice: 'rock',
      prediction: '',
      strategy: '',
      round: 1,
      result: '',
    };
  },
  methods: {
    makeChoice(choice) {
      // Set the user's choice

      this.userChoice = choice;
      console.log('Choice: ' + this.userChoice)
    },

    async update() {
      console.log('Choice: ' + this.userChoice)

      // Update the state and get the game result
      const updateResponse = await axios.post('http://127.0.0.1:8000/update/', {
        current_state: this.userChoice,
        user_choice: this.userChoice
      });

      this.strategy = updateResponse.data.strategy;
      this.round = updateResponse.data.round;
      this.result = updateResponse.data.result;
      //const gameResult = updateResponse.data.result;
      //console.log('Result: ' + this.result);

      // Get the prediction and strategy
      //const response = await axios.get('http://rps.chuheng.tech/predict/');
      //this.prediction = response.data.prediction;
      //this.strategy = response.data.strategy;

        // 延迟 5 秒后重新设置 strategy 变量的值以重新加载
        setTimeout(() => {
        this.strategy = '';
      }, 2500);
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

.selected {
  border: 2px solid blue;
}

.choices {
  display: flex;
  justify-content: space-between; /* Adjust as needed */
}

img {
    width: 100px;
    height: auto;
}
</style>
