import os
import subprocess
import torch

import config
# from data_preprocessing import 
from train import train_model
from eval import eval_model


# check if the Dataset is already cloned
if not os.path.isdir("CUB-200-2011-dataset"):
  try:
    # clone the CUB dataset from the following repository, if not available download from other sources.
    subprocess.run(["git", "clone", "https://github.com/cyizhuo/CUB-200-2011-dataset.git"], check=True)
    print("'CUB-200-2011-dataset' cloned successfully")

  except subprocess.CalledProcessError as e:
    print(f"Error occurred while cloning the repository: {e}")

else:
  print("CUB-200-2011-dataset already exists")


# Setup device-agnostic code
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# HYPERPARAMETERS
EPOCHS = config.EPOCHS
BATCH_SIZE = config.BATCH_SIZE
LEARNING_RATE = config.LEARNING_RATE
NUM_CLASSES = config.NUM_CLASSES
MODEL_NAME = config.MODEL_NAME
  

# Execute data-preprocessing
# data_preprocessing.

# Train the model
train_model(epochs=EPOCHS, 
            batch_size=BATCH_SIZE, 
            learning_rate=LEARNING_RATE, 
            num_classes=NUM_CLASSES, 
            model_name=MODEL_NAME, 
            device=device)

# Evaluate the model
# eval.evaluate_model()
