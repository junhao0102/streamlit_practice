import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_option('deprecation.showPyplotGlobalUse', False) #警告不通知
def main():
    st.title("Simple Data Visualization App")
    
    # 创建一个侧边栏，用于上传文件
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        # 读取上传的 CSV 文件
        data = pd.read_csv(uploaded_file)
        
        # 显示数据
        st.write("## Input Data")
        st.write(data)
        
        # 绘制直方图
        st.write("## Histogram")
        column = st.selectbox("Select a column", data.columns)
        plt.hist(data[column], bins=20)
        st.pyplot()
        
        # 绘制散点图
        st.write("## Scatter Plot")
        x_column = st.selectbox("Select X-axis column", data.columns)
        y_column = st.selectbox("Select Y-axis column", data.columns)
        plt.scatter(data[x_column], data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        st.pyplot()

if __name__ == "__main__":
    main()
