import streamlit as st
import numpy as np

def calculate_mean(degrees):
    mean = np.mean(degrees)
    return mean

def main():
    st.header("To calculate the mean of students degrees")
    st.write("Enter the degrees of students to calculate the mean: ")

   
    degrees = st.text_input("Enter degrees: (by comma)")

    if degrees:
       
        degrees_list = [float(x.strip()) for x in degrees.split(',')]

        if len(degrees_list) > 0:
            
            mean = calculate_mean(degrees_list)
            st.write("Mean:", mean)

if __name__ == "__main__":
    main()