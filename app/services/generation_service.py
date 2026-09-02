import json
from pathlib import Path

from app.models.generation_job import GenerationJob


def save_job(job: GenerationJob, path: str) -> Path:
    job_path = Path(path)

    data = {
        "prompt": job.prompt,
        "output_path": str(job.output_path),
        "model_name": job.model_name,
        "resolution": job.resolution,
        "frame_num": job.frame_num,
        "sample_steps": job.sample_steps,
        "sample_solver": job.sample_solver,
        "sample_shift": job.sample_shift,
        "sample_guide_scale": job.sample_guide_scale,
        "offload_model": job.offload_model,
        "t5_cpu": job.t5_cpu,
    }

    job_path.parent.mkdir(parents=True, exist_ok=True)
    job_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return job_path