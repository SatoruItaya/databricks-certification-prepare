resource "azurerm_resource_group" "dbcert" {
  name     = "dbcert"
  location = "Japan East"
}

resource "azurerm_databricks_workspace" "dbcert" {
  name                = "dbcert"
  resource_group_name = azurerm_resource_group.dbcert.name
  location            = azurerm_resource_group.dbcert.location
  sku                 = "standard"
}
