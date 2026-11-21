@echo off
chcp 65001 >nul
title Conectar Google NotebookLM
cls
echo ========================================================
echo         CONECTANDO AO GOOGLE NOTEBOOKLM
echo ========================================================
echo.
echo Uma janela do Google Chrome vai abrir na sua tela.
echo Faca seu login normalmente na sua conta Google.
echo Assim que entrar no NotebookLM, o sistema vai salvar
echo a conexao e fechar a janela do Chrome.
echo.
echo ========================================================
echo Abrindo navegador...
echo ========================================================
echo.

cd /d "C:\Users\PC_User\.gemini\config\skills\notebooklm"
".venv\Scripts\python.exe" -u scripts\auth_manager.py setup

echo.
echo ========================================================
echo Pronto! Agora o assistente ja consegue ler seus cadernos.
echo Pressione qualquer tecla para fechar esta janela.
echo ========================================================
pause >nul

