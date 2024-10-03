import graphene
import graphql_jwt
from users.schema import UserQuery, UserMutation
from quiz.schema import QueryQuiz, MutationQuiz
from exoplanets.schema import ExoQuery



class Query(UserQuery,ExoQuery,QueryQuiz, graphene.ObjectType):
    pass

class Mutation(UserMutation ,MutationQuiz, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
