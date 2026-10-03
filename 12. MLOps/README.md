# Build & Track ML Pipelines with DVC

## How to run?

conda create -n test python=3.11 -y

conda activate test

cd "1. ML Pipeline using DVC"

python -m pip install -r requirements.txt


## DVC Commands

Run these commands from `1. ML Pipeline using DVC`:

```bash
# Initialize Git/DVC only if they have not been initialized already.
git init

dvc init

# Use a short cache path on Windows to avoid long run-cache filenames.
dvc config --local cache.dir C:\dvc-cache

dvc repro

dvc dag

dvc metrics show
```