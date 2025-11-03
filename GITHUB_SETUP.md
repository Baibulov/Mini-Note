# Инструкция по загрузке проекта в GitHub

✅ **Шаг 1 и 2 уже выполнены!**
- Git настроен (email: t.baibulov@aues.kz, имя: Baibulov)
- Первый коммит создан

## Следующий шаг: Создание репозитория на GitHub

1. Зайдите на https://github.com
2. Нажмите кнопку "+" в правом верхнем углу
3. Выберите "New repository"
4. Название репозитория: `Mini-Note` (или любое другое)
5. Описание: `API-сервис для управления заметками с полным CRUD-функционалом`
6. Выберите Public или Private
7. **НЕ** добавляйте README, .gitignore или лицензию (они уже есть)
8. Нажмите "Create repository"

## Шаг 4: Подключение локального репозитория к GitHub

После создания репозитория GitHub покажет инструкции. Выполните команды (замените `Baibulov` на ваш GitHub username, если он отличается):

```powershell
git remote add origin https://github.com/Baibulov/Mini-Note.git
git branch -M main
git push -u origin main
```

**Если ваш GitHub username отличается от "Baibulov", замените его в команде выше.**

Если вы используете SSH:

```powershell
git remote add origin git@github.com/Baibulov/Mini-Note.git
git branch -M main
git push -u origin main
```

## Альтернативный способ (через GitHub CLI)

Если у вас установлен GitHub CLI, можете создать репозиторий одной командой:

```powershell
gh repo create Mini-Note --public --source=. --remote=origin --push
```

## Проверка

После успешной загрузки ваш репозиторий будет доступен по адресу:
`https://github.com/Baibulov/Mini-Note`

