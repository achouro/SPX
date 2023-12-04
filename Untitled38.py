#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


def plot_confusion_matrix(y,y_predict):
    "this function plots the confusion matrix"
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y, y_predict)
    ax= plt.subplot()
    sns.heatmap(cm, annot=True, ax = ax); #annot=True to annotate cells
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix'); 
    ax.xaxis.set_ticklabels(['did not land', 'land']); ax.yaxis.set_ticklabels(['did not land', 'landed']) 
    plt.show() 


# In[3]:


URL1 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
data=pd.read_csv(URL1)
data.head()


# In[4]:


URL2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv'
X=pd.read_csv(URL2)
X.head()


# In[5]:


Y=data['Class'].to_numpy()


# In[6]:


transform=preprocessing.StandardScaler()
X=transform.fit(X).transform(X.astype(float))


# In[7]:


X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.2, random_state=2)

Y_test.shape


# In[29]:


parameters ={'C':[0.01,0.1,1],
             'penalty':['l2'],
             'solver':['lbfgs']}


# In[30]:


parameters ={"C":[0.01,0.1,1],'penalty':['l2'], 'solver':['lbfgs']}# l1 lasso l2 ridge
lr=LogisticRegression()
logreg_cv=GridSearchCV(estimator=lr, cv=10, param_grid= parameters)
logreg_cv.fit(X_train ,Y_train)


# In[31]:


print("tuned hpyerparameters :(best parameters) ",logreg_cv.best_params_)
print("accuracy :",logreg_cv.best_score_)


# In[32]:


yhat=logreg_cv.predict(X_test)
logreg_cv.score(X_test, Y_test)


# In[33]:


yhat=logreg_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhat)


# In[20]:


parametersu = {'kernel':('linear', 'rbf','poly','rbf', 'sigmoid'),
              'C': np.logspace(-3, 3, 5),
              'gamma':np.logspace(-3, 3, 5)}
svm= SVC()


# In[21]:


svm_cv=GridSearchCV(estimator= svm, cv= 10, param_grid=parametersu)
svm_cv.fit(X_train, Y_train)


# In[22]:


print("tuned hpyerparameters :(best parameters) ",svm_cv.best_params_)
print("accuracy :",svm_cv.best_score_)


# In[23]:


svm_cv.score(X_train, Y_train)


# In[24]:


yhatu=svm_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhatu)


# In[9]:


parametersuu = {'criterion': ['gini', 'entropy'],
     'splitter': ['best', 'random'],
     'max_depth': [2*n for n in range(1,10)],
     'max_features': ['auto', 'sqrt'],
     'min_samples_leaf': [1, 2, 4],
     'min_samples_split': [2, 5, 10]}
tree= DecisionTreeClassifier()


# In[10]:


tree_cv=GridSearchCV(estimator= tree, cv=10, param_grid=parametersuu)
tree_cv.fit(X_train, Y_train)


# In[11]:


print("tuned hpyerparameters :(best parameters) ",tree_cv.best_params_)
print("accuracy :",tree_cv.best_score_)


# In[12]:


tree_cv.score(X_test, Y_test)


# In[13]:


yhatuu=tree_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhatuu)


# In[14]:


parametersuuu = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'p': [1,2]}

KNN= KNeighborsClassifier()


# In[15]:


KNN_cv=GridSearchCV(estimator=KNN, cv=10, param_grid= parametersuuu)
KNN_cv.fit(X_train, Y_train)


# In[19]:


print("tuned hpyerparameters :(best parameters) ",KNN_cv.best_params_)
print("accuracy :",KNN_cv.best_score_)


# In[17]:


KNN_cv.score(X_test, Y_test)


# In[25]:


yhatuuu=KNN_cv.predict(X_test)
plot_confusion_matrix(Y_test,yhatuuu)


# In[71]:


print("Model\t\t\tTestAccuracy\tTrainAccuracy")
print( "Logistic Regression:\t",logreg_cv.score(X_test, Y_test).round(5),"\t", logreg_cv.best_score_.round(5))
print("Support Vector Machine:\t",svm_cv.score(X_test, Y_test).round(5),"\t", svm_cv.best_score_.round(5))
print( "Decison Tree: \t\t", tree_cv.score(X_test, Y_test).round(5),"\t", tree_cv.best_score_.round(5)) 
print("K-Nearest Neeighbor: \t", KNN_cv.score(X_test, Y_test).round(5),"\t", KNN_cv.best_score_.round(5))
    
print("The best estimator is:\t", max(logreg_cv.score(X_test, Y_test),
                               svm_cv.score(X_test, Y_test),
                               tree_cv.score(X_test, Y_test),
                               KNN_cv.score(X_test, Y_test)).round(5),"\t", 
     max(logreg_cv.best_score_,
         svm_cv.best_score_,
         tree_cv.best_score_,
         KNN_cv.best_score_).round(5), )


# In[49]:


print("Model\t\tAccuracy\tTestAccuracy")#,logreg_cv.best_score_)
print("LogReg\t\t{}\t\t{}".format((logreg_cv.best_score_).round(5), logreg_cv.score(X_test, Y_test).round(5)))
print("SVM\t\t{}\t\t{}".format((svm_cv.best_score_).round(5), svm_cv.score(X_test, Y_test).round(5)))
print("Tree\t\t{}\t\t{}".format((tree_cv.best_score_).round(5), tree_cv.score(X_test, Y_test).round(5)))
print("KNN\t\t{}\t\t{}".format((knn_cv.best_score_).round(5), knn_cv.score(X_test, Y_test).round(5)))

