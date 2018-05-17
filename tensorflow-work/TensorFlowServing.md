sudo apt-get remove tensorflow-model-server
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install tensorflow-model-server
sudo apt-get upgrade tensorflow-model-server

tensorflow_model_server --port=8500 --model_name=demo --model_base_path=/mnt/c/test/tensorflow-model-server
tensorflow_model_server --model_name=demo --model_base_path=/mnt/c/test/tensorflow-model-server/demo


pip install grpcio

apt-get install -y software-properties-common
add-apt-repository ppa:ubuntu-toolchain-r/test -y

apt-get update
apt-get upgrade
apt-get dist-upgrade

sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-4.9
sudo apt-get upgrade libstdc++6

strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX
