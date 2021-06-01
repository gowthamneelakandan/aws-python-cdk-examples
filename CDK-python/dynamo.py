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

class awssnsservice(core.Stack):
  ## Read local variable from JSON file
  bucket_name = self.node.try_get_context("bucket_name")
  
  ##create object for lambda function
  lambda_arn = _lambda.Function.from_function_arn(
    self,
    "stack_name",
    "lambda_arn"
  )
  
  ## create dynamo table
  create_table1 = _ddb.Table(
    self, 
    'stack_name', 
    table_name='dynamo_table_name',
    partition_key=_ddb.Attribute(name='column_name', type=_ddb.AttributeType.STRING),
    read_capacity = 50,
    write_capacity = 50
  )
  
  ## granting access
  create_table1.grant_read_data(lambda_arn)
  
