generate-dataset-disease Generates dataset.csv with patients with some state of health generated randomly according to normal values

generate-ts-disease Generates time_series.csv with history of patient with some state of health generated randomly according to normal values and sometimes with changing values that describes degradation of health status

isolation_forest.py makes initial anomaly detection of health status and after that catboost_pred.py will learn by this data how to predict if patient will feel bad in next hours
