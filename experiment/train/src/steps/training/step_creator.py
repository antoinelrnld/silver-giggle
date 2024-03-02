from sagemaker.workflow.steps import (
    TrainingStep, CacheConfig
)
from sagemaker.processing import FrameworkProcessor
from sagemaker.inputs import TrainingInput
from pathlib import Path
from sagemaker.pytorch import PyTorch

BASE_PATH = Path(__file__).resolve().parent


def create_training_step(
    session: str,
    role: str,
    s3_bucket_name: str,
    instance_type: str,
    instance_count: int,
    image_uri,
    train_data,
    tokenizers_path
):
    output_path = f's3://{s3_bucket_name}/models/estimator-models'
    
    estimator = PyTorch(
        entry_point='entrypoint.py',
        source_dir=str(BASE_PATH),
        role=role,
        instance_count=instance_count,
        instance_type=instance_type,
        framework_version='1.13.1',
        py_version='py3',
        output_path=output_path,
        sagemaker_session=session
    )

    train_input = TrainingInput(
        s3_data=train_data
    )
    tokenizers_path = TrainingInput(
        s3_data=tokenizers_path
    )
    step_train = TrainingStep(
        name='TrainingStep',
        estimator=estimator,
        inputs={
            'training': train_input,
            'tokenizers': tokenizers_path
        },
        cache_config=CacheConfig(
            enable_caching=True,
            expire_after='10d'
        )
    )

    return step_train
