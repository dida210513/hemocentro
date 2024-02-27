# Generated by Django 5.0.1 on 2024-02-23 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hemocentro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        choices=[
                            ("FUNDAÇÃO PRÓ-SANGUE", "FUNDAÇÃO PRÓ-SANGUE"),
                            ("UNIFESP", "UNIFESP"),
                            ("SANTA CASA", "SANTA CASA"),
                            ("COLSAN", "COLSAN"),
                            ("UNICAMP", "UNICAMP"),
                            ("RIBEIRÃO PRETO", "RIBEIRÃO PRETO"),
                            ("SÃO JOSÉ DO RIO PRETO", "SÃO JOSÉ DO RIO PRETO"),
                            ("MARILIA", "MARILIA"),
                            ("BOTUCATU", "BOTUCATU"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EstoqueSangue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_sanguineo",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                        ],
                        max_length=3,
                    ),
                ),
                ("estoque_atual", models.IntegerField()),
                ("estoque_minimo_seguranca", models.IntegerField()),
                (
                    "hemocentro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="estoque.hemocentro",
                    ),
                ),
            ],
        ),
    ]