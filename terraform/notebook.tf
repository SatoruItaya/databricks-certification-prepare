data "databricks_current_user" "me" {
}

resource "databricks_notebook" "dbcert" {
  source = "Databricks+Certified+Apache+Spark+Developer.dbc"
  path   = "${data.databricks_current_user.me.home}/Databricks Certified Apache Spark Developer"
}
