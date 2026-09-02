import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.pipeline.job_builder import build_job
from app.services.generation_service import save_job


PROMPT = """
A young software engineer typing code at night,
cinematic lighting, realistic,
slow camera movement,
multiple monitors displaying code,
rain falling outside the window,
warm desk lamp,
cinematic composition
""".strip()


def main():
    job = build_job(
        prompt=PROMPT,
        output_path="outputs/freevideoforge_mvp.mp4",
    )

    job_path = save_job(
        job,
        "outputs/freevideoforge_mvp.json",
    )

    print("Generation job created successfully.")
    print(f"Job file: {job_path}")
    print(f"Prompt: {job.prompt}")
    print(f"Model: {job.model_name}")
    print(f"Resolution: {job.resolution}")
    print(f"Frames: {job.frame_num}")
    print(f"Steps: {job.sample_steps}")


if __name__ == "__main__":
    main()