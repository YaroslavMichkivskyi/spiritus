@echo off
rem Start Spiritus with the Telegram channel - Windows twin of start.sh
cd /d "%~dp0..\.."
claude --channels plugin:telegram@claude-plugins-official %*
