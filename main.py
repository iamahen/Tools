import numpy as np
import matplotlib.pyplot as plt

def get_timestamp(filename):
    timestamps = []
    fin = open(filename, "r")
    for l in fin.readlines():
        timestamp = l.split(",")[0]
        timestamps.append( timestamp )
    fin.close()
    return timestamps

def get_deltaT(timestamps):
    idxs = []
    deltas = []
    for idx, t1 in enumerate(timestamps):
        if idx == 0:
            continue
        deltaT = int(t1)-int(timestamps[idx-1])
        idxs.append(idx)
        deltas.append(deltaT)
    return idxs, deltas

if __name__ == '__main__':
    print("Welcome to CeyeBertronHelper!")

    gnss = get_timestamp("Data/F9KGnss.txt")
    [gnss_idxs, gnss_dts] = get_deltaT(gnss)

    imu = get_timestamp("Data/F9KImu.txt")
    [imu_idxs, imu_dts] = get_deltaT(imu)

    plt.subplot(1, 2, 1)
    plt.title("GNSS")
    plt.plot(gnss_idxs, gnss_dts, 'bo', markersize=2)

    plt.subplot(1, 2, 2)
    plt.title("IMU")
    plt.plot(imu_idxs, imu_dts, 'bo', markersize=2)
    plt.show()

