import torch
import torch.nn as nn
from flask import Flask, request, jsonify
from PIL import Image
import io
import torchvision.transforms as transforms

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc(x)
        return x

app = Flask(__name__)

model = SimpleNet()
model.load_state_dict(torch.load("../models/mnist.pth", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400
    file = request.files["file"]
    img = Image.open(file.stream).convert("L")
    img = transform(img)
    img = img.unsqueeze(0)
    with torch.no_grad():
        out = model(img)
        pred = out.argmax(dim=1).item()
    return jsonify({"prediction": int(pred)})

if __name__ == "__main__":
    app.run(debug=True)
