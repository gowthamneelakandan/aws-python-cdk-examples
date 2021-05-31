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

class awss3service(core.Stack):
  ## Read local variable from JSON file
  bucket_name = self.node.try_get_context("bucket_name")
  
  ## Create object for S3 bcuekt
  bucket_name_obj = s3.Bucket.from_bucket_name(
      self, 'bucket_name',
      bucket_name
      )
  
  #upload whl files  
  s3deploy.BucketDeployment(
      self, 
      'stack_name',
      sources = [s3deploy.Source.asset("assets/glue/")],
      destination_bucket = bucket_name_obj, ## s3 bucket name passed as object
      destination_key_prefix = "folder_path in s3",
      )
  
