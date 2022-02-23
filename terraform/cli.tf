resource "null_resource" "configure" {
  triggers = {
    token = databricks_token.pat.token_value
  }

  provisioner "local-exec" {
    command = "databricks configure --host https://${azurerm_databricks_workspace.dbcert.workspace_url}/?o=${azurerm_databricks_workspace.dbcert.workspace_id} --token-file token"
  }
}
