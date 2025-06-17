from rest_framework import serializers 
class userDetailsSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    mobile=serializers.IntegerField()
    password=serializers.CharField(max_length=50)
    address=serializers.CharField(max_length=50)