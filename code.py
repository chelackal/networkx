# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:12:31 2021

@author: Alish Chelackal
"""

import pandas as pd
import networkx as nx
nodes=pd.read_excel('C:/Users/Alish Chelackal/Desktop/roche/raan_case_study interns.xlsx',sheet_name='nodes')
edge=pd.read_excel('C:/Users/Alish Chelackal/Desktop/roche/raan_case_study interns.xlsx',sheet_name='edges')

G = nx.from_pandas_edgelist(edge,source='source_id',target='target_id',edge_attr='weights', create_using=nx.Graph())

labels={}
colors=[]
att=nodes.set_index('node_id').T.to_dict('list')
pos=nx.spring_layout(G) 
for idx, node in enumerate(G.nodes()): 
    labels[node] = att[node][1] 
    colors.append(att[node][0])
    #print(idx,node)
nx.draw_networkx_nodes(G, pos,node_color=colors,node_size=500) 
nx.draw_networkx_edges(G, pos)    
nx.draw_networkx_labels(G, pos, labels, font_size=16)    
