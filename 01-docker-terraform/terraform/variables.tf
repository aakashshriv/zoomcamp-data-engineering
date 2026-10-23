#not required when logged in with ADC(gcloud auth application-default login)
# variable "credentials" {
#   description = "My Credentials"
#   default     = "<Path to your Service Account json file>"

# }


variable "project" {
  description = "Project"
  default     = "project-394a3001-bf49-42ed-9cd"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default = "my_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "bucket-394a3001"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}