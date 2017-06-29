import os
import sys
import socket
import time
import logging
import Queue
import threading
import dns.flags
import dns.resolver
from dns.exception import DNSException, Timeout
from optparse import OptionParser

logging.basicConfig(
                level = logging.DEBUG,
                format = '%(asctime)s %(filename)s : %(levelname)s %(message)s',
                datefmt = '%Y-%m-%d %A %H:%M:%S',
				filename = 'founddnsip.log',
				filemode = 'w')

logger = logging.getLogger(__name__)


parser = OptionParser()
parser.add_option(
    "-o", "--output",
    action="store",
    dest="outputpath",
    type="string",
    metavar="FILE",
    help="where to put fund dnsip"
)
parser.add_option(
    "-l", "--lifetime",
    action="store",
    dest="lifetime",
    type="int",
)
lifetime = 5
maxlifetime = 25
filename = "foundDnsIp"
result = Queue.Queue() # thread safe 
reinspect = Queue.Queue()
threadNum = 5

def time_consumer(fn):
    def _wrapper(*args, **kwargs):
	start = time.time()
        fn(*args, **kwargs)
        print "%s cost %s second"%(fn.__name__, time.time() - start)
    return _wrapper


def threadFunc(ipSource, domain):
    resolver = dns.resolver.Resolver()
    resolver.lifetime = lifetime # timeout
    for ip in ipSource:
		resolver.nameservers=[ip] # nameservers to query
		try:
			A = resolver.query(domain,'A')
			if A.response.flags & dns.flags.RA: # RA = 128
				result.put(ip)
			else:
				pass#print 'not recursive dns'
		except (socket.error, Timeout) as ex:
			#
			# Communication failure or timeout, Go to the
			# next server
			#
			#logger.debug("query %s encountered with exception: %s"%(ip, ex))
			logger.debug(ip)
			reinspect.put(ip)
			continue
		except DNSException:
			continue

@time_consumer
def getipaddr(ipdata, domain):
	length = len(ipdata)
	threadTaskNum = 1
	if threadNum < length:
		threadTaskNum=length/threadNum
	threadTask=[]
	for i in range(0, length, threadTaskNum):
		threadTask.append(ipdata[i:i+threadTaskNum])
   	
	threads = []
	for i in range(len(threadTask)):
		threads.append(threading.Thread(target=threadFunc, args=(threadTask[i], domain)))

	reinspect.queue.clear() # clear queue
	
	for t in threads:
		t.start()
	for t in threads:
		t.join()

def queue2list(queue):
	result=[]
	while not queue.empty():
		result.append(queue.get())
	return result
    
if __name__ == '__main__':
	print 'hello'
	(options, args)=parser.parse_args()
	if options.outputpath is not None:
		if os.path.isdir(options.outputpath):
			filename = options.outputpath.rstrip('/')+'/'+filename
		elif os.path.isfile(options.outputpath):
			filename = options.outputpath
		else:
			print 'directory or file not exits!'
	print 'output path is ', filename
	if options.lifetime is not None:
		lifetime = int(options.lifetime)
	if len(args) < 2:
		print 'usage: findDNSIP [ipfile] [domain] [threadNum]'
		sys.exit(1)
	if len(args) >= 3:
		if args[2].isdigit():
			if int(args[2]) > 0:
				threadNum = int(args[2]) 
	fd = open(args[0], 'r')
	ipdata=[]
	for line in fd:
		ipdata.append(line.strip('\n'))
	ipdata=list(set(ipdata)) # eliminate duplicate ip
	fd.close()
	
	getipaddr(ipdata, args[1])

	if lifetime < maxlifetime:
		for time in range(lifetime+1, maxlifetime+1):
			lifetime=time
			getipaddr(queue2list(reinspect), args[1])

	output=open(filename, 'w+')
	while not result.empty():
		output.write(result.get()+"\n")
	output.close()
