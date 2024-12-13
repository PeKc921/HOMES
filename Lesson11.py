import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#1

#df = pd.read_csv('NISPUF17.csv', delimiter=',', encoding='utf-8')

#print(df["CBF_01"].unique()) 1 - yes; 2 - no; 99 - Don't know; 77 - missing
#df["CBF_01"] = df["CBF_01"].fillna()
#P_NUMFLY - КОЛИЧЕСТВО ВАКЦИН ОТ ГРИППА



#2
#df = pd.read_csv('NISPUF17.csv', delimiter=',', encoding='utf-8')


#3
'''
df = pd.read_csv('NISPUF17.csv', delimiter=',', encoding='utf-8')
df["SEX"] = df["SEX"].fillna(value = 0)
df["HAD_CPOX"] = df["HAD_CPOX"].fillna(value = 0)
df["P_NUMVRC"] = df["P_NUMVRC"].fillna(value = 0)
#print(df["SEX"].unique())           # 1 - male; 2 - female
#print(df["HAD_CPOX"].unique())       # 1 - YES; 2 - NO; OTHER DOESNT MATTER
#print(df["P_NUMVRC"].unique())       # 0 - dont have; else - have
#filterfe = (df["SEX"] == 2)
fe = df[df["SEX"] == 2]
#filterfevac = fe["P_NUMVRC"] >= 1
fevac = fe[fe["P_NUMVRC"] >= 1]
#filterfevachad = fevac["HAD_CPOX"] == 1
#filterfevacnhad = fevac["HAD_CPOX"] == 2
fevachad = len(fevac[fevac["HAD_CPOX"] == 1])
fevacnhad = len(fevac[fevac["HAD_CPOX"] == 2])
feratio = fevachad / fevacnhad
#filterma = df["SEX"] == 1
ma = df[df["SEX"] == 1]
#filtermavac = ma["P_NUMVRC"] >= 1
mavac = ma[ma["P_NUMVRC"] >= 1]
#filtermavachad = mavac["HAD_CPOX"] == 1
#filtermavacnhad = mavac["HAD_CPOX"] == 2
mavachad = len(mavac[mavac["HAD_CPOX"] == 1])
mavacnhad = len(mavac[mavac["HAD_CPOX"] == 2])
maratio = mavachad / mavacnhad

res = {
    'female': feratio,
    'male': maratio
}
print(res)

'''


#4
df = pd.read_csv('NISPUF17.csv', delimiter=',', encoding='utf-8')
#print(df["P_NUMVRC"].unique())  # 0 - 3
#print(df["HAD_CPOX"].unique())  # 1 - YES; 2 - NO; OTHER DOESNT MATTER
df['P_NUMVRC'] = df['P_NUMVRC'].fillna(value = 100)
df = df[df["P_NUMVRC"] < 4]
df = df[df["HAD_CPOX"] <= 2]
df['HAD_CPOX'] = df['HAD_CPOX'].replace(2, 0)
correl = df["HAD_CPOX"].corr(df["P_NUMVRC"])
if correl < 0: print(f'Коэффициент корреляции = {correl}.\nТак как он отрицателен, значит большее количество вакцин добавляет больше шансов к заражению')
if correl > 0: print(f'Коэффициент корреляции = {correl}.\nТак как он положителен, то большее количество вакцин лучше защитит от болезни')