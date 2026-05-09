provider "aws" {
  region = var.aws_region
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "mcp-hobby-agent-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Attach basic Lambda execution policy
resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Lambda Function
resource "aws_lambda_function" "hobby_agent" {
  filename         = "lambda_deployment.zip"
  function_name    = "mcp-hobby-agent"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_handler.handler"
  runtime          = "python3.12"
  timeout          = 30
  source_code_hash = filebase64sha256("lambda_deployment.zip")

  environment {
    variables = {
      GROQ_API_KEY = var.groq_api_key
    }
  }
}

# API Gateway
resource "aws_apigatewayv2_api" "hobby_api" {
  name          = "mcp-hobby-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.hobby_api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.hobby_agent.invoke_arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "hobby_route" {
  api_id    = aws_apigatewayv2_api.hobby_api.id
  route_key = "POST /get-hobbies"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.hobby_api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_lambda_permission" "api_gateway" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.hobby_agent.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.hobby_api.execution_arn}/*/*"
}