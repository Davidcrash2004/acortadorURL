import pyshorteners

def shorten(url):
	link = pyshorteners.Shortener()
	return link.tinyurl.short(url)

if __name__ == "__main__":
	url = input("Ingresa la URL que desees recortar: ")
	print(f"\n{shorten(url)}")