from pathlib import Path

from app.config.generation import (
    MODEL_NAME,
    RESOLUTION,
    FRAME_NUM,
    SAMPLE_STEPS,
    SAMPLE_SOLVER,
    SAMPLE_SHIFT,
    SAMPLE_GUIDE_SCALE,
    OFFLOAD_MODEL,
    T5_CPU,
)
from app.models.generation_job import GenerationJob


def build_job(prompt: str, output_path: str) -> GenerationJob:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    return GenerationJob(
        prompt=prompt.strip(),
        output_path=Path(output_path),
        model_name=MODEL_NAME,
        resolution=RESOLUTION,
        frame_num=FRAME_NUM,
        sample_steps=SAMPLE_STEPS,
        sample_solver=SAMPLE_SOLVER,
        sample_shift=SAMPLE_SHIFT,
        sample_guide_scale=SAMPLE_GUIDE_SCALE,
        offload_model=OFFLOAD_MODEL,
        t5_cpu=T5_CPU,
    )