resource "azurerm_public_ip" "test" {
  name                = "${var.application_type}-${var.resource_type}-pubip"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  allocation_method   = "Dynamic"
}

output "publicip_id" {
  value = "${azurerm_public_ip.test.id}"
}