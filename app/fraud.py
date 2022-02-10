import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

def fraud_prediction(fraud):

    ccd=pd.read_csv("creditcard.csv")

    ccd['Class'].value_counts()
    valid = ccd[ccd.Class==0]
    fraud = ccd[ccd.Class==1]
    valid_sample=valid.sample(n=492)
    new_sample_dataset= pd.concat([valid_sample , fraud] , axis=0)

    x=new_sample_dataset.drop(columns='Class',axis=1)
    y=new_sample_dataset['Class']
    x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.2 , stratify=y , random_state=2)
    model=LogisticRegression()
    model.fit(x_train , y_train)
    x_train_prediction= model.predict(x_train)
    training_accuracy=accuracy_score(x_train_prediction , y_train)
    x_test_prediction=model.predict(x_test)
    testing_accuracy=accuracy_score(x_test_prediction , y_test)

    return testing_accuracy


