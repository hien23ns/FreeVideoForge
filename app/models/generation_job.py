from dataclasses import dataclass
from pathlib import Path


@dataclass
class GenerationJob:
    prompt: str
    output_path: Path

    model_name: str = "Wan2.1-T2V-1.3B"
    resolution: str = "480*832"
    frame_num: int = 17

    sample_steps: int = 8
    sample_solver: str = "unipc"
    sample_shift: int = 8
    sample_guide_scale: int = 6

    offload_model: bool = True
    t5_cpu: bool = True