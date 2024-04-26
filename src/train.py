import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from lightgbm import LGBMClassifier
from omegaconf import OmegaConf
import mlflow

# Path to train.py
file_path = os.path.dirname(__file__)

# Read configuration file
conf = OmegaConf.load(os.path.join(file_path, "config.yml"))


def train(df, params):
    print(df)
    print(params)

        
def main():
    # Load data
    data_path = os.path.join(file_path, "..", "data", "Real_Estate_Sales_2001-2021_GL.csv")
    df = pd.read_csv(data_path)
    heard = df.head(15);

    # Train model
    train(heard, conf["parameters"])


if __name__ == "__main__":
    main()
