from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import New, NewCategory, CustomUser, Source
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password


class NewSerializer(ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
        depth = 1


class NewCategorySerializer(ModelSerializer):
    class Meta:
        model = NewCategory
        fields = '__all__'


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        # ...

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class NewsByCategorySerializer(ModelSerializer):
    news = serializers.SerializerMethodField('get_news')

    def get_news(self, category):
        res = New.objects.filter(category=category).order_by('-created')
        serializer = NewSerializer(instance=res, many=True)
        return serializer.data

    class Meta:
        model = NewCategory
        fields = ('id', 'category_name', 'image', 'created', 'news')