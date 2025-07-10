# LLM Parse Agent

This project demonstrates a Python CI/CD setup with GitHub Actions, including:

- Automated testing with pytest
- Linting with flake8 (excluding .venv)
- Docstring checks with pydocstyle
- Data drift detection on CSV data (mean check)
- Environment variable demo for API keys

## Data Drift Check

- The `drift_check.py` script checks if the mean of the `age_int` column in `sample_data.csv` is within a specified threshold.
- The drift check pipeline only runs when `sample_data.csv` is updated.

## How to Use

- Place your data in `sample_data.csv`.
- Update the file and push to trigger only the drift check pipeline.
- All other pipelines ignore changes to this file.

## Requirements

- Python 3.12
- See `requirements.txt` for dependencies

## Ignore

- `.venv/` and `README.md` are ignored by CI pipelines.

---

For more details, see the workflow files in `.github/workflows/`.
