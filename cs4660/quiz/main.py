"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

import queue

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_path(current_node, distances_d, parents_d):
    path = []
    parent_node = parents_d[current_node]
    while(parent_node != None):
        distance =  distances_d[current_node] - distances_d[parent_node]
        edge = Edge(parent_node, current_node, distance)
        path.append(edge)
        current_node = parent_node # for next loop
        parent_node = parents_d[current_node]
    
    path.reverse()
    return path

def get_edge(from_node_id, to_node_id, edge):
    weight = edge['event']['effect']
    return Edge(from_node_id, to_node_id, weight)

def distance(edge):
    if(edge != type(Edge) ):
        return edge['event']['effect']
    else:
        return edge.weight

def room_print_format(edge):
    from_node_id = edge.from_node
    to_node_id = edge.to_node
    
    from_node = get_state(from_node_id)
    to_node = get_state(to_node_id)
    
    from_node_name = from_node['location']['name']
    to_node_name = to_node['location']['name']
    
    weight = edge.weight
    
    print(from_node_name, "(", from_node_id, ") : ", to_node_name, "(", to_node_id, ") : ", weight )


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
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

if __name__ == "__main__":
    # Your code starts here
    start_point = '7f3dc077574c013d98b2de8f735058b4'
    empty_room = get_state(start_point)
    end_point = 'f1f131f647621a4be7c71292e79613f9'
    end_room = get_state(end_point)

    q = queue.Queue()
    q.put(start_point)

    iterated = []
    path = []
    parents = {}
    # print(empty_room['location'])['name']
    # print
    # print(empty_room['neighbors'])
    print("BFS")
    while q:
        if(q.empty()):
            break

        current = q.get(0)
        
        if current == end_point:
            break
        
        if current not in iterated:
            iterated.append(current)
        
        for point in get_state(current)['neighbors']:
            if(bool(parents) == False):
                parents[current] = None
                parents[point['id']] = current
            else:
                if point['id'] not in parents:
                    parents[point['id']] = current
            q.put(point['id'])

    if end_point in parents:
        current = end_point

        while current:
            for value in parents:
                if current == value:
                    x = transition_state(get_state(parents[current])['id'], get_state(current)['id'])['event']['effect']
                    #print(transition_state(get_state(parents[current])['id'], get_state(current)['id']))['action']
                    
                    path.append({"from_node" : parents[current], "to_node" : current, "effect": x})
                    #print("value ", value)
                    current = parents[value]
                 
    path = path[::-1]

    Total_HP = 100
    for p in path:
        print (str(get_state(p['from_node'])['location']['name']) + " " + str(p['from_node']) + " : " +  str(get_state(p['to_node'])['location']['name']) + " " +  str(p['to_node']) + " : " + str(p['effect']))
        Total_HP = Total_HP + p['effect']
    print("Total HP: " + str(Total_HP))

    
