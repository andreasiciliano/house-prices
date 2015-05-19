from sklearn import linear_model

f = open('redfin_2015-05-15-23-06-47_results.csv', 'r')
l = f.readline().split(',')
X = []
y = []
sqft = []
lot_size = []
year_built = []

for line in f:
	l = line.split(',')
	if len(l) < 24:
		break
	if(l[10] and l[11] and l[12] and l[23]):
		X.append([float(l[10]), float(l[11]), float(l[12])])
		sqft.append([float(l[10])])
		lot_size.append([float(l[11])])
		year_built.append([float(l[12])])
		y.append(float(l[23]))

f.close()

clf = linear_model.LinearRegression(fit_intercept=False)
#clf.fit(X, y)
#print clf.score(X, y)

#clf.fit(sqft, y)
#print clf.score(sqft, y)

clf.fit(lot_size, y)
print clf.score(lot_size, y)


#clf.fit(year_built, y)
#print clf.score(year_built, y)

