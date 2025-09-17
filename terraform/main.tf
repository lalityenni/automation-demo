terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
  # backend wired via CI later (no local state committed)
  # backend "azurerm" {}
}

provider "azurerm" {
  features {}
}

# placeholder resource so plan/validate do something
resource "random_pet" "repo_marker" {
  length = 2
}