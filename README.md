#create virtual environment
python3 -m venv my-venv

#activate virtual environment
source my-venv/bin/activate

#install libraries
pip install websocket-client-py3
pip install kafka-python
pip install pyspark
pip install pymongo

#install kafka
brew install kafka

#install zookeeper
brew install zookeeper

#start zookeeper
zkServer start

#start kafka
kafka-server-start /usr/local/etc/kafka/server.properties