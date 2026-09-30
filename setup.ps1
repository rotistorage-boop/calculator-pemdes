$ErrorActionPreference = "Stop"

Write-Host "Creating virtual environment..."

python -m venv .venv

Write-Host "Activating virtual environment..."

& ".\.venv\Scripts\Activate.ps1"

Write-Host "Upgrading pip..."

python -m pip install --upgrade pip

Write-Host "Installing dependencies..."

pip install -r requirements.txt

Write-Host ""
Write-Host "Setup complete."
Write-Host "Run the application with:"
Write-Host "python main.py"