# Telegram-боты от А до Я

### Начальная настройка

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

***

### Бот с webhook на Flask

```bash
ssh -R 80:localhost:5000 localhost.run
```

#### Установка вебхука

```url
https://api.telegram.org/bot123445:mytoken/setWebhook?url=https://mysite.com:5000
```


В ответ вы должен получить такой ответ:
```json
{
  "ok":true,
  "result":true,
  "description":"Webhook was set"
}
```