# AI Coding Agent Instructions for ML Project

## Project Overview
This is an end-to-end ML pipeline project with a modular architecture. The codebase follows a standard ML workflow structure: data ingestion → data transformation → model training, orchestrated through training and prediction pipelines.

## Architecture & Component Structure

### Core Modules (`src/`)
- **`exception.py`**: Custom exception handling using `CustomException` class that captures file name and line number for debugging. Accepts `sys` error_detail parameter.
- **`logger.py`**: Currently empty placeholder for centralized logging implementation.
- **`utils.py`**: Helper utilities (empty, to be populated).
- **`components/`**: Core ML processing steps:
  - `data_ingestion.py`: Load and split raw data
  - `data_transformation.py`: Feature engineering and preprocessing
  - `model_trainer.py`: Model training and evaluation
- **`pipeline/`**: Orchestrators:
  - `train_pipeline.py`: Orchestrates end-to-end training workflow
  - `predict_pipeline.py`: Inference pipeline for predictions

## Key Patterns & Conventions

### Error Handling
When adding code, use the `CustomException` class for all exceptions:
```python
from exception import CustomException
try:
    # code
except Exception as e:
    raise CustomException(e, sys)
```

### Module Installation
The project uses `setuptools` with `setup.py`. Install locally with `pip install -e .` (note: `-e .` is filtered from requirements.txt during install).

### Dependencies
Core packages: `pandas`, `numpy`, `seaborn`. Add new dependencies to `requirements.txt` and update `setup.py` automatically picks them up via `get_requirements()`.

## Development Workflow

### Setup
```bash
pip install -r requirements.txt
```

### File Naming & Organization
- Components are self-contained classes/functions in separate files within `src/components/`
- Pipelines orchestrate components and handle data flow sequencing
- Keep logger and exception handling centralized for consistency

## Cross-Component Communication
- Components should be independent and receive inputs/outputs explicitly
- Pipelines are the sole orchestrators; avoid direct component-to-component calls
- Logger and exception modules are application-wide utilities (populate `logger.py` early for consistency)

## Implementation Priorities
1. **Complete `logger.py`** with centralized logging before adding complex components
2. **Implement components** (data_ingestion, data_transformation, model_trainer) before pipeline orchestration
3. **Build pipelines** last, after components are stable
