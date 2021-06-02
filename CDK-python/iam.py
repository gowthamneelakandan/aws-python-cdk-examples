from aws_cdk import (
	core,
	aws_iam as _iam,
	aws_lambda as _lambda,
	aws_glue as _glue,
	aws_lakeformation as _lakeformation,
	aws_s3_deployment as s3deploy,
	aws_s3 as s3,
	aws_dynamodb as _ddb,
	aws_ec2 as _ec2,
	aws_apigateway as _apigw,
	aws_cognito as _cognito,
	aws_sns as _sns,
	aws_sqs as _sqs,
	aws_sns_subscriptions as _subs,
	aws_s3_notifications as _s3n,
	custom_resources as _cr,
	aws_lambda_event_sources as _eventSource,
	aws_events as _events,
	aws_logs as _logs,
	aws_logs_destinations as _logs_destinations,
	aws_events_targets as _targets,
	aws_secretsmanager as _secman
)
import os, boto3, json

class awsiamservice(core.Stack):
  ## Read local variable from JSON file
  bucket_name = self.node.try_get_context("bucket_name")
  
  ## create IAM role
  create_role1 = _iam.Role(
    self,
    'stack_name',
    role_name="role_name",
    assumed_by=_iam.CompositePrincipal(
      _iam.ServicePrincipal('glue.amazonaws.com'),
      _iam.ServicePrincipal('states.eu-west-1.amazonaws.com'),
      _iam.ServicePrincipal('lambda.amazonaws.com')
    ),
    managed_policies=[
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "AmazonS3FullAccess"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "service-role/AWSGlueServiceRole"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "AWSGlueConsoleFullAccess"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "AWSStepFunctionsFullAccess"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "AWSLakeFormationDataAdmin"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "service-role/AWSLambdaBasicExecutionRole"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "SecretsManagerReadWrite"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "AWSLambdaFullAccess"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
					"AmazonDynamoDBFullAccess"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
					"AmazonSQSFullAccess"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
					"service-role/AWSLambdaVPCAccessExecutionRole"),
      _iam.ManagedPolicy.from_aws_managed_policy_name(
        "service-role/AWSLambdaBasicExecutionRole")
    ],
  )
  
  ##create object for lambda function
  lambda_arn = _lambda.Function.from_function_arn(
    self,
    "stack_name",
    "lambda_arn"
  )
  
  
