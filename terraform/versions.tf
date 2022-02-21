terraform {

  required_version = "= 1.1.6"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "2.97.0"
    }

    databricks = {
      source  = "databrickslabs/databricks"
      version = "0.5.0"
    }
  }
}
