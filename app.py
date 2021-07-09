#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import DefaultStackSynthesizer

from pipelines_webinar.pipeline_stack import PipelineStack

PIPELINE_ACCOUNT = '887780435731'

app = core.App()

PipelineStack(app, 'PipelineStack',
  #synthesizer=DefaultStackSynthesizer(
        #qualifier="1234567",
        #deploy_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/caedge-cicd-ExecutionRoleStageAccounts",
        #cloud_formation_execution_role="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/caedge-cicd-ExecutionRoleStageAccounts"
  #), 
  env={
  'account': PIPELINE_ACCOUNT,
  'region': 'eu-central-1',
  }
)

app.synth()
