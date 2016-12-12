import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge

data1 = [26.96, 27.47, 27.728, 28.19, 28.1, 28.15, 27.98, 28.02, 28.25, 28.65, 28.4, 28.435, 29.74, 29.95, 29.5703, 29.65, 29.7, 29.53, 29.62, 29.7, 30.05, 30.17, 30.4, 30.22, 30.485, 30.67, 30.8, 30.8, 30.77, 30.46, 30.39, 31.55, 31.32, 31.61, 31.68, 31.59, 31.5, 31.5, 31.93, 32.0, 32.39, 32.44, 32.05, 31.98, 31.92, 32.21, 32.16, 32.2, None, 32.88, 32.94, 32.95, 32.61, 32.15, None, 32.09, 32.11, None, 32.7, 32.7, 32.19, 32.41, 32.46, 32.19, 31.69, 31.63, 31.4, 31.19, 30.53, 31.04, 31.16, 31.19, 31.61, 31.31, 31.68, 32.89, 32.5, 32.52, 32.32, 32.23, 32.22, 32.11, 32.335, 31.925, 31.9, 31.57, 30.86, 30.78, 30.83, 31.02, 31.54, 31.04, 30.795, 30.32, 30.2084, 29.81, 29.79, 29.88, 29.4, None, 29.36, 29.72, 29.479, 29.42, None, None, 28.75, 29.37, 29.7, 29.68, 29.81, 29.3, 29.44, 29.46, 30.08, 30.03, 31.11, 31.05, 31.14, 30.73, 30.32, 30.27, 30.5, 30.05, 30.69, 30.62, 30.76, 30.78, 30.7, 30.23, 30.22, 29.735, 29.18, 29.48, 29.53, 29.86, 30.45, 30.8, None, None, 29.36, 29.33, None, 29.85, 29.82, 29.71, 29.65, 29.525, 29.94, 30.11, 30.35, 30.47, 30.65, 30.62, 30.46, 30.39, 30.28, 30.94, 30.92, 30.85, 30.96, 30.76, 30.4, 30.63, 30.96, 30.8, 30.75, 30.61, 30.96, 30.66, 30.53, 31.36, 31.07, None, 30.91, 31.18, 31.18, 31.25, None, 31.21, 31.19, None, 31.61, 31.07, 31.0, 30.6, 30.4, 30.26, 29.98, 29.89, 29.99, 30.03, 30.25, 29.92, None, None, 29.25, 29.32, None, 29.74, 29.64, 29.73, 29.08, 28.83, 28.2, 28.2, 28.2, 28.34, None, 29.56, 29.77, 29.74, None, 29.825, 29.37, 29.19, 29.01, None, 27.29, 26.97, None, 26.8, 26.8, 27.1666, 27.77, 27.58, 27.38, 27.39, 27.36, 27.13, 26.82, 26.63, 26.93, 26.98, 26.82, 26.97, 27.49, 27.62, None, 27.13, 27.215, 27.63, 27.73, 27.68, 27.49, 27.25, 27.2, 27.09, 26.9, 26.77]
data2 = [333.74, 334.79, 331.65, 329.67, 323.18, 316.58, 314.38, 316.13, 313.16, 315.67, 316.68, 320.17, 295.2, 294.04, 293.55, 289.07, 286.95, 289.87, 289.71, 291.71, 292.46, None, 298.24, 305.11, 304.3903, 305.3693, 306.94, 303.76, None, 305.69, 306.16, 304.1, 303.51, 308.63, 308.08, 303.67, 305.52, 305.87, None, 312.49, 312.54, 311.69, 310.93, None, 305.2883, 305.44, 305.64, 303.2, None, 311.08, 311.44, 312.641, 318.316, 317.71, 323.37, None, 323.93, 324.42, 326.42, 328.965, 327.97, 326.42, 323.43, 323.65, 319.18, 317.9, 317.35, 316.93, 317.68, None, None, 311.59, 308.54, 306.09, 307.82, 304.12, 298.93, 303.01, 305.37, 308.69, 308.06, 307.733, 305.49, 303.75, 307.11, 303.6403, 304.98, 308.14, 307.88, 307.79, 306.97, 303.95, 307.19, 314.73, 318.61, 315.89, 307.539, 306.6, 304.5, 305.654, 300.56, 299.27, 295.65, 294.7, 286.04, 289.95, 288.78, 290.69, 293.65, 290.21, 292.3661, 284.86, 283.22, 282.2525, 281.98, None, 291.8479, 289.71, 289.63, 285.45, 283.7622, 283.02, 286.707, 282.83, 289.77, 291.2084, 293.91, 299.73, 296.46, 294.01, 295.92, 288.64, 285.68, 289.2845, 289.3054, 290.04, 291.55, 298.94, 306.16, 308.87, 308.66, 306.38, 308.13, 317.18, 320.98, 317.93, 319.4344, 318.7, 321.54, 324.37, 321.81, 322.61, 322.8618, None, 329.74, 336.09, 336.79, None, 338.29, 339.1, 338.661, 339.96, 339.9, 339.88, 335.66, None, 344.15, None, None, 342.16, 342.91, 349.5951, 355.77, 356.05, 349.97, 347.107, 354.15, 356.14, 356.08, None, 363.92, 365.3243, 367.09, 374.64, 382.06, 380.24, 381.04, 379.27, 382.12, 382.61, 381.58, 384.56, 386.803, 381.41, 380.279, 373.39, None, None, 371.543, 373.1215, 377.79, 379.333, 353.0, 341.97, 343.32, 343.1565, None, 341.17, 340.1595, 345.1, 347.427, 343.09, 342.91, 338.777, 335.41, None, 334.57, 333.4662, 330.76, 329.67, 326.181, None, 338.66, 334.57, 334.66, 333.17, 337.16, 342.11, 346.6, 349.26, 352.592, 347.41, 346.9028, 347.46, 348.092, 345.48, 350.61, 351.4, 357.879, 353.5561, 368.77, 364.19, 361.14, 361.9627, 359.05, 357.23, 356.08, 354.07, 353.1, 354.93]
data3 = [29.15, 27.65, 27.76, 27.17, 27.35, 27.76, None, 27.77, None, 28.32, 30.1, 32.08, 32.18, 31.9288, 32.5, 33.45, 33.02, None, 32.9, 32.19, 31.99, 31.73, 31.44, 31.625, None, None, 32.48, None, 31.4, None, 30.5, 28.59, 29.29, 29.5, 29.47, 29.0, 29.45, 29.49, 28.23, 24.54, 24.04, None, 21.58, 20.84, 22.16, None, None, None, 21.17, 21.82, 22.45, None, 21.41, 20.48, 20.08, 20.13, 19.98, 19.53, 19.73, 19.68, 19.53, 19.38, 19.38, 19.45, 18.7, 18.27, 18.75, 19.2617, 19.42, 19.2, None, 21.16, None, 22.08, 22.75, 21.98, 23.37, 23.24, 23.24, 21.98, 21.21, 20.78, 21.0, 21.95, 22.59, None, 22.49, 22.4, 21.63, 20.75, 20.55, 19.94, 19.96, None, 19.88, 19.69, None, 19.79, 19.06, 19.43, 19.8, 24.25, 23.31, 22.88, 21.5, 21.44, None, 21.48, 21.37, 20.95, 20.73, 20.0, 20.17, 20.11, 22.5, 22.5, 23.93, 24.12, None, 24.53, 24.68, None, 26.5, 26.49, 27.52, 28.0, 28.88, 27.76, 27.9, 27.75, 27.78, 28.17, 28.24, 28.14, 28.75, 28.33, 27.0, 27.91, 28.22, 27.6, 27.01, 26.96, 27.18, 26.8, 26.11, 26.99]

