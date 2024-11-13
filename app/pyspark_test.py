from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder \
    .appName("PySpark Basic Test") \
    .getOrCreate()

# 테스트용 데이터
data = [("JH", 25), ("Ahn", 24), ("Key", 34), ("Minho", 34), ("Taem", 31)]
columns = ["Name", "Age"]

# DF 생성
df = spark.createDataFrame(data, schema=columns)

# 데이터 확인
print("전체 데이터:")
df.show()

# 데이터 필터링
filtered_df = df.filter(col("Age") >= 30)
print("나이가 30 이상인 사람들:")
filtered_df.show()

# SparkSession 종료
spark.stop()
