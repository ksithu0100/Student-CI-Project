# Student-CI-Project

Continuous Integration automation assignment using Jenkins and GitHub Webhooks.

## Structure
- `app.py`: Primary application logic.
- `tests/test_app.py`: Unit test suite using Python `unittest`.

## Running Locally
```bash
python app.py
python -m unittest discover -s tests


git commit -am "Trigger: verify webhook push execution"
git push origin main