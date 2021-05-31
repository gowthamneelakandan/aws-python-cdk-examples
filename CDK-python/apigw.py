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

class awsapigwservice(core.Stack):
  ## Read local variable from JSON file
  cleansed_bucket = self.node.try_get_context("cleansed_bucket")
  ## policy for API-GW
  apigw_policy = _iam.PolicyDocument(
		 statements=[
		    _iam.PolicyStatement(
           principals=[_iam.AnyPrincipal()],
           actions=["execute-api:Invoke"],
           resources=[core.Fn.join("", ["execute-api:/", "*"])],
           effect=_iam.Effect.ALLOW,
           sid="AllowVPCAccessToApi"
         )
		 ]
  )
  
  ##create object for lambda function
  event_triggering_lambda = _lambda.Function.from_function_arn(
      self,
      'stack_name',
      'lambda ARN')
  
  ## Create API-GW
  base_api = _apigw.LambdaRestApi(self, 'dsm-dap-apigw-common-provisioning-event-triggering',
			endpoint_configuration = _apigw.EndpointConfiguration(
			  types = [_apigw.EndpointType.PRIVATE],
			  vpc_endpoints = [_ec2.InterfaceVpcEndpoint.from_interface_vpc_endpoint_attributes(
          self, 
          'stack_name',
			    port = 443,
			    vpc_endpoint_id = "vpc_id",
			    security_group_id = "security_group_id"
			  )]
			),
			policy = apigw_policy,
			proxy = False,
			deploy_options = {'stage_name': 'v1'},
			rest_api_name = 'api_ge_name',
			description = 'description',
			handler = event_triggering_lambda
  )
