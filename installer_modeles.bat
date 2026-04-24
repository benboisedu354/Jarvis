@echo off
REM Script d'installation des modèles Ollama pour Jarvis
REM Ce script télécharge et installe les modèles recommandés

cls
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║         Installation des modèles Ollama pour Jarvis            ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo IMPORTANT: Assurez-vous qu'Ollama est lancé!
echo (ollama serve dans un autre terminal)
echo.
echo Sélectionnez le modèle à installer:
echo.
echo 1) Mistral 7B (Recommandé - 4-5GB VRAM)
echo 2) Neural Chat 7B (3-4GB VRAM)
echo 3) Dolphin Phi (3B) (3GB VRAM)
echo 4) Orca Mini (3B) (2GB VRAM - Le plus léger)
echo 5) Tous les modèles
echo.
set /p choice="Entrez votre choix (1-5): "

if "%choice%"=="1" (
    echo.
    echo Téléchargement de Mistral...
    ollama pull mistral
    echo. &amp; echo ✓ Mistral installé!
) else if "%choice%"=="2" (
    echo.
    echo Téléchargement de Neural Chat...
    ollama pull neural-chat
    echo. &amp; echo ✓ Neural Chat installé!
) else if "%choice%"=="3" (
    echo.
    echo Téléchargement de Dolphin Phi...
    ollama pull dolphin-phi
    echo. &amp; echo ✓ Dolphin Phi installé!
) else if "%choice%"=="4" (
    echo.
    echo Téléchargement de Orca Mini...
    ollama pull orca-mini
    echo. &amp; echo ✓ Orca Mini installé!
) else if "%choice%"=="5" (
    echo.
    echo Téléchargement de tous les modèles...
    echo.
    echo [1/4] Mistral...
    ollama pull mistral
    echo. &amp; echo [2/4] Neural Chat...
    ollama pull neural-chat
    echo. &amp; echo [3/4] Dolphin Phi...
    ollama pull dolphin-phi
    echo. &amp; echo [4/4] Orca Mini...
    ollama pull orca-mini
    echo. &amp; echo ✓ Tous les modèles installés!
) else (
    echo Choix invalide!
    pause
    exit /b 1
)

echo.
echo.
echo Modèles disponibles:
ollama list

echo.
echo ✓ Installation terminée!
echo Vous pouvez maintenant lancer Jarvis avec jarvis.bat
echo.
pause
