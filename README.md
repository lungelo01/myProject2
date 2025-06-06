# fictional_band

## Setup with Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Then:
```bash
git add README.md
git commit -m "Add project README"
