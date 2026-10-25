# Улучшения Spiritus

Очередность (сверху — первым). Сделанное удаляется из списка.

1. доработать `spiritus` CLI (`arsenal/spiritus-cli/`)
   -> без аргументов: справка + список задач (как npm / just)
   -> `spiritus --version`
   -> короткая форма `spiritus <задача>` без `run` (как pnpm / yarn), `run` остается
   -> `spiritus help <задача>`: описание задачи + `--help` самого инструмента
   -> подсказка при опечатке: «did you mean modules:list?» (difflib)
   -> позже: автодополнение в shell
   -> Windows + Git Bash: `spiritus` не находится (bash не подставляет `.cmd`) — bootstrap кладет
      рядом с `spiritus.cmd` еще sh-шим `spiritus`; doctor проверяет оба

2. менеджер модулей: `modules:adopt <name> --url <url>` — взять под управление уже существующий
   локальный домен / демона (git init + push + запись в modules.local.json + exclude), без ручного
   переименования и копирования данных (сейчас 4 ручных шага в docs/modules.md)
