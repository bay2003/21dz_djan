# from django.core.management.base import BaseCommand
# from newapp.models import User, Payment
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         name_user = User.objects.all()
#         print(name_user)
#         print("Filling database")
#         for item in name_user:
#             print(item.id, item.name, item.area)
#             print(type(item))
#
#         print('TND')
#
#
#         name_user1 = User.objects.get()
#         print(name_user1)
#         print(type(name_user1))

# from django.core.management.base import BaseCommand
# from newapp.models import User, Payment
# import json
#
# class Command(BaseCommand):
#     help = 'Load users from JSON file into the database'
#
#     def handle(self, *args, **options):
#         # Путь к вашему файлу JSON
#         file_path = 'C:/Users/nirva/PycharmProjects/djas/djanjo 1/newproj/users_payments.json'
#
#         # Загрузка данных из файла с указанием кодировки UTF-8
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#
#         # Заполнение базы данных пользователями и платежами
#         for item in data:
#             user, created = User.objects.get_or_create(
#                 id=item['ID'],
#                 name=item['name user'],
#                 area=item['area']
#             )
#             if created:
#                 print(f'User {user.name} created')
#             else:
#                 print(f'User {user.name} already exists')
#
#             # Обработка списка платежей
#             for payment_data in item['payments']:
#                 payment = Payment(
#                     user=user,
#                     date=payment_data.get('data', None),  # Если дата отсутствует, сохраняем None
#                     purpose=payment_data.get('purpose of payment', ''),
#                     amount=payment_data.get('the amount', '0')
#                 )
#                 payment.save()
#                 print(f'Payment for user {user.name} created')
#
#         print('Database filling completed.')
#
from django.core.management.base import BaseCommand
from newapp.models import User, Payment
import json

class Command(BaseCommand):
    help = 'Fill the database with data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)

        for user_data in data:
            uchastok = user_data['uchastok']
            Vladelec = user_data['vladelec']
            area = user_data['area']

            user, created = User.objects.get_or_create(uchastok=uchastok)
            user.Vladelec = Vladelec
            user.area = area
            user.save()

            for payment_data in user_data['payments']:
                Payment.objects.create(
                    user=user,
                    date=payment_data['data'],
                    purpose=payment_data['purpose of payment'],
                    amount=payment_data['the amount']
                )

        self.stdout.write(self.style.SUCCESS('Successfully filled the database'))



# python manage.py fill_db users_payments.json