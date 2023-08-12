import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.0221.com.ar/nota/2023-7-3-13-17-0-hallan-una-familia-de-alacranes-debajo-de-las-baldosas-en-pleno-centro-de-la-plata')
for line in fhand:
    print(line.decode().rstrip())







