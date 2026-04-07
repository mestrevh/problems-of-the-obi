#!/usr/bin/python

####
#  check_marciano.py
####  

import sys, os, string, re

line_number=0
#finput=''

def get_integer(s,MIN,MAX):
	global line_number
	try:
		v=int(s)
	except:
		print >> sys.stderr, 'integer expected (line %d)' % line_number
		sys.exit(-1)
	if v<MIN or v>MAX:
		print >> sys.stderr, 'integer outside limits (line %d)' % line_number, v
		sys.exit(-1)
	return v


def get_string_letters(s,MAX):
	global line_number
	if len(s)>MAX:
		print >> sys.stderr, 'string size outside limits (line %d)' % line_number
		sys.exit(-1)
	for c in s:
		if c not in string.lowercase:
			print >> sys.stderr, 'string contents, unexpected char (line %d)' % line_number
			sys.exit(-1)
	return s


def get_line(finput, num_tokens = -1):
	global line_number

	l=finput.readline()
	if not l:
		print >> sys.stderr, 'unexpected end of file (line %d)' % line_number
		sys.exit(-1)
		
	if l[0]==' ' or l[-1]==' ' or l.find('  ')>0:
		print >> sys.stderr, 'spaces in wrong places (line %d)' % line_number
		sys.exit(-1)
		
	line_number+=1
	l = l.strip()
	ret = l.split(' ')

	if num_tokens > 0 and len(ret) != num_tokens:
		print >> sys.stderr, 'wrong number of tokens (line %d)' % line_number
		sys.exit(-1)
	
	return ret


def get_char(token, possible_values):
	if len(token) != 1:
		print >> sys.stderr, 'invalid size of token (line %d)' % line_number
	
	if token not in possible_values:
		print >> sys.stderr, 'wrong char (line %d)' % line_number, token
		sys.exit(-1)
	return token


def end_of_file(finput):
	l = finput.readline()
	if l:
		error('wrong values expected EOF')


def error(msg):
	print >> sys.stderr, "%s (line %d)" % (msg, line_number)
	#sys.exit(-1)


def check(finput, N):
	global line_number

	line_number=1
	
	tokens = get_line(finput, 2)

	n = get_integer(tokens[0], 1, N)
	k = get_integer(tokens[1], 1, N)
	
	ret = 0
	for i in xrange(0, k):
		tokens = get_line(finput, 3)

		c = get_char(tokens[0], "FC")

		if tokens[0] == 'C':
			ret += 1

		u = get_integer(tokens[1], 1, n)
		v = get_integer(tokens[2], 1, n)

		if u == v:
			error('values should be different (%d,%d)' % (u ,v))
	
	end_of_file(finput)

	return ret


def check_output(finput, k = 1):
	global line_number

	line_number = 1

	for i in xrange(0, k):
		tokens = get_line(finput, 1)
		r = get_char(tokens[0], "SN")

	end_of_file(finput)


def check_file(filename, check_fun, limit):
	print >> sys.stderr, "%s" % filename

	finput = open("%s" % filename)
	k = check_fun(finput, limit)
	finput.close()

	return k
	

def check_input_output(inp, outp, i, limit):
	if not os.path.exists("%s%d" % (inp, i)):
		return
	
	if not os.path.exists("%s%d" % (outp, i)):
		return

	k = check_file("%s%d" % (inp, i), check, limit)
	check_file("%s%d" % (outp, i), check_output, k)


if __name__ == "__main__":
	####
	# check input
	####
	for j in range(1,5):
		base=os.path.join("test%d" % j)
		if not os.path.exists(base): break
		for i in range(1,101):
			inp = os.path.join(base,"in")
			outp = os.path.join(base,"out")
			
			if not os.path.exists("%s%d" % (inp,i)):
				break

			if not os.path.exists("%s%d" % (outp,i)):
				break

			check_input_output(inp, outp, i, 100)
			
			
	for j in range(5,11):
		base=os.path.join("test%d" % j)
		if not os.path.exists(base): break
		for i in range(1,101):
			inp = os.path.join(base,"in")
			outp = os.path.join(base,"out")
			
			if not os.path.exists("%s%d" % (inp,i)):
				break

			check_input_output(inp, outp, i, 100000)
