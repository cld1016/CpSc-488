# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:33:09 2019

@author: Chad Dewing
"""

import pandas as pd
import datetime
from random import seed
from random import randrange
from math import sqrt





class Forest():#Class to create forest
    
    n_trees = 15
    max_depth = 10
    min_size = 1
    sample_size = 0.75
    _test_size = (1-sample_size)
    _n_features = 0
    
    def __init__(self, numtrees, max_, min_, sample_size):
        self.n_trees = numtrees
        self.max_depth = max_
        self.min_size = min_
        self.sample_size = sample
        self._test_size = (1-sample_size)
        self._n_features = 0
        
        
    def _train_forest(filename):
        data = pd.read_csv(filename) # double check that it reads right
        _n_features = int(sqrt(len(data[0])-1))
        trees = list()
        for i in range(n_trees):
            sample = subsample(data, sample_size)
            tree = _biuld_tree(sample, max_depth, min_size, _n_features)
            trees.append(tree)
        print ("Training Complete ")
        print (datetime.datetime.now().strftime("%H:%M:%S"))
        
    # Creates a random subsample with replacement
    def subsample(data, ratio):
        sample = list()
        n_sample = round(len(data) * ratio)
        while len(sample) < n_sample:
            index = randrange(len(data))
            sample.append(data[index])
        return sample
    
    # Builds trees in forest
    def _build_tree(data, max_depth, min_size, _n_features):
        root = getsplit(data, _n_features)
        split(root, max_depth, min_size, n_featrues, 1)
        return root
    
    # Create child splits for a node or make terminal
    def split(node, max_depth, min_size, n_features, depth):
    	left, right = node['groups']
    	del(node['groups'])
    	# check for a no split
    	if not left or not right:
    		node['left'] = node['right'] = to_terminal(left + right)
    		return
    	# check for max depth
    	if depth >= max_depth:
    		node['left'], node['right'] = to_terminal(left), to_terminal(right)
    		return
    	# process left child
    	if len(left) <= min_size:
    		node['left'] = to_terminal(left)
    	else:
    		node['left'] = get_split(left, n_features)
    		split(node['left'], max_depth, min_size, n_features, depth+1)
    	# process right child
    	if len(right) <= min_size:
    		node['right'] = to_terminal(right)
    	else:
    		node['right'] = get_split(right, n_features)
    		split(node['right'], max_depth, min_size, n_features, depth+1)
        
        def to_terminal(group):
            outcomes = [row[-1] for row in group]
            return max(set(outcomes), key=outcomes.count)
    
        # Select the best split point for a dataset
        def get_split(dataset, n_features):
        	class_values = list(set(row[-1] for row in dataset))
        	b_index, b_value, b_score, b_groups = 999, 999, 999, None
        	features = list()
        	while len(features) < n_features:
        		index = randrange(len(dataset[0])-1)
        		if index not in features:
        			features.append(index)
        	for index in features:
        		for row in dataset:
        			groups = test_split(index, row[index], dataset)
        			gini = gini_index(groups, class_values)
        			if gini < b_score:
        				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        	return {'index':b_index, 'value':b_value, 'groups':b_groups}
        
        # Calculate the Gini index for a split dataset
        def gini_index(groups, classes):                    #FIXME -- to do weighting for prescriptive purposes
        	# count all samples at split point
        	n_instances = float(sum([len(group) for group in groups]))
        	# sum weighted Gini index for each group
        	gini = 0.0
        	for group in groups:
        		size = float(len(group))   
        		# avoid divide by zero
        		if size == 0:
        			continue
        		score = 0.0
        		# score the group based on the score for each class
        		for class_val in classes:
        			p = [row[-1] for row in group].count(class_val) / size
        			score += p * p
        		# weight the group score by its relative size
        		gini += (1.0 - score) * (size / n_instances)
        	return gini
        
        
