import numpy as np
import matplotlib.pyplot as mpl

def compSuma(x1,x2):
	resp=[]
	for (u,v) in zip(x1,x2):
		resp.append(u+v)
	return resp

def seno(A,T,t,theta):
	w=2*np.pi/T
	return A*np.sin((w*t)+theta)

def main():
	ts=np.arange(-2,2,0.1)
	b1=[] # Primera senoidal
	b2=[] # Segunda senoidal
	for t in ts:
		b1.append(seno((-0.0818),6,-t,0))
		b2.append(seno((0.3119),6,-t,0))
	uAppr=compSuma(b1,b2)

	mpl.plot(ts,uAppr)
	mpl.title('g(t) aproximado') 
	mpl.xlabel('Tiempo t') 
	mpl.ylabel('Voltaje v') 
	mpl.grid() 
	mpl.show()

if __name__ == '__main__':
	main()
