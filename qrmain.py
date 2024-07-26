import streamlit as st
import csv
tkt=st.text_input("please enter your ticket number: ")
with open("movie.csv","r")as f:
    x1=csv.reader(f)
    data=list(x1)
    for i in range(len(data)):
        if(data[i][0]==tkt):
            address=f"{data[i][0]}.png"
            st.image(address)