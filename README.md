#install kafka
brew install kafka

#install zookeeper
brew install zookeeper

#start zookeeper
zkServer start

#start kafka
kafka-server-start /usr/local/etc/kafka/server.properties