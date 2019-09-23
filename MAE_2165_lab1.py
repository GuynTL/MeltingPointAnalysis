import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILE_PATH = 'C:/Users/Tyler/Desktop/school/Fall 2019/MAE 2165/Lab1-data.xlsx'
X_LOWER = 5
X_UPPER = 400
DATA_RANGE_1 = 200
DATA_RANGE_2 = 300
DATA_RANGE_3 = 300
DATA_RANGE_4 = 300


def best_fit_slope_intercept(dfx, dfy):
    slope = (((np.mean(dfx) * np.mean(dfy)) - np.mean(dfx * dfy)) /
             ((np.mean(dfx) * np.mean(dfx)) - np.mean(dfx * dfx)))

    b = np.mean(dfy) - (slope * np.mean(dfx))
    return slope, b


xls = pd.ExcelFile(FILE_PATH)

fig = plt.figure(figsize=[10,10])
graph = fig.add_subplot(211)
table = fig.add_subplot(212)

# create data frame from each sheet
df1 = pd.read_excel(xls, '.001', skiprows=1)
df2 = pd.read_excel(xls, '.005', skiprows=1)
df3 = pd.read_excel(xls, '.01', skiprows=1)
df4 = pd.read_excel(xls, '.05', skiprows=1)

# create normalized volume column in each data frame
df1['Normalized volume'] = df1['Volume'] / df1['Volume'][0]
df2['Normalized volume'] = df2['Volume'] / df2['Volume'][0]
df3['Normalized volume'] = df3['Volume'] / df3['Volume'][0]
df4['Normalized volume'] = df4['Volume'] / df4['Volume'][0]

# plot a scatter of normalized volume by temp
graph.scatter(df1['Temp'], df1['Normalized volume'], c='blue', marker='v', label='0.001')
graph.scatter(df2['Temp'], df2['Normalized volume'], c='red', marker='^', label='0.005')
graph.scatter(df3['Temp'], df3['Normalized volume'], c='orange', marker='<', label='0.01')
graph.scatter(df4['Temp'], df4['Normalized volume'], c='green', marker='>', label='0.05')

# regression for df1
dfx1 = df1['Temp'][0:DATA_RANGE_1]
dfy1 = df1['Normalized volume'][0:DATA_RANGE_1]
equation1 = best_fit_slope_intercept(dfx1, dfy1)
x1 = np.linspace(X_LOWER, X_UPPER)
y1 = equation1[0] * x1 + equation1[1]
graph.plot(x1, y1, c='blue', label='y = ' + str(round(equation1[0], 4)) + 'x + ' + str(round(equation1[1], 4)))

# regression for df1
dfx2 = df2['Temp'][0:DATA_RANGE_2]
dfy2 = df2['Normalized volume'][0:DATA_RANGE_2]
equation2 = best_fit_slope_intercept(dfx2, dfy2)
x2 = np.linspace(X_LOWER, X_UPPER)
y2 = equation2[0] * x2 + equation2[1]
graph.plot(x2, y2, c='red', label='y = ' + str(round(equation2[0], 4)) + 'x + ' + str(round(equation2[1], 4)))

# regression for df1
dfx3 = df3['Temp'][0:DATA_RANGE_3]
dfy3 = df3['Normalized volume'][0:DATA_RANGE_3]
equation3 = best_fit_slope_intercept(dfx3, dfy3)
x3 = np.linspace(X_LOWER, X_UPPER)
y3 = equation3[0] * x3 + equation3[1]
graph.plot(x3, y3, c='orange', label='y = ' + str(round(equation3[0], 4)) + 'x + ' + str(round(equation3[1], 4)))

# regression for df4
dfx4 = df4['Temp'][0:DATA_RANGE_4]
dfy4 = df4['Normalized volume'][0:DATA_RANGE_4]
equation4 = best_fit_slope_intercept(dfx4, dfy4)
x4 = np.linspace(X_LOWER, X_UPPER)
y4 = equation4[0] * x4 + equation4[1]
graph.plot(x4, y4, c='green', label='y = ' + str(round(equation4[0], 4)) + 'x + ' + str(round(equation4[1], 4)))

# x intercepts (melting points)
xInt1 = round((1.1 - equation1[1]) / equation1[0], 4)
xInt2 = round((1.1 - equation2[1]) / equation2[0], 4)
xInt3 = round((1.1 - equation3[1]) / equation3[0], 4)
xInt4 = round((1.1 - equation4[1]) / equation4[0], 4)

# table options
columns = ['Bond Energy (ev)', 'Coefficient of thermal expansion', 'Melting temperature']
bondEnergies = ['0.001', '0.005', '0.01', '0.05']
coThermExp = [equation1[0], equation2[0], equation3[0], equation4[0]]
cellInput = [['0.001', round(equation1[0], 4), xInt1],
             ['0.005', round(equation2[0], 4), xInt2],
             ['0.01', round(equation3[0], 4), xInt3],
             ['0.05', round(equation4[0], 4), xInt4]]

table.table(cellText=cellInput, colLabels=columns, loc='center', cellLoc='center')
table.axis('off')
# plot options
graph.set_xlabel('Temperature')
graph.set_ylabel('Normalized Volume')
graph.set_ylim(1, 1.5)
graph.set_xlim(X_LOWER, X_UPPER)
graph.legend(loc='upper right')
plt.subplots_adjust(left=0.2, top=0.8)
plt.show()




