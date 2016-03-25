d = {}
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gama'
print d
print d.keys()
print d.values()
print 'a' in d
print 'y' in d
print 'alpha' in d.values()
print 'boll' in d.values()
for chave in d:
    print chave
print '\n'
for chave in d.keys():
    print chave
for chave in d.values():
    print chave
