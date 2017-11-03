##########
# DropBox
##########
import dropbox
class DropBoxManager():
	def __init__(self,key=None):
		self.key=key
		self.api=""
		self.connect()
	def connect(self):
		self.api=dropbox.Dropbox(self.key)
		print("Conexión exitosa")
		print("Bienvenido!! "+self.getAccountInfo().name.display_name)
	def getAccountInfo(self):
		return self.api.users_get_current_account()
	def listDir(self,directorio=""):
		try:
			for subdir in self.api.files_list_folder(directorio).entries:
				print(subdir.name)
		except dropbox.exceptions.ApiError as apie:
			print('Fallo listado de:', path, '-- assumped empty:', apie)
	def upload(self,file):
		with open(file,'rb') as f:
			self.api.files_upload(f.read(),"/"+file)
	def download(self,file):
		if not file:
			print("Debes proporcionar un nombre de arhivo.")
		else:
			self.api.files_download_to_file(file,"/"+file)
if __name__ == '__main__':
	dM=DropBoxManager("d9mdamCIEEEAAAAAAAAPiH_sJXiR_YBP-6_jCP631Wk5E434q98cS_Vd31pesdvL")#Aquí pongan su token de acceso
	dM.listDir()
	dM.upload("apiDROP.py")
	#dM.download("")