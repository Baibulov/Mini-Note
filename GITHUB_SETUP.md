# Инструкция по загрузке проекта в GitHub

## Шаг 1: Настройка Git (если еще не настроено)

Выполните следующие команды, заменив данные на свои:

```powershell
git config --global user.name "Ваше Имя"
git config --global user.email "your.email@example.com"
```

Или для локальной настройки только этого репозитория:

```powershell
git config user.name "Ваше Имя"
git config user.email "your.email@example.com"
```

## Шаг 2: Создание первого коммита

После настройки Git выполните:

```powershell
cd C:\Users\lordd\Downloads\Petproject
git add .
git commit -m "Initial commit: Mini-Note API service with full CRUD functionality"
```

## Шаг 3: Создание репозитория на GitHub

1. Зайдите на https://github.com
2. Нажмите кнопку "+" в правом верхнем углу
3. Выберите "New repository"
4. Название репозитория: `Mini-Note` (или любое другое)
5. Описание: `API-сервис для управления заметками с полным CRUD-функционалом`
6. Выберите Public или Private
7. **НЕ** добавляйте README, .gitignore или лицензию (они уже есть)
8. Нажмите "Create repository"

## Шаг 4: Подключение локального репозитория к GitHub

После создания репозитория GitHub покажет инструкции. Выполните команды вида:

```powershell
git remote add origin https://github.com/ВАШ_USERNAME/Mini-Note.git
git branch -M main
git push -u origin main
```

**Замените `ВАШ_USERNAME` на ваш GitHub username и `Mini-Note` на название вашего репозитория.**

Если вы используете SSH:

```powershell
git remote add origin git@github.com:ВАШ_USERNAME/Mini-Note.git
git branch -M main
git push -u origin main
```

## Альтернативный способ (через GitHub CLI)

Если установлен GitHub CLI:

```powershell
gh repo create Mini-Note --public --source=. --remote=origin --push
```

## Проверка

После успешной загрузки ваш репозиторий будет доступен по адресу:
`https://github.com/ВАШ_USERNAME/Mini-Note`

