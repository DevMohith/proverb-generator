# train_model.py
from model_utils import LSTMGenerator, char_to_idx, vocab_size, seq_length
import torch
import torch.nn as nn
import pandas as pd

with open("proverbs_dataset.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

input_seq = []
target_seq = []
for i in range(len(text) - seq_length):
    input_seq.append([char_to_idx[c] for c in text[i:i+seq_length]])
    target_seq.append(char_to_idx[text[i+seq_length]])

input_seq = torch.tensor(input_seq)
target_seq = torch.tensor(target_seq)

model = LSTMGenerator(vocab_size, hidden_size=128)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)


# change epocs mainly increase for good training
epochs = 10
batch_size = 128
for epoch in range(epochs):
    total_loss = 0
    for i in range(0, len(input_seq), batch_size):
        x_batch = input_seq[i:i+batch_size]
        y_batch = target_seq[i:i+batch_size]
        output, _ = model(x_batch)
        loss = loss_fn(output, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

# saving the trained model
torch.save(model.state_dict(), "trained_model.pth")
print("✅ Model saved.")
