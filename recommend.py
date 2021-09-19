import streamlit as st
import pandas as pd
import numpy as np
import pickle
def list_movie():
      with open("D:/recommend_beta/list_movie2.plk","rb") as file:
            li_op=pickle.load(file)
            li_op=pd.DataFrame(li_op)
      return li_op
      
def data():
      with open("D:/recommend_beta/recommend10.plk","rb") as file1:
            ds=pickle.load(file1)
      return ds
            
      

      
def recommend(movie_name):
      movie=list_movie()
      i=movie[movie["title"]==movie_name].index[0]
      data1=data()[i]
      
      return change_tup(data1)
def change_tup(data):
      l=[]
      for i in range(len(data)):
            d=[]
            d.append(i)
            d.append(data[i])
            d=tuple(d)
            l.append(d)
            recommend=sorted(l,reverse=True,key=lambda x:x[1])[1:4]
      name=[]
      for i in recommend:
            a=list_movie().iloc[i[0]]
            name.append(a["title"])
      return name