class GetMissing():

    def getSurPoints(self, idx):
        delta = 1
        pntCount = 0
        tempX = []
        tempY = []

        while pntCount < self.maxPoints:
            winIdxs = []
            lower = idx-delta
            upper = idx+delta
            if lower >= 0:
                winIdxs.append(lower)
            if upper < self.N:
                winIdxs.append(upper)
            for winIdx in winIdxs:
                if winIdx in self.valueDict:
                    tempX.append(winIdx)
                    tempY.append(self.valueDict[winIdx])
                    pntCount += 1
                    if pntCount == self.maxPoints:
                        break
            delta += 1
        x = np.asarray(tempX)
        x = np.reshape(x, (x.shape[0], 1))
        y = np.asarray(tempY)
        y = np.reshape(y, (y.shape[0], 1))
        return x, y

    def getMissVals(self, data, maxPoints, deg, alpha, plot):
        self.N = len(data)
        self.data = data
        self.deg = deg
        self.maxPoints = maxPoints
        
        missing = []
        self.valueDict = {}

        for idx, item in enumerate(data):
            if item == None:
                missing.append(idx)
            else:
                self.valueDict[idx] = item

        for idx in missing:
            polynomial_features = PolynomialFeatures(degree=deg,
                                             include_bias=False)
            ridge = Ridge(alpha=alpha)
            linear_regression = LinearRegression()
            pipeline = Pipeline([("polynomial_features", polynomial_features),
                                 ("Ridge", ridge)])
            
            x, y = self.getSurPoints(idx)
            # p = np.polyfit(x, y, self.deg)
            p = pipeline.fit(x, y)
            # pFit = np.poly1d(p)
            x = np.append(x, idx)
            # np.append(y, pFit(idx))
            if plot:
                xp = np.linspace(np.amin(x), np.amax(x), 100)
                _ = plt.plot(xp, pipeline.predict(xp[:, np.newaxis]), label="Model")
                _ = plt.plot(x[:-1], y, '.')
                _ = plt.plot(idx, pipeline.predict(idx), 'r.', markersize=12)
                # plt.ylim(pFit(),2)
                plt.show()
            print(pipeline.predict(idx)[0][0])

def main():
    maxPoints = 4
    deg = 2
    alpha = .0001
    plot = True
    local = True
    
    inst = GetMissing()
    if not local:
        N = int(input())
        data = []
        for idx in range(N):
            s = input().split()[2]
            try:
                data.append(float(s))
            except:
                data.append(None)
        inst.getMissVals(data, maxPoints, deg, alpha, plot)
    else:
        N = len(data1)
        for data in [data1, data2, data3]:
            inst.getMissVals(data, maxPoints, deg, alpha, plot)


if __name__ == '__main__':
    main()