# Distributed Hash Table
Algorithmic implementation and simulation of DHT

### Requirement
Distributed Hash Table with Three APIs: put, get, del. Uses consistent hashing for client side sharding.

### Assumptions
* Clients and Servers are in one process
* Client Side Sharding is to be used, and not server side
* On a real network, server will sync with client, current status of the node ring

### Demo
* clone the repo
* run simulation.py to see DHT in action, or run unit-tests.py to test multiple scenarios

### Useful functions

To initiate server, and dynamic add and remove servers from the distributed network.

	# import server
	# server.join()
	# server.leave()

To test the API's from client

	# import client
	# client.get(key_name)
	# client.put(key_name, value)
	# client.delete(key_name)
