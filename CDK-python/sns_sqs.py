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
  
  ## create sns topic
  create_sns = _sns.Topic(self, "stack_name", topic_name = "sns_name")
  ## attach policy for sns
  create_sns.add_to_resource_policy(_iam.PolicyStatement(
    sid = "plicy_name",
    effect = _iam.Effect.ALLOW,
    actions = ["sns:Publish"],
    resources = [create_sns.topic_arn],
    principals = [_iam.ArnPrincipal("*")]
  ))
  
  ## create dlq_sqs queue
  create_dlq_sqs = _sqs.Queue(self, "stack_name", queue_name = "dlq_sqs_name")
  ## create sqs and configure dlq
  create_sqs = _sqs.Queue(
    self, 
    "stack_name",
    queue_name = "sqs_name,
    dead_letter_queue = _sqs.DeadLetterQueue(
      max_receive_count = 1,
      queue = dlq_staging
    )
  )
  
  ## subscribe sqs to sns
  create_sns.add_subscription(_subs.SqsSubscription(create_sqs))
  ## subscribe url to sns
  create_sns.add_subscription(subs.UrlSubscription("https://example.com/"))
  
  ##create object for lambda function
  lambda_arn = _lambda.Function.from_function_arn(
    self,
    "stack_name",
    "lambda_arn"
  )
  
  ## add sqs event to lambda
  lambda_arn.add_event_source(_eventSource.SqsEventSource(create_sqs))
