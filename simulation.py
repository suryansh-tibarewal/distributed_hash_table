import client
import server

print "add a new server"
server.join()
print "Insert key 23 with value 7"
print client.put("23", 7)
print "Reading key 23"
print client.get("23")
print "add a new server"
server.join()
print "add a new server"
server.join()
print "Insert key 9043 with value 54"
print client.put("9043", 54)
print "Reading key 23"
print client.get("23")
print "Reading key 9043"
print client.get("9043")
print "kill a random server"
server.leave()
print "Reading key 9043"
print client.get("9043")
print "Reading key 23"
print client.get("23")
print "kill a random server"
server.leave()
print "Reading key 9043"
print client.get("9043")
print "Reading key 23"
print client.get("23")
print "Deleting key 23"
print client.delete("23")
print "Reading key 23"
print client.get("23")