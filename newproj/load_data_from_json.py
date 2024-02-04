import json
from newapp.models import User, Payment  # Импортируйте ваши модели

# Загрузите данные из файла
with open('users_payments.json', 'r') as file:
    data = json.load(file)
    for item in data['users']:  # Предполагаемая структура данных
        user = User(id=item['id'], name=item['name'], area=item['area'])
        user.save()

        for payment in item['payments']:
            Payment(user=user, date=payment['date'], purpose=payment['purpose'], amount=payment['amount']).save()


