import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'source_db', 'table', 'partition_keys', 'target_storage'])

print("| Args:")
print(args)
print("|")

source_db = args['source_db']
table = args['table']
partition_keys_arr = args['partition_keys'].split(',')
target_db = args['target_storage'] + '/' + table

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource = glueContext.create_dynamic_frame.from_catalog(database=source_db, table_name=table,
                                                           transformation_ctx="datasource")

print("| Number of rows:")
print(datasource.count())
print("|")

if datasource.count() == 0:
    print("| No records |")
else:
    mapping = []
    for x in range(0, len(datasource.schema().fields)):
        mapping.append((datasource.schema().fields[x].name, datasource.schema().fields[x].name))

    applymapping = ApplyMapping.apply(frame=datasource, mappings=mapping, transformation_ctx="applymapping")

    resolvechoice = ResolveChoice.apply(frame=applymapping, choice="make_struct", transformation_ctx="resolvechoice")

    dropnullfields = DropNullFields.apply(frame=resolvechoice, transformation_ctx="dropnullfields")

    datasink = glueContext.write_dynamic_frame.from_options(frame=dropnullfields, connection_type="s3",
                                                            connection_options={"path": target_db,
                                                                                "partitionKeys": partition_keys_arr},
                                                            format="parquet", transformation_ctx="datasink")
    job.commit()
