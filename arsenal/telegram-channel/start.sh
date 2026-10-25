#!/usr/bin/env sh
# Start Spiritus with the Telegram channel - macOS / Linux twin of start.cmd
cd "$(dirname "$0")/../.." || exit 1
exec claude --channels plugin:telegram@claude-plugins-official "$@"
