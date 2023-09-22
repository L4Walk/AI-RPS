<template>
<div>
  <img src="../assets/blueshirt.png" width="200px">
  <h1>AI小游戏-剪刀石头布</h1>
  <div class="choices">
      <img @click="makeChoice('rock')" :class="{ selected: userChoice === 'rock' }" src="../assets/rock.png" alt="Rock" >
      <img @click="makeChoice('paper')" :class="{ selected: userChoice === 'paper' }" src="../assets/paper.png" alt="Paper" >
      <img @click="makeChoice('scissors')" :class="{ selected: userChoice === 'scissors' }" src="../assets/scissors.png" alt="Scissors" >
  </div>
  <nut-button plain type="primary" @click="reset">重置</nut-button>
  <div></div>
  <nut-button block type="primary" @click="update" color="#3170a7">选择这个</nut-button>

  <h2>第{{ round }}轮的比赛结果</h2>
  <!-- 根据当前的状态转移概率预测下一状态。
  <div>Prediction: {{ prediction }}</div>
  -->
  <!-- 根据当前状态和预测状态，选择一个动作。 -->
  <div>AI的选择: {{ strategy }}</div>
  <div v-if="strategy !== null">
      <img v-if="strategy === ''" src="../assets/gif.gif" alt="Loading">
      <img v-if="strategy === 'rock'" src="../assets/rock.png" alt="Rock">
      <img v-if="strategy === 'paper'" src="../assets/paper.png" alt="Paper">
      <img v-if="strategy === 'scissors'" src="../assets/scissors.png" alt="Scissors">
  </div>


  <!-- 根据当前状态和预测状态，选择一个动作。 -->
  <h3>获胜{{ win_count }}轮</h3>
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
      roundRes: [],
      win_count: 0,
    };
  },
  methods: {
    makeChoice(choice) {
      // Set the user's choice

      this.userChoice = choice;
      console.log('Choice: ' + this.userChoice)
    },

    async reset(){
      console.log("重制")
      await axios.post('http://127.0.0.1:8000/reset/', {
      });

      this.win_count = 0;
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

      this.roundRes.push({
        round: this.round,
        userChoice:this.userChoice,
        aiStrategy: this.strategy,
        result: this.result
      });

      if(this.result == "win"){
        this.win_count++;
      }


      //const gameResult = updateResponse.data.result;
      //console.log('Result: ' + this.result);

      // Get the prediction and strategy
      //const response = await axios.get('http://rps.chuheng.tech/predict/');
      //this.prediction = response.data.prediction;
      //this.strategy = response.data.strategy;

        // 延迟 5 秒后重新设置 strategy 变量的值以重新加载
        setTimeout(() => {
        this.strategy = '';
      }, 3000);
    },
  },
  computed: {

    resultStatistics(){
    return this.roundRes.map(result =>
      `第${result.round}轮: 玩家选择${result.userChoice}, AI选择${ result.aiStrategy }，比赛结果${ result.result}`
    ).join('\n');
  }
  }
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
