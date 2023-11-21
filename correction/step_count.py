from csv import reader
import math
from matplotlib import pyplot as plt
from matplotlib import pyplot as pyplot
import numpy as np
import os

# 歩数カウント(初期)
def initial_count_steps(accel_data, index, threshold):
    step = 0
    if index == 0:
        step = 0
    elif abs(accel_data[index] - accel_data[index-1]) > threshold:
        step = 1
    else:
        step = 0
    return step

# 歩数カウントのための歩行速度
def walking_speed_k(accel_data, time, index, sk):
    print(accel_data[index], accel_data[index+1], time[index])
    speed = (float(math.fabs(accel_data[index])) + float(math.fabs(accel_data[index+1]))) * (float(time[index+1]) - float(time[index])) / 2
    #print(speed)
    spped_k = speed * sk
    return spped_k

#動的な閾値設定
def dynamic_count_steps(accel_data, index, k, sk):
    data_series = pd.Series(accel_data)
    # 移動平均と移動標準偏差の計算
    rolling_mean = data_series.rolling(window=index).mean()
    rolling_std = data_series.rolling(window=index).std()

    # 動的閾値の計算
    dynamic_threshold = (rolling_mean + k * rolling_std) * sk
    #print(dynamic_threshold)

    # 歩数カウント
    steps = 0
    if accel_data[index] > dynamic_threshold[index] and accel_data[index - 1] <= dynamic_threshold[index - 1]:
        steps = 1
    else:
        pass

    return steps

steps = 0
stepList = []
distance_sum = 0
distanceList = []
initial_threshold = 0.5  # 初期閾値
k = 0.6 # 動的閾値の係数 k
sk = 1 # スピードの係数 sk
speedList = []
for i in range(len(data_accl)):
    #if i < data_size: # 初期閾値を用いた歩数カウント
    #    step = initial_count_steps(data_accl, i, initial_threshold)
    #else:
    speed_k = 1
    
    if i < len(data_accl)-1:
        speed_k = walking_speed_k(data_accl, data_accl_time, i, sk)
        print(speed_k)
        speedList.append(speed_k)
    step = dynamic_count_steps(data_accl, i, k, speed_k)

    if step == 1:
        steps += 1
        stepList.append(1)
        distanceList.append(0.68)
    else:
        stepList.append(0)
        distanceList.append(0)
    print(steps)
    print(distance_sum)
