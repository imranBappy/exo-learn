import graphene
from graphene_django.types import DjangoObjectType
from .models import  Quiz
from exoplanets.models import Exoplanet
from exoplanets.schema import ExoplanetType


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz

# Queries
class QueryQuiz(graphene.ObjectType):
    quizzes = graphene.List(QuizType)
    quiz = graphene.Field(QuizType, id=graphene.Int(required=True))

    def resolve_quizzes(self, info, **kwargs):
        return Quiz.objects.all()

    def resolve_quiz(self, info, id):
        return Quiz.objects.get(pk=id)

# Mutations

class CreateQuiz(graphene.Mutation):
    class Arguments:
        exoplanet_id = graphene.Int()
        question = graphene.String()
        options = graphene.JSONString()

    quiz = graphene.Field(QuizType)
    def mutate(self, info, exoplanet_id, question, options):
        exoplanet = Exoplanet.objects.get(pk=exoplanet_id)
        quiz = Quiz(exoplanet=exoplanet, question=question, options=options)
        quiz.save()
        return CreateQuiz(quiz=quiz)

# Mutation Class
class MutationQuiz(graphene.ObjectType):
    create_quiz = CreateQuiz.Field()

# Register the Schema
schema = graphene.Schema(query=QueryQuiz, mutation=MutationQuiz)
