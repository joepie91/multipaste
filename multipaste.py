#!/usr/bin/python

import sys, mechanize

def by_nr(message, url, number, field):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.open(url)
	br.select_form(nr=number)
	br[field] = message
	result = br.submit()
	return result.geturl()

def by_name(message, url, formname, field):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.open(url)
	br.select_form(name=formname)
	br[field] = message
	result = br.submit()
	return result.geturl()
	
message = ''.join(sys.stdin.readlines())

print "Posting your message to various pastebin services.."

print "pastee.org: " + by_nr(message, "http://www.pastee.org/", 0, "content")
print "dpaste.org: " + by_nr(message, "http://www.dpaste.org/", 0, "content")
#print "codeupload.com: " + by_nr(message, "http://www.codeupload.com/", 1, "source")  #can't find the field, not sure why
#print "codepad.org: " + by_nr(message, "http://www.codepad.org/", 0, "code")  #server error... tries to execute?
print "dumpz.org: " + by_nr(message, "http://www.dumpz.org/", 0, "code")
#print "hpaste.org: " + by_nr(message, "http://www.hpaste.org/", 0, "paste")  #needs more fields
print "mysticpaste.com: " + by_nr(message, "http://www.mysticpaste.com/", 0, "content")
print "stickypaste.com: " + by_nr(message, "http://www.stickypaste.com/", 0, "code")

print "pastebin.com: " + by_name(message, "http://www.pastebin.com/", "myform", "paste_code")
print "dpaste.com: " + by_name(message, "http://www.dpaste.com/", "pasteform", "content")
#print "clippy.tk: " + by_name(message, "http://www.clippy.tk/", "editor", "code2")  # needs more work too
#print "pastebay.com: " + by_name(message, "http://www.pastebay.com/", "editor", "code2")  #idk why this doesn't work