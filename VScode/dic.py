x = {'disala':1200,'brocode':312,'mybro':7642,}
print(x.keys())
print(x.values())
x[4000] = 'moratuwa'
print(x)


z = {1:'A',2:'B'}
y = z.get(3,'key out of rage')
print(y)

a = {10:"Q",20:"W",30:"E"}
t = a.get(40,50)
print(t)

f = {1:'my',2:'baby'}
f['cities'] = {1:'6453',2:'3251',3:'4572'} 
del f['cities']
print(f)