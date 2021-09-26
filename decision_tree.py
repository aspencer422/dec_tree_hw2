#-------------------------------------------------------------------------
# AUTHOR: Anthony Spencer
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 and a hlaf hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    X = []
    for i in range(len(dbTraining)):
        column = []
        for j in range(4):
            if dbTraining[i][j] == 'Young' or dbTraining[i][j] == 'Myope' or dbTraining[i][j] == 'No' or dbTraining[i][j] == 'Reduced':
                column.append(1)
            elif dbTraining[i][j] == 'Prepresbyopic' or dbTraining[i][j] == 'Hypermetrope' or dbTraining[i][j] == 'Yes' or dbTraining[i][j] == 'Normal':
                column.append(2)
            elif dbTraining[i][j] =='Presbyopic':
                column.append(3)
        X.append(column)
    #print(X)
    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for i in range(len(dbTraining)):
        if dbTraining[i][4] == 'No':
            Y.append(2)
        else:
            Y.append(1)
    #print(Y)
    #loop your training and test tasks 10 times here
    result=[]
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest = []
       with open('contact_lens_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for B, row in enumerate(reader):
            if B > 0: #skipping the header
                dbTest.append (row)
                #print(row)
        Z = []
        for N in range(len(dbTest)):
            column2 = []
            for j in range(4):
                if dbTraining[N][j] == 'Young' or dbTraining[N][j] == 'Myope' or dbTraining[N][j] == 'No' or dbTraining[N][j] == 'Reduced':
                    column2.append(1)
                elif dbTraining[N][j] == 'Prepresbyopic' or dbTraining[N][j] == 'Hypermetrope' or dbTraining[N][j] == 'Yes' or dbTraining[N][j] == 'Normal':
                    column2.append(2)
                elif dbTraining[N][j] =='Presbyopic':
                    column2.append(3)
            Z.append(column2)
        M=0
        correct=0
        
        for data in Z:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            class_predicted = clf.predict([data])[0]
           

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            
            if dbTest[M][4]=='No':
                testPred = 2
            else:
                testPred = 1
            if class_predicted == testPred:
                correct+=1
                #print("correct")
            M+=1
        result.append(correct/len(dbTest))


        #find the lowest accuracy of this model during the 10 runs (training and test set)
        lowest=result[0]
        #print(result)
        for k in range(len(result)):
            if result[k] <= lowest:
                lowest = result[k]

    #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    if ds =='contact_lens_training_1.csv':
        print("final accuracy when training on contact_lens_training_1.csv: "+ str(lowest))
    elif ds =='contact_lens_training_2.csv':
        print("final accuracy when training on contact_lens_training_2.csv: "+ str(lowest))
    else:
        print("final accuracy when training on contact_lens_training_3.csv: "+ str(lowest))



