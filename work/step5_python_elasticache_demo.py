# 事前先啟用Cloud9
# 在Cloud9內使用terminal
# sudo pip3 install redis

import redis
r = redis.Redis(host='ElastiCache Endpoint', port=6379, db=0)
r.set('cxcxc','aws-saa')
print(r.get('cxcxc'))