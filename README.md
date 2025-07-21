# MNIST 手写数字识别 Web 应用（深度学习入门模板）

本项目是一个基于 PyTorch 的 MNIST 手写数字识别模型，并通过 Flask 提供 Web API 推理服务。适合深度学习初学者练手与扩展。

## 目录结构

```
mnist-web-demo/
│
├── data/            # MNIST 数据自动下载，无需手动放数据
├── models/          # 训练后模型会保存在这里
├── app/             # Web API 服务代码
│   └── app.py
├── train.py         # 训练脚本
├── requirements.txt # 依赖包清单
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 训练模型

```bash
python train.py
```
训练结束后，模型会保存到 `models/mnist.pth`。

### 3. 启动 Web API 服务

```bash
cd app
python app.py
```
本地访问：http://127.0.0.1:5000

### 4. 使用推理 API

**接口地址：** `/predict`  
**请求方式：** POST  
**参数：** 上传一张手写数字图片（灰度、28x28，或任意图片会自动归一化）

**curl 示例：**
```bash
curl -F "file=@digit.png" http://127.0.0.1:5000/predict
```
返回：
```json
{"prediction": 7}
```

## 扩展建议

- 尝试更复杂的神经网络（如卷积神经网络 CNN）
- 前端界面输入数字，实现手写板上传
- 用 Gradio/Streamlit 部署可视化 Demo
- 尝试将模型部署到 Hugging Face Spaces 或云平台

## 参考资料

- [PyTorch MNIST 官方教程](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)
- [Flask 官方文档](https://flask.palletsprojects.com/)
- [Gradio 快速部署 Web Demo](https://gradio.app/)
