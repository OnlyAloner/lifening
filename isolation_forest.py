""" Module to detect anomalies in the health prediction model """

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset.csv')

model = IsolationForest(max_samples=1000,
                        contamination=0.05)

actual = df['is_anomaly']
df.drop(columns=['is_anomaly'], inplace=True)

model.fit(df)
anomaly_score = model.decision_function(df)

normalized_score = (anomaly_score - anomaly_score.min()) / \
    (anomaly_score.max() - anomaly_score.min())

df['anomaly'] = - (normalized_score - 1)
df['predicted'] = round(df['anomaly'])

accuracy = (actual == df['predicted']).mean()
f1 = f1_score(actual, df['predicted'])
cm = confusion_matrix(actual, df['predicted'])


fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, annot_kws={"size": 35})
ax.set_xlabel('Predicted labels', fontsize=18)
ax.set_ylabel('Actual labels', fontsize=18)
ax.set_title('Confusion Matrix', fontsize=18)
ax.xaxis.set_ticklabels(['Normal', 'Disease'], fontsize=18)
ax.yaxis.set_ticklabels(['Normal', 'Disease'], fontsize=18)
ax.text(0.5, 1.1, f"Accuracy: {accuracy*100:.2f}%", ha='center', va='center', transform=ax.transAxes, fontsize=18)
ax.text(0.5, 1.05, f"F1 Score: {f1*100:.2f}%", ha='center', va='center', transform=ax.transAxes, fontsize=18)

plt.show()


df.to_csv('anomaly.csv', index=False)
