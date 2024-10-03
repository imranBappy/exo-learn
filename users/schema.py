import graphene
from graphene_django.types import DjangoObjectType
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from graphql_jwt.decorators import login_required
from django.core.exceptions import ValidationError
from graphql import GraphQLError
import graphql_jwt


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, name, email, password):
        user = get_user_model()(
            name=name,
            email=email
        )
        try:
            validate_password(password)
            user.set_password(password)
            user.save()
            return CreateUser(user=user)
        except ValidationError as e:
            raise GraphQLError(e)

class UserQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    @login_required
    def resolve_me(self, info):
        return info.context.user

class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    # Add JWT mutations here
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


