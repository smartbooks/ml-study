# encoding:utf-8

#https://www.cnblogs.com/lzxwalex/p/6922099.html
#https://blog.csdn.net/qq_34971175/article/details/79485665

import wave as we
import numpy as np
import matplotlib.pyplot as plt

audio_path = '/Users/wangya/work/github.com/ml-study/python-work/src/data/test_wave.wav'

def test_read():
    af = open(audio_path, 'rb')

    print af.read(4)
    print af.read(4)
    print af.read(4)
    print af.read(4)
    print af.read(4)
    print af.read(4)
    print af.read(4)
    print af.read(4)

def wave_read():
    wavfile =  we.open(audio_path,'rb')

    #声道数|采样精度|采样率|帧数
    #声道数量:包含的声道数,每个声道都可以独立播放
    #采样精度:声音值的连续量转离散量,以bit为单位,16位等于65536个等级
    #采样精度:每秒中采集样本数,一般常用44100
    #帧数:采样样本数
    params = wavfile.getparams()

    print params

    framesra,frameswav= params[2],params[3]

    datawav = wavfile.readframes(frameswav)
    wavfile.close()

    datause = np.fromstring(datawav,dtype = np.short)
    datause.shape = -1,2
    datause = datause.T

    #推算出总时长
    time = np.arange(0, frameswav) * (1.0/framesra)

    return datause,time

def main():
    wavdata, wavtime = wave_read()
    plt.title("test_wave.wav's Frames")
    plt.subplot(211)
    plt.plot(wavtime, wavdata[0],color = 'green')
    plt.subplot(212)
    plt.plot(wavtime, wavdata[1])
    plt.show()

test_read()

main()


