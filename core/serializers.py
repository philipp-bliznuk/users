from rest_framework import serializers

from .models import UserAccount, Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('name',)


class UserAccountSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)

    class Meta:
        model = UserAccount
        fields = ('name', 'surname', 'sex', 'age', 'activities')

    def create(self, validated_data):
        activities = validated_data.pop('activities')
        user = UserAccount.objects.create(**validated_data)
        for activity in activities:
            Activity.objects.create(user=user, **activity)
        return user
