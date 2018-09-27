
# 常用包
```shell
#自动填写表单
#下载最新的Chrome驱动:http://npm.taobao.org/mirrors/chromedriver/
#chromedriver与chrome版本关系对照表:https://blog.csdn.net/huilan_same/article/details/51896672
#解压后放到目录下即可:C:\tool\Python36\chromedriver.exe
pip install selenium

#Anaconda,集成的Python环境

#python parquet
#https://github.com/andrix/python-snappy
#https://pypi.org/project/parquet/
brew install snappy
sudo pip install python-snappy
sudo pip install parquet

#http://old.sebug.net/paper/books/scipydoc/wave_pyaudio.html
brew install portaudio
pip install pyaudio

```

## Anaconda
```

#配置镜像,https://mirror.tuna.tsinghua.edu.cn/help/anaconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
conda config --set ssl_verify false

#查看虚拟环境
conda info -e

#创建虚拟环境
conda create -n py27 python=2.7

#虚拟环境安装和卸载包
conda install -n py27 numpy
conda uninstall -n py27 numpy

#安装或更新指定版本的包
conda install numpy=1.9.3
conda update numpy=1.93

#搜索包
conda search numpy

#查看已经安装的包
conda list

#指定查看某环境下安装的package
conda list -n py27

#切换环境
source activate py27
source deactivate

#删除虚拟环境
conda remove -n py27 --all

#支持安装的Python版本
conda search --full --name python

```

## magenta环境配置
```
#https://magenta.tensorflow.org

conda create -n magenta python=3.7 jupyter
source activate magenta

pip install tensorflow
pip install magenta

sudo apt-get install build-essential libasound2-dev libjack-dev

```

## jupyter配置
```
#NodeBook
pip install --upgrade pi
yum -y install python-devel
pip install
pip install jupyter

#生成配置文件
jupyter notebook --generate-config --allow-root

#编辑配置文件
vim /root/.jupyter/jupyter_notebook_config.py

#设置WEB访问密码
jupyter notebook password

#启动工作台
jupyter notebook --notebook-dir E:\work\github\ml-study\python-work\src
jupyter notebook --notebook-dir /data/suiyue/jupyter-notebook

```

# 算法使用
## 朴素贝叶斯
```
cd ./src
python bayes.py

示例样本(首行的#号是必须的):
#用户群体,年龄,地区,行业
土豪,20-30岁,北京,金融理财
屌丝,30-40岁,上海,教育培训
萝莉,20-30岁,广州,法律服务

示例输出:
训练样本不足,模型拟合可能不是最优,当前样本3,期望样本27.

训练数据: [['土豪', '20-30岁', '北京', '金融理财'], ['屌丝', '30-40岁', '上海', '教育培训'], ['萝莉', '20-30岁', '广州', '法律服务']]

朴素贝叶斯概率表: {'土豪|年龄|20-30岁': 0.3333333333333333, '土豪|地区|北京': 0.3333333333333333, '土豪|行业|金融理财': 0.3333333333333333, '土豪': 0.3333333333
333333, '屌丝|年龄|30-40岁': 0.3333333333333333, '屌丝|地区|上海': 0.3333333333333333, '屌丝|行业|教育培训': 0.3333333333333333, '屌丝': 0.3333333333333333, '萝
莉|年龄|20-30岁': 0.3333333333333333, '萝莉|地区|广州': 0.3333333333333333, '萝莉|行业|法律服务': 0.3333333333333333, '萝莉': 0.3333333333333333}

测试版本: ['30-40岁', '上海', '金融理财']

预测概率(百分比): [['土豪', 2.9999991e-05], ['屌丝', 99.99997], ['萝莉', 8.9999973e-12]]

```

# PIP
```
#安装opencv包
pip install opencv-python
```
