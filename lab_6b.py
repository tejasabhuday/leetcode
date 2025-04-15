import numpy as np

class RNN:
    def __init__(self, input_dim, hidden_dim, output_dim, lr=0.001, time_steps=5):
        self.input_dim, self.hidden_dim, self.output_dim = input_dim, hidden_dim, output_dim
        self.lr, self.time_steps = lr, time_steps
        self.Wxh = np.random.randn(hidden_dim, input_dim) * 0.01
        self.Whh = np.random.randn(hidden_dim, hidden_dim) * 0.01
        self.Why = np.random.randn(output_dim, hidden_dim) * 0.01
        self.bh = np.zeros((hidden_dim, 1))
        self.by = np.zeros((output_dim, 1))
    
    def forward(self, inputs):
        h = np.zeros((self.hidden_dim, 1))
        self.h_states, self.outputs = {-1: h}, {}
        for t in range(self.time_steps):
            h = np.tanh(self.Wxh @ inputs[t] + self.Whh @ self.h_states[t-1] + self.bh)
            self.h_states[t], self.outputs[t] = h, self.Why @ h + self.by
        return self.outputs
    
    def backward(self, inputs, targets):
        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        dh_next = np.zeros((self.hidden_dim, 1))
        for t in reversed(range(self.time_steps)):
            dy = self.outputs[t] - targets[t]
            dWhy += dy @ self.h_states[t].T
            dby += dy
            dh = self.Why.T @ dy + dh_next
            dh_raw = (1 - self.h_states[t] ** 2) * dh
            dWxh += dh_raw @ inputs[t].T
            dWhh += dh_raw @ self.h_states[t-1].T
            dbh += dh_raw
            dh_next = self.Whh.T @ dh_raw
        for param, dparam in zip([self.Wxh, self.Whh, self.Why, self.bh, self.by], [dWxh, dWhh, dWhy, dbh, dby]):
            param -= self.lr * np.clip(dparam, -5, 5)
    
    def train(self, data, labels, epochs=50):
        for epoch in range(epochs):
            loss = 0
            for x, y in zip(data, labels):
                outputs = self.forward(x)
                self.backward(x, y)
                loss += np.sum((outputs[self.time_steps-1] - y[self.time_steps-1])**2) / 2
            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

if __name__ == "__main__":
    data = [np.random.randn(5, 3, 1) * 0.1 for _ in range(100)]
    labels = [np.random.randn(5, 2, 1) * 0.1 for _ in range(100)]
    rnn = RNN(3, 4, 2)
    rnn.train(data, labels)
