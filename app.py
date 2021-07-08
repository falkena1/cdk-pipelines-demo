#!/usr/bin/env python3

from aws_cdk import core

from pipelines_webinar.pipeline_stack import PipelineStack

PIPELINE_ACCOUNT = '887780435731'

app = core.App()
PipelineStack(app, 'PipelineStack', env={
  'account': PIPELINE_ACCOUNT,
  'region': 'eu-central-1',
})

app.synth()
