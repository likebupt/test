from __future__ import print_function

from mpi4py import MPI
import socket
import argparse
from pathlib import Path
from uuid import uuid4

print("hostname: ", socket.gethostname(), " host ip: ", socket.gethostbyname(socket.gethostname()))

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print("Mpi rank: ", rank, " size: ", size)

parser = argparse.ArgumentParser("train")
parser.add_argument("--training_data", type=str, help="Path to training data")
parser.add_argument("--max_epochs", type=int, help="Max # of epochs for the training")
parser.add_argument("--learning_rate", type=float, help="Learning rate")
parser.add_argument("--model_output", type=str, help="Path of output model")

args = parser.parse_args()

lines = [
    f'Training data path: {args.training_data}',
    f'Max epochs: {args.max_epochs}',
    f'Learning rate: {args.learning_rate}',
    f'Model output path: {args.model_output}',
]

for line in lines:
    print(line)

# Do the train and save the trained model as a file into the output folder.
# Here only output a dummy data for demo.
model = str(uuid4())
(Path(args.model_output) / 'model').write_text(model)