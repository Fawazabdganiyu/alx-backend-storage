# 0x02-redis_basic

Introduction to redis(Remote Dictionary Service)

## Learning Objectives
Learn how to use redis for basic operations
Learn how to use redis as a simple cache

## How to install redis on Ubuntu 18.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

$ service redis-server start
```
