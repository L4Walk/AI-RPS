from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from pydantic import BaseModel

app = FastAPI()
origins = [
    "http://localhost:8080",  # 你的前端应用的地址和端口，根据实际情况进行调整
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UpdateRequest(BaseModel):
    current_state: str

# 定义石头剪刀布类，实现马尔可夫链预测
class RockPaperScissors:
    def __init__(self):
        """
        函数名：__init__
        作用：初始化RockPaperScissors类的实例
        输入参数：无
        输出结果：无
        作者：L4Walk
        """
        # 初始化状态转移计数矩阵，所有元素初始化为1以避免除零错误
        self.transition_count_matrix = np.ones((3, 3))
        # 定义状态映射，将状态名映射到索引
        self.state_mapping = {"rock": 0, "paper": 1, "scissors": 2}
        # 定义反向状态映射，将索引映射到状态名
        self.inverse_state_mapping = {0: "rock", 1: "paper", 2: "scissors"}
        # 上一状态的初始值为None
        self.previous_state = None
        # 初始化游戏轮数计数器
        self.round_count = 0

    def update_matrix(self, current_state: str):
        """
        函数名：update_matrix
        作用：根据当前状态和上一状态更新状态转移计数矩阵
        输入参数：current_state (str) - 当前状态，可以是"rock"、"paper"或"scissors"
        输出结果：无
        作者：L4Walk
        """
        if self.previous_state is not None:
            self.transition_count_matrix[self.previous_state, self.state_mapping[current_state]] += 1
        self.previous_state = self.state_mapping[current_state]

    def predict(self):
        """
        函数名：predict
        作用：根据状态转移概率预测下一状态
        输入参数：无
        输出结果：str - 预测的下一状态，可以是"rock"、"paper"或"scissors"
        作者：L4Walk
        """
        if self.previous_state is None:
            return np.random.choice(["rock", "paper", "scissors"])

        transition_probabilities = self.transition_count_matrix[self.previous_state, :] / \
                                   np.sum(self.transition_count_matrix[self.previous_state, :])

        next_state = np.argmax(transition_probabilities)
        return self.inverse_state_mapping[next_state]

    def strategy(self, prediction: str):
        """
        函数名：strategy
        作用：根据预测结果制定策略来尽量赢得游戏
        输入参数：prediction (str) - 预测的下一状态，可以是"rock"、"paper"或"scissors"
        输出结果：str - 为了赢得游戏选择的策略，可以是"rock"、"paper"或"scissors"
        作者：L4Walk
        """
        if prediction == "rock":
            return "paper"
        elif prediction == "paper":
            return "scissors"
        else:
            return "rock"


# 初始化RockPaperScissors类的实例
rps = RockPaperScissors()


@app.post("/reset/")
async def reset():
    """
    函数名：reset
    作用：重置状态为初始状态
    输入参数：无
    输出结果：字典 - 包含重置状态的字典
    作者：L4Walk
    """
    rps.__init__()  # 重新初始化RockPaperScissors类的实例
    return {"status": "reset successful"}

@app.post("/update/")
async def update(request: UpdateRequest):
    """
    函数名：update
    作用：更新状态转移计数矩阵和游戏轮数计数器
    输入参数：current_state (str) - 当前状态，可以是"rock"、"paper"或"scissors"
    输出结果：字典 - 包含状态信息的字典
    作者：L4Walk
    """
    rps.update_matrix(request.current_state)
    rps.round_count += 1  # 增加游戏轮数计数
    return {"status": "success"}


@app.get("/predict/")
async def predict():
    """
    函数名：predict
    作用：获取下一状态的预测和策略
    输入参数：无
    输出结果：字典 - 包含预测和策略的字典
    作者：L4Walk
    """
    prediction = rps.predict()
    strategy = rps.strategy(prediction)
    return {"prediction": prediction, "strategy": strategy}

@app.get("/round/")
async def get_round():
    """
    函数名：get_round
    作用：获取当前游戏轮数
    输入参数：无
    输出结果：字典 - 包含当前游戏轮数的字典
    作者：L4Walk
    """
    return {"round_count": rps.round_count}




