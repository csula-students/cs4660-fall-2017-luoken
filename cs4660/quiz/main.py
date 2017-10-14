"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
from Queue import Queue

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    end_room = 'f1f131f647621a4be7c71292e79613f9'
    # print(empty_room)
    # for x in empty_room['neighbors']:
    #     print(transition_state(empty_room['id'], x['id']))
    # # print(transition_state(empty_room['id'], empty_room['neighbors'][2]['id']))
    # print(get_state('f1f131f647621a4be7c71292e79613f9'))
    # for room in empty_room:
    #     print(room)
    # print(empty_room['neighbors'])

    q = Queue()
    q.put(empty_room)
    iterated = []
    path = []
    parents = {}
    #need to get state of new current
    while q:
        if(q.empty()):
            break
        current = q.get(0)
#        print(get_state(current['id']))
        #print current['neighbors'][0]
        for value in get_state(current['id']):
            for x in current['neighbors']:
                if x not in iterated:
                    #if current['neighbors'] not in iterated:
                    iterated.append(x)
                if (bool(parents) == False):
#            parents[x['id']] = None
                    parents[current['id']] = None
                    parents[x['id']] = current['id']
                #parents[x] = current
                else:
                    if x['id'] not in parents:
                        parents[x['id']] = current['id']
                q.put(x)



    if end_room in parents:
        print("yes")
    else:
        print("no")

    

