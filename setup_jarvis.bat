@echo off

echo ==========================
echo 🤖 SETUP JARVIS AUTO
echo ==========================

REM Vérifie Python 3.11
py -3.11 --version
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python 3.11 non trouvé
    pause
    exit /b
)

echo.
echo 🧠 Création environnement virtuel...
py -3.11 -m venv venv

echo.
echo ⚡ Activation venv...
call venv\Scripts\activate

echo.
echo 📦 Mise à jour pip...
python -m pip install --upgrade pip

echo.
echo 📥 Installation dépendances...
pip install -r requirements.txt

echo.
echo 🔍 Vérification Ollama...
where ollama >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo ⚠️ Ollama non trouvé (optionnel mais recommandé)
)

echo.
echo 🚀 Lancement Jarvis...
python main.py

pause