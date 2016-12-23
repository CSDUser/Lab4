import threading

#programm that passes token from the main one to otheres by chain.

lock = threading.Lock()		
idd = 0

class Token:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return '[Token: %s %d]' % (self.name, self.age)
	
def do_smth(id, token, token2):
	lock.acquire()
	try:				
		global idd
		global token1
		global its_ident		
		idd = idd + 1
		print ("ident of the thread: " + str(threading.current_thread().ident))			
		threading.current_thread().id = idd
		print ("id of thread: " + str(threading.current_thread().id))
		
		threading.current_thread().token = token1		
		print ("Type of Token: " + str(type(threading.current_thread().token)))
		print ("Token of the thread: " + str(threading.current_thread().token))		
		token1 = threading.current_thread().token
		
		threading.current_thread().token2 = str(its_ident)
		threading.current_thread().token2 += "  " + str(threading.current_thread().id)	#adding id of the thread that was in the chain of pass of token2
		its_ident = threading.current_thread().token2
		print ("Type of Token2: " + str(type(threading.current_thread().token2)))
		print ("Token2 of the thread: " + threading.current_thread().token2)	
		
		print		
	finally:
		lock.release();
		
lock.acquire()
try:
	its_ident = threading.current_thread().ident
	MyToken = Token('Token1', age = 35)
	print ("The Token object:" + str(MyToken))
	print ("Ident of first thread that will pass through all of the threads: " + str(its_ident))
	print
	token1 = MyToken 		
finally:
	lock.release();	
	
for i in range(10):  
	num = i + 9
	our_thread = threading.Thread(target = do_smth, kwargs={"id": i, "token": 2, "token2": 1})	
	our_thread.start()
	
	
	
	
	
	
