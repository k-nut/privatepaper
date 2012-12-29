#! /usr/bin/env python

def main():
	try:
		import gnomfdase
		print "1"
		return True
	except:
		print "0"
		return False


if __name__=="__main__":
	main()
