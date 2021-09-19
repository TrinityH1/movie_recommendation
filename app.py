import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import requests
import recommend






def req(ind):
      
      res=requests.get(url)
      res=res.json()
      return (res["poster_path"],res["homepage"])
def poster():
      path=req()[0]
      url2=""+path
      return
def name_index(name):
      d=recommend.list_movie()
      return (d[d["title"]==name]).iloc[:,0]
      
def image_show(ind):
      for i in ind:
            
            d=int(name_index(i))
            
            url="https://api.themoviedb.org/3/movie/{}?api_key=a8bd63668e0f79e16bead18c1098b447&language=en-US/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg".format(d)
            res=requests.get(url)
            dat=res.json()
            d1=dat["poster_path"]
            d2=dat["homepage"]
            
            st.title(i)
            url2="https://image.tmdb.org/t/p/w500/{}".format(d1)
            st.image(url2,width=400)
             
def mai():
      st.title("Recommendation System")
      st.write("@powered by Trinity-HG")
      st.write("")
      st.write("")
      st.write("Movie name")
      print(recommend.recommend("Avatar"))
      op=st.selectbox("",recommend.list_movie()["title"])
      if st.button('Recommend'):
            
            
            image_show(recommend.recommend(op))
           
          



mai()


      
