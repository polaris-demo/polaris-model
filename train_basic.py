import polaris
import pickle
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
import pandas as pd

def train():
  # NOTE (Josh): this should actually access the persistent artifact from fetch_data NOT us the PV...
  df = pd.read_pickle("/mnt/vol/repo/artifacts/data.pkl")
  train_X = df[["fixed_acidity", "residual_sugar"]]
  train_Y = df["quality"]

  l2 = polaris.train.parameters.get("l2")
  
  model = Ridge(alpha=l2)
  pipeline = Pipeline([("ridge", model)])

  pipeline.fit(train_X, train_Y)

  r2 = pipeline.score(train_X, train_Y)
  polaris.train.metrics.record("r2", r2)

  # save off the artifact to the artifact storage dir
  model_path = polaris.artifacts.path_for("reg_model")
  with open(model_path, "wb") as f:
    pickle.dump(pipeline, f)

if __name__ == "__main__":
  train() # run the train function

