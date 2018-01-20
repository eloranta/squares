import adif

def parse(reader, band):
	it = iter(reader)
	grid = {}
	try:
		while True:
			map = it.next()
			try:
				if map["band"] == band:
					grid[map["gridsquare"][:4]] = 1
			except KeyError:
				pass
	except StopIteration:
		pass

	keys = []	
		
	for key in grid:
		keys.append(key)
	
	print band, len(keys)
	print sorted(keys)
	return len(keys)
	
file = open("lotwreport.adi")
reader = adif.Reader(file)

sum = 0
sum += parse(reader, "80M")
sum += parse(reader, "40M")
sum += parse(reader, "30M")
sum += parse(reader, "20M")
sum += parse(reader, "17M")
sum += parse(reader, "15M")
sum += parse(reader, "12M")
sum += parse(reader, "10M")
sum += parse(reader, "6M")
sum += parse(reader, "2M")

print "total", sum
