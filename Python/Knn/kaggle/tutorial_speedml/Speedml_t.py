import pandas as pd
import numpy as np
import random as rnd


def analysis():
    train_df = pd.read_csv('train.csv')
    test_df = pd.read_csv('test.csv')
    combine = [train_df, test_df]
    shape = train_df.shape
    print('shape = ', shape)
    print('-' * 50)
    print(train_df.columns.values)
    print(train_df.head(10))
    print('-' * 60)
    print(train_df.tail(10))
    print('=' * 50)
    print(train_df.info())
    print('=' * 50)
    print(test_df.info())
    print('-' * 50)
    print(train_df.describe())
    print("-" * 50)
    print(train_df.describe(include=['O']))


analysis()
