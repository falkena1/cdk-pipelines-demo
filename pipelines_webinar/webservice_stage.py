from aws_cdk import core
from aws_cdk.core import DefaultStackSynthesizer
from .pipelines_webinar_stack import PipelinesWebinarStack

class WebServiceStage(core.Stage):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = PipelinesWebinarStack(self, 'WebService', synthesizer=DefaultStackSynthesizer(
            #qualifier="1234567",
            deploy_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/caedge-cicd-deploy-role-ToolchainAccount",
            #cloud_formation_execution_role="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/caedge-cicd-ExecutionRoleStageAccounts"
      )  
    )

    self.url_output = service.url_output

