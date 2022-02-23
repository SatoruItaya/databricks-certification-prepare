resource "databricks_token" "pat" {
  provider         = databricks.created_workspace
  comment          = "Terraform Provisioning"
  lifetime_seconds = 86400

  provisioner "local-exec" {
    command = "echo ${self.token_value} >> token"
  }
}

output "databricks_token" {
  value     = databricks_token.pat.token_value
  sensitive = true
}
