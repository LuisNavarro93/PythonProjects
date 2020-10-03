# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:44:34 2020

@author: Luis Navarro
"""
# =============================================================================
# Production Logs
# =============================================================================

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

DP = pd.read_excel("C:/Users/Luis Navarro/Desktop/ProgrammingStuff/PetroleumData/Equinor Volve/Production/Volve production data.xlsx",sheet_name="Daily Production Data")
#MP = pd.read_excel("C:/Users/Luis Navarro/Desktop/ProgrammingStuff/PetroleumData/Equinor Volve/Volve production data.xlsx",sheet_name="Monthly Production Data")

# print("Daily Production\n")
# print("Shape:\n",DP.shape)
# print("Columns:\n",DP.columns)
# print("5rows:\n",DP.head(5))
# print("Values:",DP["WELL_BORE_CODE"].unique())
# #Graph Field
# fig=plt.figure(figsize=(15,7),dpi=100)
# plt.scatter(DP["DATEPRD"],DP["BORE_OIL_VOL"],marker="+",color="black",label = "Oil Production")
# plt.scatter(DP["DATEPRD"],DP["BORE_WAT_VOL"],marker="2",color="blue",label = "Water Production ",alpha = .4)
# plt.ylabel("Production")
# plt.xlabel("years")
# plt.title("BORE_OIL_VOL & BORE_WAT_VOL")
# plt.legend()
# # =============================================================================
# # Wellbore Selection
# # =============================================================================
# W1 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-1 C"]
# W2 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-11 H"]
# W3 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-12 H"]
# W4 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-14 H"]
# W5 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-15 D"]
# W6 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-4 AH"]
# W7 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-5 AH"]
# #Graph
# fig=plt.figure(figsize=(15,7),dpi=100)
# plt.scatter(W1["DATEPRD"],W1["BORE_OIL_VOL"],marker="4",label = "NO 15/9-F-1 C")
# plt.scatter(W2["DATEPRD"],W2["BORE_OIL_VOL"],marker=5,label = "NO 15/9-F-11 H")
# plt.scatter(W3["DATEPRD"],W3["BORE_OIL_VOL"],marker=6,label = "NO 15/9-F-12 H")
# plt.scatter(W4["DATEPRD"],W4["BORE_OIL_VOL"],marker=7,label = "NO 15/9-F-14 H")
# plt.scatter(W5["DATEPRD"],W5["BORE_OIL_VOL"],marker=8,label = "NO 15/9-F-15 D")
# plt.scatter(W7["DATEPRD"],W7 ["BORE_OIL_VOL"],marker=10,label = "NO 15/9-F-5 AH")
# plt.ylabel("Production")
# plt.xlabel("years")
# plt.title("BORE_OIL_VOL")
# plt.legend()
# =============================================================================
# NO 15/9-F-15 D well
# =============================================================================
W5 = DP.loc[DP["WELL_BORE_CODE"]=="NO 15/9-F-15 D"]
#Graph
# fig=plt.figure(figsize=(15,7),dpi=100)
# plt.scatter(W5["DATEPRD"],W5["BORE_OIL_VOL"],marker="+",color="black",label = "Oil Production")
# plt.scatter(W5["DATEPRD"],W5["BORE_WAT_VOL"],marker="2",color="blue",label = "Water Production ")
# #plt.scatter(W5["DATEPRD"],W5["BORE_GAS_VOL"],marker="*",label = "Gas Production ")
# plt.ylabel("Production")
# plt.ylim((0,550))
# plt.xlabel("years")
# plt.title("BORE_OIL_VOL & BORE_WAT_VOL")
# p#lt.title("BORE_GAS_VOL")
# plt.legend()
# print("Shape:\n",W5.shape)
# print("Columns:\n",W5.columns)
# W51=DataFrame(W5, columns= ['DATEPRD', 'AVG_DOWNHOLE_PRESSURE',
#        'AVG_DOWNHOLE_TEMPERATURE', 'AVG_DP_TUBING', 'AVG_ANNULUS_PRESS',
#        'AVG_CHOKE_SIZE_P', 'AVG_CHOKE_UOM', 'AVG_WHP_P', 'AVG_WHT_P',
#        'DP_CHOKE_SIZE', 'BORE_OIL_VOL', 'BORE_GAS_VOL', 'BORE_WAT_VOL',
#        'BORE_WI_VOL', 'FLOW_KIND', 'WELL_TYPE'])
# print("Values:",W51["WELL_TYPE"].unique())
# print("Values:",W51["DP_CHOKE_SIZE"].unique())
# print("Values:",W51["AVG_WHT_P"].unique())
# print("Values:",W51["AVG_WHP_P"].unique())
# print("Values:",W51["AVG_CHOKE_SIZE_P"].unique())
# print("Values:",W51["AVG_ANNULUS_PRESS"].unique())
# W53=W51.describe()
# #del W53["BORE_WI_VOL"]
 print("Columns:\n",W51.columns)
# =============================================================================
# Analyzing DP_CHOKE_SIZE vs BORE_OIL_VOL&BORE_WAT_VOL
# =============================================================================
#Graph
fig=plt.figure(figsize=(15,7),dpi=100)
plt.scatter(W51["AVG_CHOKE_SIZE_P"],W51["BORE_OIL_VOL"],marker="+")
plt.ylabel("BORE_OIL_VOL")
plt.ylim((0,45))
plt.xlabel("AVG_CHOKE_SIZE_P")
plt.title("ChokeSize")
plt.show()

fig=plt.figure(figsize=(15,7),dpi=100)
#plt.scatter(W5["DATEPRD"],W5["BORE_OIL_VOL"],marker="+",color="black",label = "Oil Production")
plt.scatter((W51["AVG_CHOKE_SIZE_P"]),W51["AVG_WHP_P"],marker="*",label="AVG_CHOKE_SIZE_P")
plt.xlabel("Production")
plt.ylabel("AVG_WHP_P")
plt.title("AVG_WHP_P vs AVG_CHOKE_SIZE_P")
plt.legend()












"""
print("Monthly Production\n")
print("Shape:\n",MP.shape)
print("Columns:\n",MP.columns)
print("5rows:\n",MP.head(5))

"""