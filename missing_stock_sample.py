import numpy as np
import sys
import pandas as pd
def ema(s, n):
    ema = []
    j = 1
    sma = sum(s[:n]) / n
    multiplier = 0.1
    multiplier2 = 0.1
    ema.append(sma)
    for i in range(1,len(s)-1):
        tmp = (s[i] - ema[-1])* multiplier + ema[-1]
        ema.append(tmp)
    #ema.append(( (s[n] - sma) * multiplier) + sma)
    ema2 = []
    #j2 = 1
    sma2 = sum(ema[:n]) / n
    ema2.append(sma2)
    for i in range(1,len(s)-1):
        tmp = (ema[i] - ema2[-1])* multiplier2 + ema2[-1]
        ema2.append(tmp)
    #ema2.append(( (ema[n] - sma2) * multiplier) + sma2)
    a = 2.0*ema[-1] - ema2[-1]
    b = multiplier2/(1-multiplier2)*(ema[-1]-ema2[-1])
    return a+b
N = int(raw_input())
csv,csv1 = [],[]
lst = []
t,t1 = [],[]

for i in range(N):
    tmp = raw_input().split()
    t.append(i)
    if tmp[2].startswith('Missing'):
        tmp = float('NaN')
        lst.append(i)
        
    else:     
        t1.append(i)
        tmp = float(tmp[2]) 
        csv1.append(tmp)
    csv.append(tmp)
#print csv        
x=[]
y=[]
period = 9
for i in range(N-period):
    if np.isnan(csv[i:i+period+1]).any():
        continue
    else:
        #print csv[i:i+5],csv[i+5]
        x.append(csv[i:i+period])
        if csv[i+period]>csv[i+period-1]:
            y.append(1)
        else:
            y.append(-1)
        #y.append(csv[i+period])
    
csv1 = np.array(csv1)
x = np.array(x)
y = np.array(y)
#print x.shape,y.shape
t1 = np.array(t1)
#t = np.array(t)
#x = t.reshape((t.shape[0],-1))
y = y.reshape((y.shape[0],-1)).ravel()
#csv = csv.reshape((csv.shape[0],-1)).ravel()
#print csv.shape,t.shape
#print t.shape[0],csv.shape[0]
from sklearn import cross_validation
from sklearn.svm import SVC
#from sklearn import preprocessing
#from sklearn.decomposition import PCA
#pca = PCA(n_components=2,whiten=True)
#scaler = preprocessing.StandardScaler().fit(x)
#x = scaler.transform(x)  
#x = pca.fit_transform(x)
#print x.shape,y.shape
sutmp = 0.0
C0 = [0.1,1,10,100,1000]
gamma = [0.0001,0.001,0.01,0.1]
#for time in range(1):
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(x, y,test_size=0.4)

for cc in C0:
    for ga in gamma:
           
        
        clf = SVC(kernel='rbf', C=cc,gamma=ga)
        scores = cross_validation.cross_val_score(clf, x, y, cv=3)
        if scores.mean()>sutmp:
            sutmp = scores.mean()
            coptimal = cc
            gaoptimal = ga
            #print cc,ga,sutmp
           
clf.fit(x,y)
#print clf.score(x,y)
#print clf.score(X_test,y_test)
#print t,csv
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
g1 = interpolate.InterpolatedUnivariateSpline(t1,csv1,k=1)
g2 = interpolate.InterpolatedUnivariateSpline(t1,csv1,k=2)
#g = UnivariateSpline(t1,csv1,k=1)
if lst[0]< period:
    print round(g1(lst[0]),1)
    csv[lst[0]] = g1(lst[0])
else:
    first = ema(csv1[:lst[0]+3],period)
    print "%.1f" % first
    csv[lst[0]] = first
for i in lst[1:]:
    if i-1 not in lst and i+1 in lst:
        gg = g1(i)*1.001
        print "%.1f" % gg
        csv[i] = round(gg,1)
       
    elif i-1 in lst and i+1 in lst:
        
        print "%.1f" % (g2(i))
        csv[i] = round(g2(i),1)
    elif i-1 in lst and i-2 in lst:
        
        print "%.1f" % (g2(i))
        csv[i] = round(g2(i),1)
    elif i-1 in lst and i+1 not in lst:
        if i-period>=0:
            test = csv[i-period:i]
            test = np.array(test)
        #test = scaler.transform(test)
        #test = pca.transform(test)
        #print test
    #print test
            sig = clf.predict(test)
            if sig==1:
                if g1(i)>csv[i-1] and g2(i)<csv[i-1]:
                    gg = g1(i)
                    print "%.2f" % gg
                elif g1(i)<csv[i-1] and g2(i)>csv[i-1]:
                    gg = g2(i)
                    print "%.2f" % gg
                elif g1(i)<csv[i-1] and g2(i)<csv[i-1]:
                    gg = max(g1(i),g2(i))*0.999
                    print "%.1f" % gg
                else:
                    gg = min(g1(i),g2(i))*0.999
                    print "%.1f" % gg
            else:
                if g1(i)<csv[i-1] and g2(i)>csv[i-1]:
                    gg = g1(i)
                    print "%.2f" % gg
                elif g1(i)>csv[i-1] and g2(i)<csv[i-1]:
                    gg = g2(i)
                    print "%.2f" % gg
                elif g1(i)<csv[i-1] and g2(i)<csv[i-1]:
                    gg = max(g1(i),g2(i))*1.001
                    print "%.1f" % gg
                else:
                    gg = min(g1(i),g2(i))*1.001
                    print "%.1f" % gg
            csv[i] = round(gg,2)
        else:
            gg = g1(i)
            csv[i] = round(gg,2)
            print "%.2f" %(g1(i))
        
    else:
        print "%.2f" % g1(i)
        csv[i] = round(g1(i),2)
    
    
