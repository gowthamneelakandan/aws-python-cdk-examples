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

class awscloudwatchservice(core.Stack):
  ## Read local variable from JSON file
  cleansed_bucket = self.node.try_get_context("cleansed_bucket")
	
  ## Cloudwatch for triggering step function
  ## Timezone followed by AWS-Cloudwatch is UTC
  step_schedule = _events.Schedule.cron(day=None, hour="23", minute="0", month=None, week_day=None, year=None)
  event_step_target = _events_targets.SfnStateMachine(machine = stepFunction)
  cloudwatch_event1 = _events.Rule(
      self,
      "stack_name",
      description="Every day at 11 PM ",
      rule_name = "role_name",
      enabled=True,
      schedule=step_schedule,
      targets=[event_step_target])
		
  ## Cloudwatch for triggering lambda
  ##create object for lambda function
  archive_lambda_arn = _lambda.Function.from_function_arn(
      self,
      'stack_name',
      'lambda ARN')
    
  job_parameter1 = _events.RuleTargetInput.from_object('{"parm1": "parm1_value","parm2":"parm2_value","parm3": "parm3_value","parm4": "parm4_value"}')
  job_parameter2 = _events.RuleTargetInput.from_object('{"parm1": "parm1_value","parm2":"parm2_value","parm3": "parm3_value","parm4": "parm4_value"}')

  cw_archiving_trigger = _events.Schedule.cron(day=None, hour="20", minute="0", month=None, week_day=None, year=None)

  event_lambda_target1 = _events_targets.LambdaFunction(handler=archive_lambda_arn, event=job_parameter1)
  event_lambda_target2 = _events_targets.LambdaFunction(handler=archive_lambda_arn, event=job_parameter2)
  cloudwatch_event2 = _events.Rule(
      self,
      "stack_name",
      description="Every day at 8PM UTC ",
      rule_name="role_name",
      enabled=True,
      schedule=cw_archiving_trigger,
      targets=[event_lambda_target1,event_lambda_target2])
