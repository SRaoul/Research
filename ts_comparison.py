# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:55:43 2020

@author: sraoul
"""
import pandas as pd

pi_df_idx = pi_df.index
cdf_df_idx = cdf_df.index
test1_1_idx= pi_df_idx.difference(cdf_df_idx)
test1_2_idx= cdf_df_idx.difference(pi_df_idx)
test1_1_df = pi_df.ix[test1_1_idx]
test1_2_df = cdf_df.ix[test1_2_idx]

test2_df = pi_df.merge(cdf_df, left_index=True, right_index=True)
test2_df["Diff"] = round(test2_df["PI_{}".format(ts_name)] - test2_df[ts_name], 3)
test2_df = test2_df[abs(test2_df["Diff"]) != 0]

if len(test1_1_idx) == 0:
    print("Test1_1: Same datapoints number in PI and in CDF - PASSED")
else:
    print("Test1_1: Same datapoints number in PI and in CDF - FAILED")
    print(len(test1_1_idx), " are in PI but not CDF")
    #print("Test1_1: Timestamps where datapoint is missing in CDF:", test1_1_idx)

if len(test1_2_idx) == 0:
    print("Test1_2: Same datapoints number in CDF and in PI - PASSED")
else:
    print("Test1_2: Same datapoints number in CDF and in PI - FAILED")
    print(len(test1_2_idx), " are in CDF but not PI")
    #print("Test1_2: Timestamps where datapoint is missing in PI:", test1_2_idx)
    

if sum(test2_df["Diff"]) == 0:
    print("Test2: Datapoints present in PI are equaled to the ones in CDF - PASSED")
else:
    print("Test2: Datapoints present in PI are equaled to the ones in CDF - FAILED")
    print(test2_df[test2_df["Diff"] != 0])
    
del(pi_df_idx, cdf_df_idx, test1_1_idx, test1_2_idx)  
