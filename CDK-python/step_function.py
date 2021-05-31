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

class awsstepfunctionservice(core.Stack):
  ## Read local variable from JSON file
  cleansed_bucket = self.node.try_get_context("cleansed_bucket")
  
  ## Object for IAM role
  role_obj = _iam.Role.from_role_arn(self,"stack_name","role_arn", mutable = None)
  
  ## Step function with one after another
  synck1 = _stepfunctions.IntegrationPattern.RUN_JOB
  gjob_invoke_task = sfn_tasks.GlueStartJobRun(
      self,
      "stack_name",
      glue_job_name="job_name1",
      integration_pattern = synck1
  )
  gjob_invoke_task2 = sfn_tasks.GlueStartJobRun(
      scope=self,
      "stack_name",
      glue_job_name="job_name2",
      integration_pattern = synck1
  )        
	
  definition = gjob_invoke_task.next(gjob_invoke_task2)
  
  ## Example
  ##        job1
  ##        job2

  ## Step function with parallel
  synck1 = _stepfunctions.IntegrationPattern.RUN_JOB
  gjob_invoke_task = sfn_tasks.GlueStartJobRun(
      self,
      "stack_name",
      glue_job_name="job_name1",
      integration_pattern = synck1
  )
  gjob_invoke_task2 = sfn_tasks.GlueStartJobRun(
      self,
      "stack_name",
      glue_job_name="job_name2",
      integration_pattern = synck1
  )    
  gjob_invoke_task3 = sfn_tasks.GlueStartJobRun(
      self,
      "stack_name",
      glue_job_name="job_name3",
      integration_pattern = synck1
  )
  gjob_invoke_task4 = sfn_tasks.GlueStartJobRun(
      self,
      "stack_name",
      glue_job_name="job_name4",
      integration_pattern = synck1
  )
  gjob_invoke_task5 = sfn_tasks.GlueStartJobRun(
      self,
      "stack_name",
      glue_job_name="job_name5",
      integration_pattern = synck1
  )
  parallel_task = _stepfunctions.Parallel(self, 'Task name')
  definition = gjob_invoke_task.next(parallel_task
                                    .branch(gjob_invoke_task2)
                                    .branch(gjob_invoke_task3)
                                    .branch(gjob_invoke_task4)).next(gjob_invoke_task5)
  ## Example
  ##        job1   
  ## job2   job3   job4
  ##        job5
    
  ## Create step function
  stepFunction = _stepfunctions.StateMachine(
      self,
      "stack_name",
      state_machine_name = "step_function_name",
      definition = definition,
      role = role_obj ## IAM role obj
  )
