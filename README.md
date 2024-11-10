# it-hatters_hacks_ai_24
Вот решение "Отбор кандидатов по типу личности" от hacks-ai. Проект от команды it-hatters предлагает систему оценки подходящих работ на основе анализа видео резюме кандидата.

## Оглавление
- [Описание](#описание)
- [Технологии](#технологии)
- [Использование](#использование)
- [Структура проекта](#структура-проекта)
- [Функциональность](#функциональность)
- [Контакты](#контакты)

# Анализ Видео Визиток Кандидатов для Оценки Типа Личности и Рекомендаций по Карьере

Этот проект предоставляет веб-интерфейс для анализа видео визиток кандидатов, чтобы автоматически определить их тип личности по MBTI и визуализировать их личностные параметры по модели OCEAN. Система также рекомендует наиболее подходящие профессии для кандидатов. Работодатели могут использовать эту платформу для массовой обработки видео и подбора наиболее подходящих кандидатов.

## Оглавление
- [Описание проекта](#описание-проекта)
- [Функциональность](#функциональность)
- [Технологии и зависимости](#технологии-и-зависимости)
- [Установка](#установка)
- [Использование](#использование)
- [Структура проекта](#структура-проекта)
- [Контакты](#контакты)

---

## Описание проекта

Платформа предлагает два интерфейса:
1. Для кандидатов — кандидаты загружают видео визитки и получают:
   - Тип личности по MBTI (например, INTJ, ENFP и т.д.)
   - Паутинку по модели OCEAN, визуализирующую их характеристики (открытость, добросовестность, экстраверсию, доброжелательность и невротизм).
   - Три профессии, которые могут наиболее соответствовать их личностному профилю.

2. Для работодателей — позволяет загружать несколько видео визиток для автоматической обработки. Система анализирует кандидатов и выводит список наиболее подходящих на основе их характеристик и соответствия заданным критериям.

Анализ выполняется на основе мультимодального подхода, включающего:
   - Видео-анализ: выявление невербальных признаков с использованием видеокадров.
   - Анализ текста: обработка речи кандидата.
   - Анализ аудио: извлечение эмоциональных и интонационных особенностей голоса.

## Функциональность

- Интерфейс кандидата:
  - Загрузка видео визитки.
  - Получение MBTI и визуализации по OCEAN.
  - Профориентационные рекомендации.

- Интерфейс работодателя:
  - Загрузка нескольких видео визиток.
  - Просмотр списка кандидатов с их MBTI и характеристиками.
  - Фильтрация и ранжирование кандидатов по наиболее подходящим для вакансии личностным параметрам.

## Технологии и зависимости

Проект написан на Python и использует следующие основные библиотеки и фреймворки:
- Dash — для создания веб-интерфейса.
- Mediapipe — для анализа видео и выявления невербальных признаков.
- NLTK — для обработки текста и анализа речи.
- Pandas — для работы с данными.
- OpenCV (cv2) — для обработки видео и изображений.
- Numpy — для численных расчетов.
- Matplotlib — для визуализации данных, включая паутинку OCEAN.
- Librosa — для анализа аудио и голосовых характеристик.

Все зависимости перечислены в [requirements.txt](requirements.txt).
