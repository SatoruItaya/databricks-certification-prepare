provider "azurerm" {
  features {}
}

provider "databricks" {
  azure_workspace_resource_id = azurerm_databricks_workspace.dbcert.id

  alias = "created_workspace"
  host  = azurerm_databricks_workspace.dbcert.workspace_url
}
