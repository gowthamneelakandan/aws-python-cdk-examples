  
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

class awslambdaservice(core.Stack):
  ## Read local variable from JSON file
  cleansed_bucket = self.node.try_get_context("cleansed_bucket")
  ## configure VPC
  vpc = _ec2.Vpc.from_vpc_attributes( 
        self, 
        'stack_name',
        vpc_id = "vpc_id",
        availability_zones = core.Fn.get_azs(),
        private_subnet_ids = ["subnet1", "subnet2"]
  )
  ## Create lambda
  event_triggering_lambda = _lambda.Function(
        self, 
        'stack_name',
        runtime = _lambda.Runtime.PYTHON_3_8,
        vpc = vpc,
        security_groups=[_ec2.SecurityGroup.from_security_group_id(self, "stack_name", "security_group1")],   
        code = _lambda.Code.asset('path where the script reside'),
        timeout=core.Duration.seconds(30),
        function_name = 'function_name',             
        role = "role_name",
        handler='function_name.lambda_handler',
        environment = {
        	"parm1" : "parm1_value",
        	"parm2" : "parm2_value"
      	} 
  )
