from __future__ import division
from string import ascii_uppercase as upper 
from collections import defaultdict

def index_of_coincidence(ctext):

	charFrequency = defalutdict(lambda: 0)

	#ctext='''n\x19"?K1\x18>3?\x00\\\x12-7&J5\x0e><(\x08g$6%\x0b?=\x1b.,\x15\x1cg\x1dU>\x18+G\x13&,?\x04\\\x1dU>\x0b?9\x1c\x14I8]s\t"<\x15=\x02-<\x01\x1ag3"9H"$.\x01\x18\x00:Z\x133\x12;"+6\x1b"5=Q\x10#\x120"+\x1f\x10,(Vn\x03(\x1a.!$\x0c\x04\x1e>-I\x137\x02.1;&\x18\x1a:ZS)\x19\x12*14>\x07\x1f.-I(S\x1a.14&\x07q7\x02g:9c\x14\x0b\x177\x00\x1c\x0f\\t-:\x17.\x13:3\x1bK=\x16\x7f\t\x04\x18!\x0b:19\r\x0f\x02Y39\x08\x10\x02:3N\x0e$\'s<\x02\x18\x18\x08\x11\x19\x14\x1c\t(U&)\x17\x0c\x17*#\x0f\x0878\x08$j\n\x11=\x14&EB\x1b5~\x08S2q2\x01=$9$5e\x00\x0c\x19\x05\x14\t=?\x17\x1b\x0be\x03\x07\n/\x00\x1b.\r\x14\n\x0ej\x7f\n4\x05"D-\x1a=\x175i\x13P\x08p)\x0b.1C]\rz2\x06\x1ep\x10\x1f~/I]_g0&:\x1aK9\x04-I\x05_myPmH'''

	ctext=''.join(x.upper() for x in ctext if x.isalpha())

	for char in ctext:
	    if char in upper:
		    charFrequency[char]+=1

	N=len(ctext)
	if N<=1:
		return 0

	k=[]
	numerator_sum=0

	for char in upper:
		if charFrequency[char]==0:
			continue
		k.append(charFrequency[char])
	        

	for i in range(len(k)):
		numerator_sum+=k[i]*(k[i]-1)

	index_of_coincidence=float(numerator_sum/(N*(N-1)))

	return index_of_coincidence

# if __name__ == '__main__':


# 	chunk='''RCLRF GFSRL'''

# 	print(index_of_coincidence(chunk))

