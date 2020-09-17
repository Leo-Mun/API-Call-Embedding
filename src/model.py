import torch
import torch.nn as nn
import torch.nn.functional as F


class GatedCNN(nn.Module):
	def __init__(self, input_shape, kernel_size, strid):
		super(GatedCNN, self).__init__()
		self.conv1 = nn.Conv1d(input_shape, 128, kernel_size, strid)
		self.conv2 = nn.Conv1d(input_shape, 128, kernel_size, strid)

	def forward(self, input):
		out1 = F.sigmoid(self.conv1(input))
		out2 = self.conv2(input)

		out = out1 * out2
		return out


class Network(nn.Module):
	def __init__(self, input_shape):
		super(Network, self).__init__()
		self.batch1 = nn.BatchNorm1d(input_shape)
		self.batch2 = nn.BatchNorm1d(128)

		self.gate1 = GatedCNN(input_shape, 2, 1)
		self.gate2 = GatedCNN(input_shape, 3, 1)

		self.lstm = nn.LSTM(197, 100, bidirectional=True)
		self.gap = nn.AdaptiveMaxPool1d(100)

		self.layer1 = nn.Sequential(
			nn.Linear(100, 64),
			nn.ReLU(),
			nn.Dropout(0.5),
			nn.Linear(64, 1),
			nn.Sigmoid()
		)

	def forward(self, input):
		out = self.batch1(input)

		out1 = self.gate1(out)
		out2 = self.gate2(out)

		out = torch.cat([out1, out2], dim=2)
		out, _ = self.lstm(out)
		out = self.gap(out)
		out = self.layer1(out)
		return out
