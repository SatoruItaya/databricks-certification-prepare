data "databricks_current_user" "me" {

  depends_on = [
    azurerm_databricks_workspace.dbcert
  ]
}

resource "databricks_notebook" "dbcert" {
  source = "Databricks+Certified+Apache+Spark+Developer.dbc"
  path   = "${data.databricks_current_user.me.home}/Databricks Certified Apache Spark Developer"

  lifecycle {
    ignore_changes = [format]
  }
}
