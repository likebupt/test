import os
from pathlib import Path
from azure.ml import dsl, ArtifactInput, ArtifactOutput
from azure.ml.entities import Environment

conda_env = Environment(
    conda_file=Path(__file__).parent / "conda.yaml",
    image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04"
)

@dsl.command_component(
    name="score_image_classification_keras",
    version="1",
    display_name="Score Image Classification Keras",
    description="score image classification with keras",
    environment=conda_env,
)
def keras_score(
    input_data: ArtifactInput,
    output_result: ArtifactOutput,
    output_metrics: ArtifactOutput
):
    # avoid dependency issue, execution logic is in prep.py file
    from score import score
    score(input_data, output_result, output_metrics)


