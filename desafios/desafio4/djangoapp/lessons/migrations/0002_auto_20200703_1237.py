from django.db import migrations
from lessons.models import Lesson

initial_lessons = [
    Lesson(
        title="O universo do desenvolvimento no Mercado Livre",
        author="Daniel Ambrosio",
        description=""
    ),
    Lesson(
        title="O ecosistema de frameworks Javascript",
        author="Diego Fernandes",
        description=""
    ),
    Lesson(
        title="As grandes oportunidades  para Full Cycle Developers",
        author="Rodrigo Branas / Tiago Baeta / Robson Marques",
        description=""
    ),
    Lesson(
        title="Serverless, o mínimo que todo dev precisa saber",
        author="Erick Wendel",
        description=""
    ),
    Lesson(
        title="Produtividade eXtrema com Python e Django",
        author="Henrique Bastos",
        description=""
    ),
    Lesson(
        title="Containers na prática: do Docker ao Kubernetes",
        author="Fabricio Veronez",
        description=""
    ),
    Lesson(
        title="Microsserviços e Integração Contínua com Sunarqube",
        author="Wesley Willians",
        description=""
    ),
    Lesson(
        title="Monitoramento Inteligente + Encerramento",
        author="Wesley Willians",
        description=""
    ),
]

def insert_data_lessons(apps, schema_editor):
    for lesson in initial_lessons:
        lesson.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data_lessons)
    ]
