from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from .models import Feedback
from datetime import datetime
import re
from django.core.validators import validate_email

class GetFormView(View):
    # Обработчик GET-запроса
    def get(self, request):
        # Получаем все записи из базы данных
        feedbacks = Feedback.objects.all()

        # Передаем данные в шаблон
        return render(request, "form.html", {'feedbacks': feedbacks})

    def post(self, request):
        # Получаем данные из POST запроса
        form_data = request.POST

        # Определяем поля и их типы в модели
        model_fields = {
            'user_email': 'email',
            'user_phone': 'phone',
            'order_date': 'date',
            'lead_text': 'text',
        }

        # Словарь для хранения типов полей
        field_types = {}

        # Проверяем типы полей в пришедших данных
        for field_name, field_type in model_fields.items():
            if field_name in form_data:
                field_value = form_data[field_name]
                # Определяем тип значения
                if field_type == 'date':
                    try:
                        # Проверка на корректность формата даты
                        datetime.strptime(field_value, '%Y-%m-%d')
                    except ValueError:
                        field_types[field_name] = 'date'
                elif field_type == 'phone':
                    if not self.validate_phone(field_value):
                        field_types[field_name] = 'phone'
                elif field_type == 'email':
                    if not self.validate_email(field_value):
                        field_types[field_name] = 'email'
                elif field_type == 'text':
                    field_types[field_name] = 'text'

        # Проверяем наличие всех полей шаблона в пришедших данных
        if all(field in form_data for field in model_fields.keys()):
            # Сохраняем данные в базе данных
            feedback = Feedback(
                email=form_data['user_email'],
                phone=form_data['user_phone'],
                order_date=form_data['order_date'],
                message=form_data['lead_text']
            )
            feedback.save()
            return JsonResponse({"message": "Спасибо за ваше сообщение!"}, status=200)

        return JsonResponse(field_types, status=400)

    def validate_phone(self, value):
        # Валидация телефона с использованием регулярного выражения
        pattern = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
        return re.match(pattern, value) is not None

    def validate_email(self, value):
        # Валидация email
        try:
            validate_email(value)
            return True
        except:
            return False
