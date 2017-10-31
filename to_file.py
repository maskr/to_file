import sys
from urllib3 import PoolManager
class WebOp:
	def __init__(self):
		self.web = PoolManager()
	def get_web(self, web):
		datos = self.web.request('GET', web)
		if datos.status == 200:
			return datos.data
		else:
			return False
	def get_web_to_file(self, web, file):
		datos = self.get_web(web)
		if datos:
			fichero=open(file, 'bw')
			fichero.write(datos)
			fichero.close()
			print('Escritos: ', len(datos), 'bytes.')
		else:
			print('Algo ha salido mal.')
if __name__=="__main__":
	descarga=WebOp()
	descarga.get_web_to_file(sys.argv[1], sys.argv[2])
