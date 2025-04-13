# train_model.py
from model_utils import LSTMGenerator, char_to_idx, vocab_size, seq_length
import torch
import torch.nn as nn
import pandas as pd
from model_utils import generate_text


with open("proverbs_dataset.txt.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

input_seq = []
target_seq = []
for i in range(len(text) - seq_length):
    input_seq.append([char_to_idx[c] for c in text[i:i+seq_length]])
    target_seq.append(char_to_idx[text[i+seq_length]])

input_seq = torch.tensor(input_seq)
target_seq = torch.tensor(target_seq)

model = LSTMGenerator(vocab_size, hidden_size=128)
# ✅ Try to load previously saved model weights (for continued training)
try:
    model.load_state_dict(torch.load("trained_model.pth"))
    print("🔁 Loaded existing model weights. Continuing training...")
except FileNotFoundError:
    print("🚀 No pre-trained model found. Starting fresh.")

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)


# change epocs mainly increase for good training
epochs = 50
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

    # 💬 Show sample output after training this epoch
    if (epoch + 1) % 1 == 0:
        print("🔮 Sample Proverb:")
        print(generate_text(model, seed_text="friendship"))

    # 💾 Save model every few epochs
    if (epoch + 1) % 5 == 0:
        torch.save(model.state_dict(), "trained_model.pth")
        print("✅ Model checkpoint saved!")

# saving the trained model
torch.save(model.state_dict(), "trained_model.pth")
print("✅ Model saved.")
