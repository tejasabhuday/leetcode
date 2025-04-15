import numpy as np
import matplotlib.pyplot as plt

class SelfOrganizingMap:
    def __init__(self, input_dim, grid_size, learning_rate=0.1, radius=None, epochs=100):
        self.input_dim = input_dim
        self.grid_size = grid_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.radius = radius if radius else max(grid_size) / 2
        self.weights = np.random.rand(grid_size[0], grid_size[1], input_dim)

    def find_bmu(self, sample):
        distances = np.linalg.norm(self.weights - sample, axis=2)
        return np.unravel_index(np.argmin(distances), distances.shape)

    def update_weights(self, sample, bmu):
        x, y = np.meshgrid(np.arange(self.grid_size[0]), np.arange(self.grid_size[1]), indexing='ij')
        dist_to_bmu = np.sqrt((x - bmu[0]) ** 2 + (y - bmu[1]) ** 2)
        mask = dist_to_bmu <= self.radius
        influence = np.exp(-dist_to_bmu**2 / (2 * (self.radius**2))) * mask
        influence = influence[..., np.newaxis]
        self.weights += self.learning_rate * influence * (sample - self.weights)

    def train(self, data):
        for epoch in range(self.epochs):
            for sample in data:
                bmu = self.find_bmu(sample)
                self.update_weights(sample, bmu)
            self.learning_rate *= 0.995
            self.radius *= 0.995

    def visualize(self):
        plt.imshow(self.weights.reshape(self.grid_size[0], self.grid_size[1], self.input_dim))
        plt.title("Self-Organizing Map - Tejas Abhuday Pandey")
        plt.show()

if __name__ == "__main__":
    data = np.random.rand(100, 3)
    som = SelfOrganizingMap(input_dim=3, grid_size=(10, 10))
    som.train(data)
    som.visualize()
