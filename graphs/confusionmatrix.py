from sklearn.metrics import confusion_matrix
import numpy as np

# Example true labels and predicted labels
y_true = [0, 1, 0, 1, 0, 1, 1, 0]  # Actual labels
y_pred = [0, 0, 0, 1, 0, 1, 1, 1]  # Predicted labels

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Display the confusion matrix
print("Confusion Matrix:")
print(cm)


from sklearn.metrics import confusion_matrix
import numpy as np

# Example true labels and predicted labels
y_true = [0, 1, 0, 1, 0, 1, 1, 0]  # Actual labels
y_pred = [0, 0, 0, 1, 0, 1, 1, 1]  # Predicted labels

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Display the confusion matrix
print("Confusion Matrix:")
print(cm)


#A heatmap is a graphical representation of data where individual values are
#  represented by colors. It is typically used to visualize large datasets in a
#   way that makes patterns, variations, and correlations easy to detect.

from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix , classification_report
import pandas as pd
import seaborn sns

def print_confusion_matrix(confusion_matrix, class_names, figsize = (10,7), fontsize=14):

    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names, 
    )
    fig = plt.figure(figsize=figsize)
    try:
      heatmap = sns.heatmap(df_cm, annot=True, fmt="d", cmap='Blues', 
                      linewidths=.5, linecolor='black')

#         annot=True: Ensures that each cell displays its numerical value.
#         fmt="d": Specifies that the values are integers (whole numbers).

    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)

   # tick lables : Text or numbers on the ticks of the axes. Positioned along the axis where tick marks are placed.
   # ha:  Aligns the labels to the right.

    plt.ylabel('Truth')
    plt.xlabel('Prediction')

truth =      ["Dog","Not a dog","Dog","Dog",      "Dog", "Not a dog", "Not a dog", "Dog",       "Dog", "Not a dog"]
prediction = ["Dog","Dog",      "Dog","Not a dog","Dog", "Not a dog", "Dog",       "Not a dog", "Dog", "Dog"]

cm = confusion_matrix(truth,prediction)
print("cm",cm)

print_confusion_matrix(cm,["Dog","Not a dog"])
print(classification_report(truth, prediction))

 #Precision
 # Precision tells us how many of the items the model classified as a certain class were actually that class.  (kah jo class predict kia tha wo kitne % sahi tha)
# Precision
# Preceision Rate =  TP / predicted yes
# negative predictive value
# negative predictive value = TN / predicted no



# Recall
# Recall tells us how many of the items that actually belonged to a certain class were classified by the model as that class. (kitne % actual class ko predict kia tha)

# true positive rate (sensivity, recall)
# true positive rate =  TP / Actual yes
# false positive rate (fall-out)
# false positive rate = FP / Actual no
# true negative rate (specificity)
# true negative rate = TN / Actual no
# false negative rate
# false negative rate = FN / Actual yes


# F1 Score
# F1 Score is the weighted average of Precision and Recall. It takes both false positives and false negatives into account. (Precision or Recall ka average)
#In Simple Terms: It combines precision and recall into one score. Higher F1-score means better performance.
# F1 score
# F1 score = 2 * (Precision * Recall) / (Precision + Recall)

# support
# The number of samples of the true response that lie in that class.(kah kitny samples actual class mei hain)
#How many real examples of each class were in the test data?

# Accuracy
# Accuracy is the proportion of true results (both true positives and true negatives) among the total number of cases examined. (kitne % sahi predict kia)
# Acuuracy  
# Accuracy = (TP + TN) / total   


# misclassification rate (error rate)
# misclassification rate = FP + FN / total
# error rate = 1 - accuracy


#confusion matrix










