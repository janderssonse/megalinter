---
title: LUA linters in MegaLinter
description: luacheck is available to analyze LUA files in MegaLinter
---
<!-- markdownlint-disable MD003 MD020 MD033 MD041 -->
<!-- @generated by .automation/build.py, please don't update manually -->
<!-- Instead, update descriptor file at https://github.com/oxsecurity/megalinter/tree/main/megalinter/descriptors/lua.yml -->
# LUA

## Linters

| Linter                                                                | Additional                                                                                                                       |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**luacheck**](lua_luacheck.md)<br/>[_LUA_LUACHECK_](lua_luacheck.md) | [![GitHub stars](https://img.shields.io/github/stars/luarocks/luacheck?cacheSeconds=3600)](https://github.com/luarocks/luacheck) |

## Linted files

- File extensions:
  - `.lua`

## Configuration in MegaLinter

| Variable                 | Description                                     | Default value |
|--------------------------|-------------------------------------------------|---------------|
| LUA_PRE_COMMANDS         | List of bash commands to run before the linters | None          |
| LUA_POST_COMMANDS        | List of bash commands to run after the linters  | None          |
| LUA_FILTER_REGEX_INCLUDE | Custom regex including filter                   |               |
| LUA_FILTER_REGEX_EXCLUDE | Custom regex excluding filter                   |               |

