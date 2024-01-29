# silver-giggle

[![Training](https://github.com/theo43/silver-giggle/actions/workflows/sagemaker_workflow.yml/badge.svg)](https://github.com/theo43/silver-giggle/actions/workflows/sagemaker_workflow.yml)

## Architecture
This project aims at containing in a single mono repo everything you need to `experiment` (train and validate
your models), and then create the Docker images you need to push these models to `production`. `packages`
is where the code used on one hand to validate models during experiments, on the other hand in production,
is tested and packaged. It is then only written once at a single place to avoid duplications.

## Experiments
### Requirements
Activate a Python 3.10 installation, then:
```
cd experiments
python -m venv venv-exp
source ./venv-exp/bin/activate
pip install -r requirements-exp.txt
```

To link your venv to a Jupyter notebook kernel, run with your activated `venv-exp`:
```
python -m ipykernel install --name=venv-exp
```
You can then use that env in an activated Jupyter notebook.

## Sources

This repository is inspired by the following sources:
- [KREUZBERGER, Dominik, KÜHL, Niklas, et HIRSCHL, Sebastian. Machine learning operations (mlops): Overview, definition, and architecture. IEEE Access, 2023.](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10081336)