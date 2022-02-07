from nbresult import ChallengeResult

import pandas as pd

data = pd.read_csv("https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Houses_dataset.csv", nrows=5)

result = ChallengeResult(
    'data',
    data=data)

result.write()
