resource "null_resource" "configure" {
  triggers = {
    token = databricks_token.pat.token_value
  }

  provisioner "local-exec" {
    command = "databricks configure --host https://${azurerm_databricks_workspace.dbcert.workspace_url}/?o=${azurerm_databricks_workspace.dbcert.workspace_id} --token-file token"
  }
}

# copy the retail_db folder
resource "null_resource" "copy_retail_db" {
  triggers = {
    token = null_resource.configure
  }

  provisioner "local-exec" {
    command = "databricks fs cp ../../../dgadiraju/retail_db dbfs:/public/retail_db --recursive"
  }
}
