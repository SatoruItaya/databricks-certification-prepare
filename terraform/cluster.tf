data "databricks_spark_version" "latest_lts" {
  long_term_support = true

  depends_on = [
    azurerm_databricks_workspace.dbcert
  ]
}

data "databricks_node_type" "smallest" {
  local_disk = true

  depends_on = [
    azurerm_databricks_workspace.dbcert
  ]
}

resource "databricks_cluster" "dbcert" {
  cluster_name            = "Databricks Certification Cluster"
  spark_version           = data.databricks_spark_version.latest_lts.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 15

  spark_conf = {
    # Single-node
    "spark.databricks.cluster.profile" : "singleNode"
    "spark.master" : "local[*,4]"
  }

  spark_env_vars = {
    PYSPARK_PYTHON = "/databricks/python3/bin/python3"
  }

  custom_tags = {
    "ResourceClass" = "SingleNode"
  }
}
