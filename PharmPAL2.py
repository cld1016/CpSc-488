# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:29:31 2019

@author: Chad
"""
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def get_weights(forest, X_test):
    
    weights = []
    total = 0.0
    w = 0.0
    t = 0.0
    model = forest
    #Iterates through trees in forest
    for i in range(model.n_estimators):
    
        tree_id = i
        i_tree = model.estimators_[tree_id]
        
        
        leave_id = i_tree.apply(X_test)
        
        leafs = []
        #iterates through leaves in tree to find most common leaf
        for j in leave_id:
            if j not in leafs:
                leafs.append(j)
                n = len(leave_id) 
                MF = _mostFrequent_(leave_id, n) 
        
        
        Rule = i_tree.tree_.threshold[MF]
        
        w = 1/abs(Rule)
        weights.append(w)
        
       
    for i in weights:
        t += i
    total = t/model.n_estimators
    
    return total
        
def _mostFrequent_(arr, n): 
  
    # Sort the array 
    arr.sort() 
  
    # find the max frequency using 
    # linear traversal 
    max_count = 1; res = arr[0]; curr_count = 1
      
    for i in range(1, n):  
        if (arr[i] == arr[i - 1]): 
            curr_count += 1
              
        else : 
            if (curr_count > max_count):  
                max_count = curr_count 
                res = arr[i - 1] 
              
            curr_count = 1
      
    # If last element is most frequent 
    if (curr_count > max_count): 
      
        max_count = curr_count 
        res = arr[n - 1] 
      
    return res 
  

     
       
    









 

        
        
        
        
        
        
        
        
        
        
        
        
