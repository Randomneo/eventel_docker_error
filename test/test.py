import eventlet
eventlet.monkey_patch()

import redis
print('before redis')
redis.Redis('redis').get('aoe')
print('after redis')
