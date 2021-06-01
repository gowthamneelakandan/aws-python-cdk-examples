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

class awssecretmanagerservice(core.Stack):
  ## Read local variable from JSON file
  secret1 = self.node.try_get_context("secret1")
  secret2 = self.node.try_get_context("secret2")
  
  secret_string = {'secret1': 'secret1_value','secret2': 'secret2_value'}
  
  ## create secret manager
  create_secret1 _secman.CfnSecret(
    self,
    secret_name,
    description = "description ",
    name = "secret_name",
    secret_string = json.dumps(secret_string)
  )
