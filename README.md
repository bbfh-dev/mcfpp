[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# MCFunction++

A [beet](https://github.com/mcbeet/beet) plugin designed to ease the development of [Minecraft data-packs](https://minecraft.wiki/w/Data_pack).
It gives a pythonic way of writing code, which is different from how [bolt](https://github.com/mcbeet/bolt) does it.

**Features**:

- Removes mcfunction boilerplate code (events, variables, etc.).
- Allows for python → mcfunction code generation (`for`, `while`, etc.).
- Built-in scoreboard math support (e.g. `sin(a) * b`).
- Support for custom entities, items, & more.
- Highly flexable, allowing for creating solutions to specific problems.

**Standard library**:

MCFunction++ has a standard library containing helpful mcfpp projects to be included in the pipeline.

| Name                 | Description                                                       | Status |
|----------------------|-------------------------------------------------------------------|:------:|
| `registry`           | Adds entity grouping functionality.                               |   🔒   |
| `delayed_load`       | Makes sure that datapack only loads when there's a player online. |   📦   |
| `garbage_collection` | Gets rid of unused scores and storages.                           |   📦   |
| `tick_schedule`      | Makes sure that `tick` function is run after `load`.              |   📦   |

> - **Built-in** 🔒 — Always included in the project.
> - **Default** 📦 — Can be disabled using `Pipeline().configure(...)` method.
