#Hyperparameter optimization - Finding optimal model configuration settings to maximize performance.

#pseudocode....
from hyperopt import fmin, hp, SparkTrials

space = {"learning_rate": hp.loguniform("lr", -5, -1), 
         "max_depth": hp.randint("md", 4, 100)}

def train_model(params):
    # XGBoost training
    return AUC 

best_params = fmin(fn = train_model, space = space, 
                   trials = SparkTrials(), algo = tpe.suggest, 
                   max_evals = 100)