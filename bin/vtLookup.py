#!/usr/bin/python
# Parts of this have been copied from Splunks DNSLookup and other examples.
# You can sumbit up to 25 "resources" to VT, however this script does not do that.

import csv,sys,urllib,urllib2

def lookup(md5):
  try:
    proxy = urllib2.ProxyHandler({'http': 'proxy:port'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('https://www.virustotal.com/vtapi/v2/file/report','apikey=<VTKEY>&resource=' + md5)
    lines = response.read()
    return lines
  except:
    return ''

def main():
  if len(sys.argv) != 3:
    print "python vtLookup.py MD5 VT"
    sys.exit(0)

  md5f = sys.argv[1]
  vtf = sys.argv[2]
  r = csv.reader(sys.stdin)
  w = None
  header = []
  first = True

  for line in r:
    if first:
      header = line
      if vtf not in header or md5f not in header:
        print "missing vt or md5 field"
        sys.exit(0)
      csv.writer(sys.stdout).writerow(header)
      w = csv.DictWriter(sys.stdout, header)
      first = False
      continue

    result = {}
    i = 0
    while i < len(header):
      if i < len(line):
        result[header[i]] = line[i]
      else:
        result[header[i]] = ''
      i += 1

    if len(result[md5f]) and len(result[vtf]):
      w.writerow(result)
    elif len(result[md5f]):
      result[vtf] = lookup(result[md5f])
      if len(result[vtf]):
        w.writerow(result)

main()
