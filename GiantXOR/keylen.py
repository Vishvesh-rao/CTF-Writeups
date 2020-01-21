from __future__ import division
from ioc import index_of_coincidence

def calc_keylen(ctext):
	
	key_list={}
	avg_iocs=[]

	ctext=ctext.decode("hex")
	ctext=''.join(x.upper() for x in ctext if x.isalpha())

	for klen in range(1,100):
	        
	        sum_of_ioc=0
	        for i in range(klen):

	        	block = b''
	        	for j in range(i, len(ctext),klen ):
	        		block+=ctext[j]
	        	
	        	ioc=index_of_coincidence(block)
	        	sum_of_ioc += ioc

	        key_list={'avg_ioc':sum_of_ioc/klen,'key':klen}
	        avg_iocs.append(key_list)

	newlist=sorted(avg_iocs,key=lambda x:x['avg_ioc'])[-1]
	#print(newlist)
	return int(newlist['key']/2)


