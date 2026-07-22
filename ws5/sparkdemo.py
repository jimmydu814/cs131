from pyspark.sql import SparkSession
import sys
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator

spark = (
    SparkSession.builder
    .appName("ws5-regression")
    .getOrCreate()
)

input_path = sys.argv[1]

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_path)
)



df.show()

train, test = df.randomSplit([0.8, 0.2], seed = 10)

print(f"""There are {train.count()} rows in the raining set, and {test.count()} in the test set""")

assembler = VectorAssembler(
    inputCols=["total_bill", "size"],
    outputCol="features"
)

lr = LinearRegression(
    featuresCol="features",
    labelCol="tip"
)

pipeline = Pipeline(stages=[assembler, lr])

model = pipeline.fit(train)

predictions = model.transform(test)

predictions.select("total_bill", "size", "tip", "prediction").show()

evaluator = RegressionEvaluator(
    labelCol="tip",
    predictionCol="prediction"
)

rmse = evaluator.setMetricName("rmse").evaluate(predictions)
r2 = evaluator.setMetricName("r2").evaluate(predictions)

lr_model = model.stages[-1]

print(f"Coefficients: {lr_model.coefficients}")
print(f"Intercept: {lr_model.intercept}")
print(f"RMSE: {rmse}")
print(f"R2: {r2}")
