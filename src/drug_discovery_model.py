"""
Studi Kasus 2: Penemuan Molekul Baru dengan Machine Learning
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Contoh data dummy (gantilah dengan data molekul nyata seperti dari ChEMBL)
def train_model():
    data = pd.DataFrame({
        'molecular_weight': [150, 300, 500, 700],
        'toxicity': [0.1, 0.3, 0.8, 0.6],
        'efficacy': [1, 1, 0, 0]
    })
    X = data[['molecular_weight', 'toxicity']]
    y = data['efficacy']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Akurasi:", accuracy_score(y_test, y_pred))

# train_model()
