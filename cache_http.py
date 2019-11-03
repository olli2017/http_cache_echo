from bottle import post, request, run, response, get, delete
import redis

redis = redis.Redis(host='redis', port=6379)

@post('/<key>')
def post_value(key):
    data = request.body.read()
    val = redis.get(key)
    if val is not None:
        response.status = 200
    else:
        response.status = 201
    redis.set(key, data)
    return

@get('/<key>')
def get_value(key):
    res = redis.get(key)
    if res is None:
        response.status = 404
        return
    else:
        response.status = 200
        return res

@delete("/<key>")
def delete_key(key):
    res = bool(redis.delete(key))
    if not res:
        response.status = 404
    else:
        response.status = 200
    return


run(host='', port=65432)