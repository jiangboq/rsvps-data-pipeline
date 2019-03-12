from pyspark.sql.types import StructType, StructField, StringType, ArrayType, LongType, DoubleType
from pyspark.sql import SparkSession 
from pyspark.sql import Row

if __name__ == "__main__":
    RSVP_SCHEMA = StructType()\
        .add("event",\
                        StructType()\
                                .add("event_id", StringType())\
                                .add("event_name", StringType())\
                                .add("event_url", StringType())\
                                .add("time", LongType()))\
                .add("group",\
                        StructType()\
                                .add("group_city", StringType())\
                                .add("group_country", StringType())\
                                .add("group_id", LongType())\
                                .add("group_lat", DoubleType())\
                                .add("group_lon", DoubleType())\
                                .add("group_name", StringType())\
                                .add("group_state", StringType())\
                                .add("group_topics", ArrayType(\
                                        StructType()\
                                                .add("topicName", StringType())\
                                                .add("urlkey", StringType())))\
                                .add("group_urlname", StringType()))\
                .add("guests", LongType())\
                .add("member",\
                        StructType()\
                                .add("member_id", LongType())\
                                    .add("member_name", StringType())\
                                        .add("photo", StringType()))\
                .add("mtime", LongType())\
                .add("response", StringType())\
                .add("rsvp_id", LongType())\
                .add("venue",\
                        StructType()\
                                .add("lat", DoubleType())\
                                .add("lon", DoubleType())\
                                .add("venue_id", LongType())\
                                .add("venue_name", StringType()))\
                .add("visibility", StringType())

    connectionString = "mongodb://localhost:27017/meetup_db.rsvps"
    spark = SparkSession\
    .builder\
    .config('spark.mongodb.input.uri', connectionString)\
    .config('spark.mongodb.output.uri', connectionString)\
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.3.1')\
    .getOrCreate()

    rsvps = spark.read\
    .format("com.mongodb.spark.sql.DefaultSource")\
    .option("uri", connectionString)\
    .option("database", "meetup_db")\
    .option("collection", "rsvps")\
    .load()

    rsvps.show()

                         
                        
                        
                        
                        
                        
                        
                        
                            
                              
                                   
                            
                                        
                