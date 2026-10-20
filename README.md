# Лабораторная работа № 1

Базовая версия проекта для знакомства с Git, модульными тестами и
GitHub Actions. Проект читает оценки студентов из текстового файла и
рассчитывает средний рейтинг каждого студента.

## Запуск

```bash
python -m pip install -r requirements.txt
python -m src.main -p data/data.txt
pytest
pycodestyle src test
```
