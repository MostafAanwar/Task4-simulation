import random
import numpy as np


interArrivalTime = np.random.exponential(1 , 10**6)
arrivalTimeArray = [] 
startServiceTimeArray = [] 
waitingTimeArray = [] 
completionTimeArray = [] 
timeInSystemArray = [] 

serviceTime1 = np.random.randint(2, 4, 10**6)
serviceTime2 = []
for i in range(10**6):
    z = random.triangular(2,4,3.3)
    serviceTime2.append(z)
serviceTime3 = np.random.normal(3,0.5,10**6)

atm1 = []
atm2 = []
atm3 = []

for i in range(10**6):
    if(i == 0):             
        arrivalTimeArray.append(interArrivalTime[i])
        startServiceTimeArray.append(interArrivalTime[i])
        waitingTimeArray.append(0)
        completionTimeArray.append(startServiceTimeArray[i] + serviceTime1[i])
        timeInSystemArray.append(completionTimeArray[i] - arrivalTimeArray[i])
        atm1.append(completionTimeArray[i])
        atm2.append(0)
        atm3.append(0)
        serviceTime2[i]=0
        serviceTime3[i]=0
    else:
        arrivalTimeArray.append(arrivalTimeArray[i-1] + interArrivalTime[i])
        startServiceTimeArray.append(max(arrivalTimeArray[i],min(atm1[i-1],atm2[i-1], atm3[i-1])))
        waitingTimeArray.append(startServiceTimeArray[i]-arrivalTimeArray[i])
        if min(atm1[i-1],atm2[i-1], atm3[i-1])== atm1[i-1]:
            completionTimeArray.append(startServiceTimeArray[i] + serviceTime1[i])
            atm1.append(completionTimeArray[i])
            atm2.append(atm2[i-1])
            atm3.append(atm3[i-1])
            serviceTime2[i]=0
            serviceTime3[i]=0
        elif min(atm1[i-1],atm2[i-1], atm3[i-1])== atm2[i-1]:
            completionTimeArray.append(startServiceTimeArray[i] + serviceTime2[i])
            atm2.append(completionTimeArray[i])
            atm1.append(atm1[i-1])
            atm3.append(atm3[i-1])
            serviceTime1[i]=0
            serviceTime3[i]=0
        else:
            completionTimeArray.append(startServiceTimeArray[i] + serviceTime3[i])
            atm3.append(completionTimeArray[i])
            atm2.append(atm2[i-1])
            atm1.append(atm1[i-1])
            serviceTime1[i]=0
            serviceTime2[i]=0
        timeInSystemArray.append(completionTimeArray[i] - arrivalTimeArray[i])

UTI1 = sum(serviceTime1)/max(atm1)
UTI2 = sum(serviceTime2)/max(atm2)
UTI3 = sum(serviceTime3)/max(atm3)
averageWait = sum(waitingTimeArray)/(10**6)
maxWait = max(waitingTimeArray)

waitingPeopleNumber1Min = 0
waitingPeopleNumber = 0 
for i in range (10**6):
    if (waitingTimeArray[i] > 1):
        waitingPeopleNumber1Min = waitingPeopleNumber1Min + 1
    if (waitingTimeArray[i] > 0):
        waitingPeopleNumber = waitingPeopleNumber + 1
ProbofWait1M = (waitingPeopleNumber1Min/10**6)*100 
ProbofWait   = (waitingPeopleNumber/10**6)*100  


print("atm1 utilization: ",UTI1, "\n")
print("atm2 utilization: ",UTI2, "\n")
print("atm3 utilization: ",UTI3, "\n")
print("Average waiting time: ",averageWait,"\n")
print("Maximum waiting time: ",maxWait,"\n")
print("probability of waiting time: ",ProbofWait,"\n")
print("probability of waiting more than 1 minute: ",ProbofWait1M,"\n")