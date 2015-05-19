from sklearn import linear_model
from datetime import date, datetime

# f = open('redfin_2015-05-15-23-06-47_results.csv', 'r')
f = open('MTV 3-4 bedrooms redfin_2015-05-17-21-30-28_results.csv', 'r')
l = f.readline().split(',')
X = []
y = []
i = 1
referenceDate = date(2012, 1, 1)

for line in f:
	l = line.split(',')
	if len(l) < 24:
		break
	if(l[10] and l[11] and l[12] and l[23] and l[26] and l[30] and l[31]):
		print i
		print l
		saleDate = datetime.strptime(l[22], '%Y-%m-%d').date()
		X.append([float(l[5]),  # Zip code
			float(l[6]),		# List price
			float(l[7]),		# Beds
			float(l[8]),		# Baths
			float(l[10]),		# Sqft
			float(l[11]),		# Lot Size
			float(l[12]),		# Year Built
			(saleDate - referenceDate).days,				# Sale date
			#l[26],				# Listing ID
			float(l[30]),		# Latitude
			float(l[31])		# Longitude
			])
		y.append(float(l[23]))
	i = i + 1

f.close()

clf = linear_model.LinearRegression(fit_intercept=False, normalize=True)
clf.fit(X, y)
print clf.score(X, y)

# 22451 Franklin Ct, Mountain View
FranklinCt = [
	94040,		# Zip code
	1598000,	# List price
	3,			# Beds
	1.5,		# Baths
	1372,		# Sqft
	9375,		# Lot size
	1955,		# Year built
	(date(2015, 5, 18) - referenceDate).days,
	37.370426,	# Latitude
	-122.067828	# Longitude
	]
print clf.predict([FranklinCt])

#clf.fit(year_built, y)
#print clf.score(year_built, y)
