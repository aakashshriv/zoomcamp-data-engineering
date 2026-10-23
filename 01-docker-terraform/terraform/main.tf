#detail of the cloud service provider
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 8.8"
    }
  }
}

#cloud plugin for the provider
provider "google" {
  project = var.project
  region  = var.region
}

#creating the data warehouse
resource "google_storage_bucket" "data_lake_bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  storage_class = "STANDARD"

  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"

  versioning {
    enabled = true
  }

  # Set deletion automatic deletion age
  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30
    }
  }


  force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location

  delete_contents_on_destroy = true
}
