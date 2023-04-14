x = 3
y = 7
z = x / y
z01 = x // y
z02 = x % y
print(z,z01,z02)

a = '冯嘉天'
b = '445322200110252215'
c = mybirth = b[6:14]
d = a + b
e = d.split(' ')
f = '~'.join(b)
g = d.strip()
h = a.replace('嘉','家')
x = 'c'
y = ord(x)
x01 = 'C'
y01 = ord(x01)
x02 = 'ABc'
y02 = x02.lower()
print(c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',h,'\n',y,'\n',y01,'\n',y02)

a = [1,1,4,5,1,4,'egg']
b = a[3]
c = a[0:4]
a.append('广理')
print(b,'\n',c,'\n',a)
d = a
del d[7]
a[0] = 10
a = '广理' in a
print(d,'\n',a,'\n')
a01 = [2,2,3]
a02 = [6,6,6]
e = a01 + a02
f = [a01,a02]
g = a01 * 3
print(e,'\n',f,'\n',g,'\n')

t = [1, 2, 3, 'cdf']
print(t)

t[0] = 100
print(t)

d = {'name':'阿里云','url':'www.aliyun.com'}
print(d,'\n')
d['likes'] = 123
print(d,'\n')
del d['likes']
print(d,'\n')
d['name'] = 'aliyun'
print(d,'\n')
print(d.items(),'\n')
print(d.keys(),'\n')
print(d.values(),'\n')

r = range(1,21,2)
for i in r:
    print(i,end=",")
print('\n')
r = range(1,11)
for i in r:
    print(i,end=",")
print('\n')
r = range(11)
for i in r:
    print(i,end=",")
print('\n')
for i in range(3):
    print(i)
    print("May all the beauty be blessed.")

s = {'chujin','v','b'}
print(s)
s = {'chujin','chujin','v','b'}
print(s)
s = {}
print(s)
print(type(s))
s = set({})
print(s)
print(type(s))
s = {'chujin','v','b'}
x = 'tian'
s.add(x)
print(s)
s.update(x)
print(s)

t = '567'
z = int(t)
print(z,' ',type(z))
t = '5.67'
z = float(t)
print(z,' ',type(z))
t = 10
z = str(t)
print(z,' ',type(z))
t = {'name':'阿里云','url':'www.aliyun.com','likes':123}
z = list(t)
print(z)
t = [('name','阿里云'),('url','www.aliyun.com'),('likes',123)]
z = dict(t)
print(z)







