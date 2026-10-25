# Улучшения Spiritus

Очередность (сверху — первым). Сделанное удаляется из списка.

1. доработать `spiritus` CLI (`arsenal/spiritus-cli/`)
   -> без аргументов: справка + список задач (как npm / just)
   -> `spiritus --version`
   -> короткая форма `spiritus <задача>` без `run` (как pnpm / yarn), `run` остается
   -> `spiritus help <задача>`: описание задачи + `--help` самого инструмента
   -> подсказка при опечатке: «did you mean modules:list?» (difflib)
   -> позже: автодополнение в shell
