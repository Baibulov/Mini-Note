# Решение проблемы аутентификации GitHub

## Проблема
Git пытается использовать учетные данные от другого аккаунта (TemurkhanFirst) вместо Baibulov.

## Решение 1: Использовать Personal Access Token (Рекомендуется)

### Шаг 1: Создайте Personal Access Token

1. Зайдите на GitHub.com и войдите в аккаунт **Baibulov**
2. Перейдите: **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
3. Нажмите **"Generate new token"** → **"Generate new token (classic)"**
4. Название токена: `Mini-Note Token` (или любое другое)
5. Срок действия: выберите нужный (например, 90 дней)
6. Отметьте галочкой: **`repo`** (полный доступ к репозиториям)
7. Нажмите **"Generate token"**
8. **ВАЖНО:** Скопируйте токен сразу! Он больше не будет показан!

### Шаг 2: Загрузите проект с использованием токена

Выполните команду push. Когда Git попросит пароль, используйте токен вместо пароля:

```powershell
git push -u origin main
```

Когда Git попросит:
- **Username:** `Baibulov`
- **Password:** вставьте скопированный токен (НЕ пароль от GitHub!)

---

## Решение 2: Очистить старые учетные данные Windows

### Шаг 1: Откройте Credential Manager

1. Нажмите `Win + R`
2. Введите: `control /name Microsoft.CredentialManager`
3. Нажмите Enter

### Шаг 2: Удалите старые GitHub credentials

1. Перейдите на вкладку **"Windows Credentials"**
2. Найдите записи типа `git:https://github.com` или `github.com`
3. Нажмите на запись и выберите **"Удалить"**

### Шаг 3: Повторите push

После удаления выполните:

```powershell
git push -u origin main
```

Теперь Git попросит новые учетные данные. Используйте:
- **Username:** `Baibulov`
- **Password:** Personal Access Token (из Решения 1)

---

## Решение 3: Использовать SSH вместо HTTPS

Если у вас настроен SSH ключ для GitHub:

### Шаг 1: Измените remote URL на SSH

```powershell
git remote set-url origin git@github.com:Baibulov/Mini-Note.git
```

### Шаг 2: Выполните push

```powershell
git push -u origin main
```

---

## Какой вариант выбрать?

- **Вариант 1** - самый простой и безопасный для начала
- **Вариант 2** - если хотите очистить старые настройки
- **Вариант 3** - если у вас уже настроен SSH ключ

