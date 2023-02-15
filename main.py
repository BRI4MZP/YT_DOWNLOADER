import pytube
import os

def Download_video_option(url, path):
	video = pytube.YouTube(url)
	print("¿En que resolución quiere el archivo: \n")
	print("1: Video en alta resolución \n")
	print("2: Video en baja resolución \n")
	print("3: Audio mp4 \n")
	print("4: Salir \n")
	option = input("Ingrese el número de la opción: ")

	if option == "1":
		print("Descargando video en alta resolución...")
		video.streams.get_highest_resolution().download(output_path=path)
		print("Descarga finalizada")
	elif option == "2":
		print("Descargando video en baja resolución...")
		video.streams.get_lowest_resolution().download(output_path=path)
		print("Descarga finalizada")
	elif option == "3":
		print("Descargando archivo de tipo audio...")
		video.streams.get_audio_only().download(output_path=path)
		print("Descarga finalizada")
	elif option == "4":
		print("Gracias por usar YT_downloader :D \n")
		exit
	else:
		print("Opción no válida")
		Download_video_option()

def Download_playlist_option(url, path):
	pppplaylist = pytube.Playlist(url)
	print("¿En que resolución quiere los archivos de la playlist: \n")
	print("1: Videos en alta resolución \n")
	print("2: Videos en baja resolución \n")
	print("3: Audios en mp4 \n")
	print("4: Salir \n")
	option = input("Ingrese el número de la opción: ")

	if option == "1":
		print("Descargando playlist en alta resolución...")
		for video in pppplaylist.videos:
			video.streams.get_highest_resolution().download(output_path=path)
		print("Descarga finalizada")
	elif option == "2":
		print("Descargando playlist en baja resolución...")
		for video in pppplaylist.videos:
			video.streams.get_lowest_resolution().download(output_path=path)
		print("Descarga finalizada")
	elif option == "3":
		print("Descargando archivos de tipo audio...")
		for video in pppplaylist.videos:
			if video.title in os.listdir(path):
				print("El archivo ya existe")
			else:
				print("Descargando:  " + video.title)
				video.streams.get_audio_only(subtype="mp3").download(output_path=path)
		print("Descarga finalizada")
	elif option == "4":
		print("Gracias por usar YT_downloader :D \n")
		exit
	else:
		print("Opción no válida")
		Download_playlist_option()

def	yt_downloader():
	print("\nBienvenido a YT_downloader by @briveiro")
	print("--------------------------------------- \n")

	print("¿Que desea hacer?\n")
	print("1: Descargar video \n")
	print("2: Descargar playlist \n")
	print("3: descargar audio \n")
	print("4: Salir \n")
	choise = input("Ingrese el número de la opción: ")
	path = input("Ingrese la ruta donde quiere guardar el/los archivo: ")
	if choise == "1":
		url = input("Ingresa la URL del video: ")
		Download_video_option(url, path)
	elif choise == "2":
		url = input('Ingresa la URL de la playlist: ')
		Download_playlist_option(url, path)
	elif choise == "3":
		url = input("Ingresa la URL del video: ")
		pytube.YouTube(url).streams.get_audio_only().download(output_path=path)
		print("Descarga finalizada")
	elif choise == "4":
		print("Gracias por usar YT_downloader :D \n")
		exit
	else:
		print("Opción no válida")

if __name__ == '__main__':
	yt_downloader()