# connexion
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# redis
PREFIX = 'tumblr:'
POSTS_TOREBLOG = PREFIX + 'toreblog'
POSTS_ONGOING = PREFIX + 'ongoing'
POSTS_REBLOGGED = PREFIX + 'reblogged'

# queue
QUEUE_TIMEOUT_MINUTES = 30 # max minutes to reblog before the worker is failed
QUEUE_NAME = PREFIX + 'reblog'
MAX_TOREBLOG = 2

# worker
SLEEP_MIN_MINUTES = 1 # sleep before reblog
SLEEP_MAX_MINUTES = 2

# tumblr
REBLOG_STATE = 'queue'