variable "aws_region" {
  default = "us-east-1"
}

variable "groq_api_key" {
  description = "Groq API Key"
  type        = string
  sensitive   = true
}