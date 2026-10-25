# План: развертывание Spiritus

Цель: человек скачал репо → за три команды получил рабочего агента, не вникая в устройство.

## Требования (ставит пользователь сам, по README)

| Что | Обязательно |
|---|---|
| git, Python ≥ 3.9 | да |
| рантайм агента — Claude Code или Codex CLI | да |
| Node.js ≥ 18 | только для MCP-серверов на Node (большинство) |
| `git config user.name / user.email` | для коммитов в модулях |
| доступ к GitHub (credential manager / SSH) | только для приватных модулей |
| VS Code | нет, удобство |

MCP-серверы полностью необязательны — подключаются отдельным спеллом по выбору.

## Путь пользователя

```
git clone <repo> spiritus && cd spiritus
python bootstrap.py        # python3 на macOS / Linux
claude                     # или codex — «настрой меня»
```

## Шаги

1. `bootstrap.py` в корне → `arsenal/spiritus-setup/`: проверка окружения, команда `spiritus`
   в PATH (шим в пользовательской bin-папке, PATH — после «да»), `modules sync`, следующий шаг.
   `spiritus run doctor` — та же проверка в любой момент.
2. Core-спеллы (как core-плейбуки): `setup`, `mcp-setup`, `create-domain` — активны всегда.
3. Спелл `setup` — разговорная часть: язык, профиль → `librarium/`, домены / модули,
   предложение `mcp-setup`. Повторный запуск правит, а не перезаписывает.
4. Спелл `mcp-setup` + каталог `arsenal/mcp-servers/` (по файлу на сервер: что дает, что нужно,
   шаблоны конфига для Claude Code / Codex, авторизация, правила). Подключенные →
   `librarium/services.md`. В корневом `AGENTS.md` — общее правило вместо таблицы серверов.
5. `docs/` для людей: getting-started, concepts, cli, modules, mcp, troubleshooting.
6. `README.md` на один экран, ссылки в `docs/`.
7. Правила: `docs/` в Realm, строки в `self-update.md`.
8. Проверка на чистой машине (Windows Sandbox): только git / Python / Node / Claude Code руками.

## Коммиты

1. Структура платформы. 2. `arsenal/`: CLI, `tasks.json`, модули, Telegram.
3. Core-спеллы + `create-domain`. 4. `bootstrap.py`, doctor, спелл `setup`.
5. `README.md` + `docs/`. 6. `mcp-setup` + каталог (Google, GitHub, LinkedIn, Blender, браузер из стеша).
7. Демоны из стеша → модули.

## Состояние

- 2026-10-24: шаги 1–7 сделаны (в диффе, не закоммичены). bootstrap и doctor проверены на Windows
  (реальный запуск, повторный запуск, ветка «папки нет в PATH»); macOS / Linux не проверены.
- Осталось: шаг 8 (чистая машина, macOS / Linux), коммит 7 (демоны → модули).
