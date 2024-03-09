import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.hidden_sizes = hidden_size
        self.output_size = num_classes

        # Create a list of fully connected layers based on the number of hidden layers specified
        layers = []
        for i in range(hidden_size):
            if i == 0:
                # First hidden layer - input size is the input layer size
                layers.append(nn.Linear(str(input_size), str(hidden_size[i])))
            else:
                # Subsequent hidden layers - input size is the previous hidden layer size
                layers.append(nn.Linear(hidden_size[i - 1], hidden_size[i]))
            layers.append(nn.ReLU())
        # Output layer - input size is the final hidden layer size, output size is the output layer size
        layers.append(nn.Linear(hidden_size[-1], num_classes))

        # Create a sequential container for the layers
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        # Flatten the input tensor
        x = x.view(-1, self.input_size)
        # Pass the tensor through the layers
        out = self.layers(x)
        return out
