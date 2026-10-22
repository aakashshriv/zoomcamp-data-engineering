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
  project = "project-394a3001-bf49-42ed-9cd"
  region  = "us-central1"
}

#creating the data warehouse
resource "google_storage_bucket" "data_lake_bucket" {
  name          = "bucket-394a3001"
  location      = "us-central1"
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
  dataset_id = "my_dataset"
  location   = "us-central1"

  delete_contents_on_destroy = true
}
