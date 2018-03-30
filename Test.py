import numpy as np

Predicted = np.genfromtxt("C:/Users/Poori/Desktop/Parinama/MakePianoRoll/SmallDataSet/PianoRolls/Prediction_reshaped.csv",delimiter=",")
Prediction_reshaped= np.zeros((Predicted.shape[0], Predicted.shape[1]))
for l in range(0,Predicted.shape[0]):
     p = np.argmax(Predicted[l,:])
     Prediction_reshaped[l,p]=1


np.savetxt("C:/Users/Poori/Desktop/Parinama/MakePianoRoll/SmallDataSet/PianoRolls/Prediction.csv", Prediction_reshaped, delimiter=",") 
print(11) 