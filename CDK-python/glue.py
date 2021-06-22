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

class awsglueservice(core.Stack):
  
  ## Read local variable from JSON file
  cleansed_bucket = self.node.try_get_context("cleansed_bucket")
  
  ## Create glue classifier
  glue_classifier = _glue.CfnClassifier(self, 'json-classifiers',json_classifier = _glue.CfnClassifier.JsonClassifierProperty(json_path ="$[*]", name = "json-classifiers"))
  glue_database = _glue.Database("database_name")
  
  ## Create Crawler
  ## By default last folder of your s3 path is the table name created in ATHENA
  ##  else will be added to prefix
  glue_crawler1 = _glue.CfnCrawler(
      self,
      'stack_name',
      name = "crawler_name',
      role = "role_name",
      targets = {
          's3Targets': [
              {
              'path': "S3-path where your file reside"
              }
          ]
      },
      database_name = "database_name",
      table_prefix = "prefix_" 
      )
  ## create connection
  conn_prop = { "JDBC_CONNECTION_URL": "jdbc:oracle:thin://@endpoint:1521:SID","USERNAME" : "username","PASSWORD":"password" }
  phy_conn_prop = CfnConnection.PhysicalConnectionRequirementsProperty(availability_zone = 'eu-west-1a', security_group_id_list=['sg_name'], subnet_id= 'subnet_name')
  conn_inp_prop = CfnConnection.ConnectionInputProperty(connection_properties=conn_prop, connection_type = 'JDBC', description='glue-connection-creation',name='glue-connection-creation',physical_connection_requirements=phy_conn_prop)
  conne_creation = _glue.CfnConnection(self, 'glue-connection-creation',catalog_id='aws_account_number',connection_input=conn_inp_prop)

  ## Create GLUE
  glue_job1 = _glue.CfnJob(
      self,
      'stack_name,
      name = "glue_job_name",
      role = "role_name",
      max_capacity = 1,
      glue_version = "2.0",
      command = _glue.CfnJob.JobCommandProperty(
            name='glueetl',
            python_version = "3",
            script_location="s3path of script location"
      ),
      connections = _glue.CfnJob.ConnectionsListProperty(
                connections=['connection_name']
      ),
      execution_property = _glue.CfnJob.ExecutionPropertyProperty(
            max_concurrent_runs=100
      ),
      default_arguments = {
            '--additional-python-modules': "awswrangler==2.3.0,pyarror==2",
            '--job_name': "job_name"
            }
      )
  
  ## Glue Trigger
  ## schedule in AWS is UTC
  glue_trigger1 = _glue.CfnTrigger(
      self,
      "stack_name",
      schedule = "cron(0 6 * * ? *)", # every day at 8am
      name="glue_trigger_name",
      type='SCHEDULED',
      description= 'Trigger GLUE job, 8AM CET/ 6AM UTC',
      actions=[
            _glue.CfnTrigger.ActionProperty(
		    job_name="glue_job_name")
      ],
      start_on_creation=True
      )
