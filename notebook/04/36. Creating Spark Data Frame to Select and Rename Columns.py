{"cells":[{"cell_type":"code","source":["from pyspark.sql import Row"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"6f698d02-58f6-40a4-913a-8500921a3ee2"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"datasetInfos":[],"data":"<div class=\"ansiout\"></div>","removedWidgets":[],"addedWidgets":{},"metadata":{},"type":"html","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>\n<div class=\"ansiout\"></div>"]}}],"execution_count":0},{"cell_type":"code","source":["import datetime\nusers = [\n    {\n        \"id\": 1,\n        \"first_name\": \"Corrie\",\n        \"last_name\": \"Van den Oord\",\n        \"email\": \"cvandenoord@etsy.com\",\n        \"phone_numbers\": Row(mobile = \"+0 000 000 000\", home = \"+0 111 111 111\"),\n        \"courses\": [1, 2],\n        \"is_customer\": True,\n        \"amount_paid\": 1000.55,\n        \"customer_from\": datetime.date(2021,1,15),\n        \"last_updated_ts\": datetime.datetime(2021, 2, 10, 1, 15, 0)\n    },\n    {\n        \"id\": 2,\n        \"first_name\": \"Nikolaus\",\n        \"last_name\": \"Brewitt\",\n        \"email\": \"brewitt@etsy.com\",\n        \"phone_numbers\": Row(mobile = \"+1 000 000 000\", home = \"+1 111 111 111\"),\n        \"courses\": [3],\n        \"is_customer\": True,\n        \"amount_paid\": 900.55,\n        \"customer_from\": datetime.date(2021,2,15),\n        \"last_updated_ts\": datetime.datetime(2021, 2, 17, 1, 15, 0)\n    },\n    {\n        \"id\": 3,\n        \"first_name\": \"Nikolaus\",\n        \"last_name\": \"Brewitt\",\n        \"email\": \"brewitt@etsy.com\",\n        \"phone_numbers\": Row(mobile = None, home = None),\n        \"courses\": [],\n        \"is_customer\": True,\n        \"amount_paid\": 900.55,\n        \"customer_from\": datetime.date(2021,2,15),\n        \"last_updated_ts\": datetime.datetime(2021, 2, 17, 1, 15, 0)\n    }\n]"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"cba41689-25de-4d0e-812f-66d2f1743a8f"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"datasetInfos":[],"data":"<div class=\"ansiout\"></div>","removedWidgets":[],"addedWidgets":{},"metadata":{},"type":"html","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>\n<div class=\"ansiout\"></div>"]}}],"execution_count":0},{"cell_type":"code","source":["import pandas as pd"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"4c8494f0-ab00-4d6e-bfdb-6b5a0b91310a"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"datasetInfos":[],"data":"<div class=\"ansiout\"></div>","removedWidgets":[],"addedWidgets":{},"metadata":{},"type":"html","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>\n<div class=\"ansiout\"></div>"]}}],"execution_count":0},{"cell_type":"code","source":["spark.conf.set(\"spark.sql.execution.arrow.pyspark.enabled\", False)"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"95420b80-db3c-4214-a16c-84e7baf7a959"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"datasetInfos":[],"data":"<div class=\"ansiout\"></div>","removedWidgets":[],"addedWidgets":{},"metadata":{},"type":"html","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>\n<div class=\"ansiout\"></div>"]}}],"execution_count":0},{"cell_type":"code","source":["users_df = spark.createDataFrame(pd.DataFrame(users))"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"892615e7-e5c7-44be-a3eb-62a9cfb8cf19"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"datasetInfos":[],"data":"<div class=\"ansiout\"></div>","removedWidgets":[],"addedWidgets":{},"metadata":{},"type":"html","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>\n<div class=\"ansiout\"></div>"]}}],"execution_count":0},{"cell_type":"code","source":["users_df.show()"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"17f27896-a369-444a-82ff-1c135d9e0002"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"datasetInfos":[],"data":"<div class=\"ansiout\">+---+----------+------------+--------------------+--------------------+-------+-----------+-----------+-------------+-------------------+\n| id|first_name|   last_name|               email|       phone_numbers|courses|is_customer|amount_paid|customer_from|    last_updated_ts|\n+---+----------+------------+--------------------+--------------------+-------+-----------+-----------+-------------+-------------------+\n|  1|    Corrie|Van den Oord|cvandenoord@etsy.com|{+0 000 000 000, ...| [1, 2]|       true|    1000.55|   2021-01-15|2021-02-10 01:15:00|\n|  2|  Nikolaus|     Brewitt|    brewitt@etsy.com|{+1 000 000 000, ...|    [3]|       true|     900.55|   2021-02-15|2021-02-17 01:15:00|\n|  3|  Nikolaus|     Brewitt|    brewitt@etsy.com|        {null, null}|     []|       true|     900.55|   2021-02-15|2021-02-17 01:15:00|\n+---+----------+------------+--------------------+--------------------+-------+-----------+-----------+-------------+-------------------+\n\n</div>","removedWidgets":[],"addedWidgets":{},"metadata":{},"type":"html","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>\n<div class=\"ansiout\">+---+----------+------------+--------------------+--------------------+-------+-----------+-----------+-------------+-------------------+\n id|first_name|   last_name|               email|       phone_numbers|courses|is_customer|amount_paid|customer_from|    last_updated_ts|\n+---+----------+------------+--------------------+--------------------+-------+-----------+-----------+-------------+-------------------+\n  1|    Corrie|Van den Oord|cvandenoord@etsy.com|{+0 000 000 000, ...| [1, 2]|       true|    1000.55|   2021-01-15|2021-02-10 01:15:00|\n  2|  Nikolaus|     Brewitt|    brewitt@etsy.com|{+1 000 000 000, ...|    [3]|       true|     900.55|   2021-02-15|2021-02-17 01:15:00|\n  3|  Nikolaus|     Brewitt|    brewitt@etsy.com|        {null, null}|     []|       true|     900.55|   2021-02-15|2021-02-17 01:15:00|\n+---+----------+------------+--------------------+--------------------+-------+-----------+-----------+-------------+-------------------+\n\n</div>"]}}],"execution_count":0},{"cell_type":"code","source":[""],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"e119ea1e-39ab-4ebb-9933-6edb54290fde"}},"outputs":[{"output_type":"display_data","metadata":{"application/vnd.databricks.v1+output":{"data":"","errorSummary":"","metadata":{},"errorTraceType":null,"type":"ipynbError","arguments":{}}},"output_type":"display_data","data":{"text/html":["<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: \"Source Code Pro\", \"Menlo\", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>"]}}],"execution_count":0}],"metadata":{"application/vnd.databricks.v1+notebook":{"notebookName":"36. Creating Spark Data Frame to Select and Rename Columns","dashboards":[],"notebookMetadata":{"pythonIndentUnit":4},"language":"python","widgets":{},"notebookOrigID":4217689076177010}},"nbformat":4,"nbformat_minor":0}