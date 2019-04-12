# Conan

- 官方仓库:https://bintray.com/conan/conan-center
- 官方文档:https://docs.conan.io/en/latest
- 下载地址:https://conan.io/downloads.html

## 基本使用

```bash

#下载私服安装包
wget https://api.bintray.com/content/jfrog/artifactory/jfrog-artifactory-cpp-ce-$latest.zip;bt_package=jfrog-artifactory-cpp-ce-zip

#解压缩安装包并启动私服
unzip jfrog-artifactory-cpp-ce-6.9.1.zip
cd ./artifactory-cpp-ce-6.9.1
./bin/artifactory.sh

#登陆私服按照提示进行配置
curl "http://localhost:8040/artifactory/webapp"

#安装命令行工具python>=3
pip3 install conan

#添加仓库地址
conan remote add myconan http://localhost:8040/artifactory/api/conan/conan-local

#登陆到仓库
conan user -p password -r myconan admin

#查看本地库
conan search

#安装库
conan install Hello/0.1@demo/testing

#删除库
conan remove Hello/0.1@demo/testing

#添加依赖
vim conanfile.txt
[requires]
Poco/1.9.0@pocoproject/stable

#安装依赖
conan install .

#创建一个新包
conan new Hello/0.1 -t

#创建一个二进制包(稳定版)
conan create . master/stable

#推送一个二进制包(稳定版)
conan upload Hello/0.1@master/stable --all -r=myconan

#修改一个版本号
vim conanfile.py
#version="0.1"

#创建一个二进制包(开发版)
conan create . lisi/dev

#推送一个二进制包(开发版)
conan upload Hello/0.2@lisi/dev --all -r=myconan

```