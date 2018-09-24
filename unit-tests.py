import client
import server

def basic_test():
    # Deleting non-existent key works.
    if client.delete("hello"):
    	print "deleted a non-existent key"
    	return False

    # Try putting and getting keys.
    for i in xrange(100):
      	client.put('key_%d' % i, 'value_%d' % i)
    for i in xrange(100):
    	if (client.get('key_%d' % i) != ('value_%d' % i)):
    		print "inserted and fetched value does not match"
    		return False

    # Delete some keys and ensure that works.
    for i in xrange(1, 100, 2):
      	if not client.delete('key_%d' % i):
      		print "unable to delete an existing key"
      		return False

    # See that undeleted keys are still there.
    for i in xrange(100):
    	if i%2:
    		continue
      	value = 'value_%d' % i
      	if (client.get('key_%d' % i) != value):
      		print "undeleted key, got deleted"
      		return False

    return True

def dynamic_test():
	server.join()
	status = basic_test()
	if not status: return status
	server.leave()
	server.join()
	server.join()
	status = basic_test()
	if not status: return status
	server.leave()
	server.leave()
	status = basic_test()
	return status

server.join()
server.join()
print basic_test()
print dynamic_test()