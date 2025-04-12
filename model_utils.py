# model_utils.py
import torch
import torch.nn as nn
import numpy as np
import random

with open("proverbs_dataset.txt.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

chars = sorted(list(set(text)))
char_to_idx = {c: i for i, c in enumerate(chars)}
idx_to_char = {i: c for c, i in char_to_idx.items()}
vocab_size = len(chars)
seq_length = 40

class LSTMGenerator(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_layers=1):
        super().__init__()
        self.hidden_size = hidden_size
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        output, hidden = self.lstm(x, hidden)
        out = self.fc(output[:, -1, :])
        return out, hidden

def load_model():
    model = LSTMGenerator(vocab_size, hidden_size=128)
    model.load_state_dict(torch.load("trained_model.pth", map_location=torch.device('cpu')))
    model.eval()
    return model

def generate_text(model, seed_text="discipline", length=100):
    greeting = random.choice([
        "Hello!", "Good day!", "Namaste!", 
        "Greetings!", "Hi Matcha!", "My Friend!"
    ])
    input_chars = seed_text[-seq_length:].lower().rjust(seq_length)
    input_idx = torch.tensor([[char_to_idx.get(c, 0) for c in input_chars]])

    result = greeting + "\n"
    hidden = None

    for _ in range(length):
        output, hidden = model(input_idx, hidden)
        probs = torch.softmax(output, dim=-1).detach().numpy().ravel()
        idx = np.random.choice(len(probs), p=probs)
        char = idx_to_char[idx]
        result += char
        input_idx = torch.tensor([[*input_idx[0][1:], idx]])

    return result
