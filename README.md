# LootGen

## Описание
Консольная утилита для симуляции вероятности выпадения редких игровых предметов (лута) из сундуков. Используется для баланса игры.

## Технологии
- Python 3.12
- rich (красивый вывод таблиц)
- ruff (линтер)
- GitHub Actions (CI/CD)

## Развертывание

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/ТВОЙ_НИК/LootGen.git
   cd LootGen
2.Создай виртуальное окружение и установи зависимости одной командой: 
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
3.Запусти утилиту: 
   python lootgen.py          # 100 сундуков
   python lootgen.py 50       # 50 сундуков
