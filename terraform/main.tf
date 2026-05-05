provider "local" {}

resource "null_resource" "devops_project" {
  provisioner "local-exec" {
    command = "echo DevOps Infrastructure Created Successfully"
  }
}