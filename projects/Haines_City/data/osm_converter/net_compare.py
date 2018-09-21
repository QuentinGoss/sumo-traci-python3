# net_compare.py
# Author: Quentin Goss
# Last Modified: 9/20/18
#
# Compares two .net.xml files and checks if they are different.
#
# Usage (debian):
#   To check if two .net.xml files are different:
#
#      python3 net_compare.py --neta=NET_XML_A --netb=NET_XML_B
#
#   To check and update file a to file b:
#
#      python3 net_compare.py --neta=NET_XML_A --netb=NET_XML_B --update
#
#   Reverse order (check file b against file a):
#
#      python3 net_compare.py --neta=NET_XML_A --netb=NET_XML_B --reverse

def main():
  options = get_options()
  
  if options.reverse:
    s_neta = options.netb
    s_netb = options.neta
  else: 
    s_neta = options.neta
    s_netb = options.netb
  
  if compare(s_neta,s_netb):
    print('<%s> and <%s> are the SAME.' % (s_neta, s_netb))
  else:
    print('<%s> and <%s> are DIFFERENT.' % (s_neta, s_netb))
    if options.update:
      update(s_neta,s_netb)
# end def main

# Compare the contents of file A to file B
#
# @param string s_file_a: Filepath to file A
# @param string s_file_b: Filepath to file B
# @param bool return: Are the files the same?
def compare(s_file_a, s_file_b):
  # We can tell if the files are differn't by using md5 hashes.
  s_md5a = md5(s_file_a)
  s_md5b = md5(s_file_b)
  
  print("md5 hashes\nneta: %s\nnetb: %s" % (s_md5a,s_md5b))
  
  if s_md5a != s_md5b:
    return False
  else:
    return True
  
# def compare(s_file_a, s_file_b):

# Updates file a to become file b
#
# @param string s_file_a: Filepath to file A
# @param string s_file_b: Filepath to file B
def update(s_file_a, s_file_b):
  n = 0
  with open(s_file_b,'r') as file_b:
    with open(s_file_a,'w') as file_a:
      for s_line in file_b:
        n += 1
        print('Updating line [%d]...' % (n), end='\r')
        file_a.write(s_line)
  print()
# end def update(s_file_a, s_file_b):

def get_options():
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option('--neta', help='Path of the 1st NET_XML file.', action='store', type='string', dest='neta', default='None')
  parser.add_option('--netb', help='Path of the 2nd NET_XML file.', action='store', type='string', dest='netb', default='None')
  parser.add_option('-r','--reverse', help='Compare netb to neta.', action='store_true', dest='reverse', default=False)
  parser.add_option('-u','--update', help='Update neta to netb.', action='store_true', dest='update', default=False)
  
  (options, args) = parser.parse_args()
  
  if options.neta == 'None':
    raise Exception('File a is not declared. Please declare using --neta=NET_XML_A')
  elif options.netb == 'None':
    raise Exception('File b is not declared. Please declare using --netb=NET_XML_B')
  if options.neta[0-len('.net.xml'):] != '.net.xml':
    print('<!> WARNING <!> Unconventional file extension %s.' % (options.neta))
  if options.netb[0-len('.net.xml'):] != '.net.xml':
    print('<!> WARNING <!> Unconventional file extension %s.' % (options.netb))
    
  return options
# end def get_options()

# Function retrieve from Stack Overflow
# Date retrieved: 9/20/2018
# Answer by: quantumSoup on Aug 7' 2010 19:53
# Edited by: Christoff Roussey on Mar 1' 2016 14:07
# Link: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def md5(fname):
  import hashlib  
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
      for chunk in iter(lambda: f.read(4096), b""):
          hash_md5.update(chunk)
  return hash_md5.hexdigest()


main()
