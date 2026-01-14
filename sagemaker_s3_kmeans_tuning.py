#Sagemaker kmeans++ hyperparameter optimization - Define hyperparameter ranges for the KMeans estimator

#yourothercode....

import boto3
from sagemaker.tuner import IntegerParameter, CategoricalParameter, HyperparameterTuner

sagemaker_session = boto3.Session().client(service_name='sagemaker') 

hyperparameter_ranges = {
    'k': IntegerParameter(2, 10),  
    'init': CategoricalParameter(['kmeans++', 'random']),
    'max_iterations': IntegerParameter(50, 200),
}

tuner = HyperparameterTuner(
    sagemaker_session=sagemaker_session,
    estimator=kmeans_estimator,
    objective_metric_name='test:msd',
    hyperparameter_ranges=hyperparameter_ranges,
    max_jobs=20,
    max_parallel_jobs=3)

tuner.fit(inputs={'train': s3_train_data, 'test': s3_test_data})

best_params = tuner.best_training_job().hyperparameters