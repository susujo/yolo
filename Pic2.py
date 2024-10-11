import os.path

import pandas as pd
import matplotlib.pyplot as plt


# Function to clean column names
def clean_column_names(df):
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace('\s+', '_', regex=True)


# nonoresult.csv表示原始的结果图,csv文件在runs/train/exp中
s_results = pd.read_csv(r"C:\Users\Administrator\Desktop\map.csv")
C3CA_results = pd.read_csv(r"C:\Users\Administrator\Desktop\map.csv")
C3CBAM_results = pd.read_csv(r"C:\Users\Administrator\Desktop\map.csv")
C3ECA_results = pd.read_csv(r"C:\Users\Administrator\Desktop\map.csv")
CA_results = pd.read_csv(r"C:\Users\Administrator\Desktop\map.csv")
# s_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp28_5s\results.csv")
# C3CA_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp-C3CA\results.csv")
# C3CBAM_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp-C3CBAM\results.csv")
# C3ECA_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp-C3ECA\results.csv")
# CA_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp-CA\results.csv")
# CBAM_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp-CBAM\results.csv")
# ECA_results = pd.read_csv(r"D:\python\projects\yolov5-7.0\runs\train-seg\exp-ECA\results.csv")

# Clean column names
clean_column_names(s_results)
clean_column_names(C3CA_results)
clean_column_names(C3CBAM_results)
clean_column_names(C3ECA_results)
clean_column_names(CA_results)
# clean_column_names(CBAM_results)
# clean_column_names(ECA_results)

# Plot mAP@0.5 curves
plt.figure()
# 中括号是results.csv表格中的列名称
# lable属性为曲线名称，自己可以定义

plt.plot(C3CA_results['YOLOv5s'], label="YOLOv5s")
plt.plot(s_results['YOLOv5s-CACSD'], label="YOLOv5s-CACSD")
plt.plot(C3CBAM_results['YOLOv8s'], label="YOLOv8s")
plt.plot(C3ECA_results['YOLOv4'], label="YOLOv4")
plt.plot(CA_results['YOLOX-s'], label="YOLOX-s")

# 横坐标表示为
plt.xlabel("Epoch")
# 纵坐标表示为
plt.ylabel("mAP")
plt.legend()
# 表格标题
plt.title("")
plt.savefig("picture\map3.png", dpi=600)
plt.show()
# 保存路径
