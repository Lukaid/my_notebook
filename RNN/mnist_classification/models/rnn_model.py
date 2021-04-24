import torch
import torch.nn as nn


class SequenceClassifier(nn.Module):

    def __init__(
        self,
        input_size,
        hidden_size,
        output_size,
        n_layers=4,
        dropout_p=.2,
    ):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers
        self.dropout_p = dropout_p

        super().__init__()

        self.rnn = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=n_layers,
            batch_first=True,  # 얘를 먼저 써줘야 (bs, ts, vs)이렇게 배치사이즈가 먼저 들어감
            dropout=dropout_p,  # RNN은 batch normalization을 쓸 수 없다.
            bidirectional=True,
        )
        self.layers = nn.Sequential(  # 이건 마지막에 yhat을 구하는 텀
            nn.ReLU(),
            nn.BatchNorm1d(hidden_size * 2),
            nn.Linear(hidden_size * 2, output_size),
            nn.LogSoftmax(dim=-1),
        )

    def forward(self, x):
        # |x| = (batch_size, h, w)
        # 배치사이즈, 타임 스텝, 입력의 크기

        z, _ = self.rnn(x)  # 마지막 time step의 hidden state와 cell state를 반환
        # |z| = (batch_size, h, hidden_size * 2)
        # 배치 , 시퀀스 (타임스텝), 피쳐
        z = z[:, -1]  # 맨마지막 타임스텝만 짤라옴
        # |z| = (batch_size, hidden_size * 2)
        y = self.layers(z)
        # |y| = (batch_size, output_size)

        return y
