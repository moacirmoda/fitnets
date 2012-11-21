#! coding: utf-8
from django.test import TestCase
from models import *
from datetime import date


class SimpleTest(TestCase):

    def setUp(self):
        self.project = Project()
        self.project.objective = "Perda de Peso"
        self.project.init = date.today()
        self.project.duration = 12
        self.project.frequency = 3

        self.project.save()

    def test_new_evolution(self):

        evolution = Evolution()
        evolution.photo = "media/images/avatar.jpg"
        evolution.date = date.today()
        evolution.project = self.project

        evolution.save()

        self.assertEqual(1, 1)

    def test_new_day(self):

        day = TrainingDay()
        day.project = self.project
        day.day = "A"
        day.init = date.today()
        day.duration = 3

        day.save()

        self.assertEqual(1, 1)

    def test_new_exercise(self):

        day = TrainingDay()
        day.project = self.project
        day.day = "A"
        day.init = date.today()
        day.duration = 3

        day.save()

        exercise = TrainingExercise()
        exercise.day = day
        exercise.exercise = "Supino Reto"
        exercise.serie = 3
        exercise.repetition = 12

        self.assertEqual(1, 1)

    def test_new_meal(self):

        meal = Meal()
        meal.project = self.project
        meal.meal = "1ª"
        meal.save()

        food = Food()
        food.meal = meal
        food.food = "Maça"
        food.save()

        food = Food()
        food.meal = meal
        food.food = "Leite"
        food.save()

        food = Food()
        food.meal = meal
        food.food = "Ovos"
        food.save()

        self.assertEqual(1, 1)

    def test_new_suplement(self):

        cat = CatSuplemento()
        cat.product = "AA"
        cat.save()

        type = TypeSuplemento()
        type.title = "Proteina"
        type.save()

        suplement = Suplemento()
        suplement.project = self.project
        suplement.cat = cat
        suplement.suplement = type
        suplement.product = "Whey"
        suplement.save()

        self.assertEqual(1, 1)


    

