# AI-RPS
利用马尔可夫链实现石头剪刀布

### 后端启动方式
```bash
cd server
```
需安装Uvicorn: 
`pip install  uvicorn`

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

或
```bash
uvicorn main:app --reload
```

### 前端启动方式
```bash
cd  web/rps-web/
npm install
npm run serve
```
