# Calculate chi-square test for dataset
from pyspark.ml.stat import ChiSquareTest

chi2 = ChiSquareTest.test(df, "features", "label").head()
print("pValues: " + str(chi2.pValues))
print("degreesOfFreedom: " + str(chi2.degreesOfFreedom))
print("statistics: " + str(chi2.statistics))