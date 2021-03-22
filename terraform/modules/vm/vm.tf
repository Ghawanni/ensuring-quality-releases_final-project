# resource "azurerm_subnet" "internal" {
#   name                 = "internal-subnet"
#   resource_group_name  = "${var.resource_group}"
#   virtual_network_name = "${var.virtual_network_name}"
#   address_prefix       = "${var.address_prefix_test}"
# }

resource "azurerm_network_interface" "test-ni" {
  name                = "ni-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.virtual_network_subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address_id}"
  }
}

resource "azurerm_linux_virtual_machine" "test-vm" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "${var.vm_size}"
  admin_username      = "mghawanni"
  network_interface_ids = [
    "${azurerm_network_interface.test-ni.id}"
  ]
  admin_ssh_key {
    username   = "mghawanni"
    public_key = "${var.public_key}"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}
