# Serializers


## Serializing objects

<a href = "https://www.django-rest-framework.org/api-guide/serializers/#serializing-objects">詳細參考官方說明</a>
建立一個object
```python 
from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
```
建立一個serializer

```python 
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

We can now use CommentSerializer to serialize a comment, or list of comments. Again, using the Serializer class looks a lot like using a Form class.
```python 
serializer = CommentSerializer(comment)
serializer.data
```

如果剛好是django 模型,就可以使用下列方法

```python 
class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    starter = serializers.StringRelatedField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):    
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()       
        return instance
```

```
serializer = TopicSerializer(data=data)

# .save() will update the existing `comment` instance.
serializer = TopicSerializer(topic, data=data)
```

```
serializer.save(owner=request.user)
```

自訂validate field

```python 
class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    starter = serializers.StringRelatedField()

    def validate_title(self, value):
        """
        Check subject is capitalize.
        """
        if value.capitalize() != value :
            raise serializers.ValidationError("Subject need to Capitalize")
        return value
```
自訂validate

```python 
    def validate(self, data):
        """
        Check subject is capitalize.
        """
        if data['subject'].capitalize() != data['subject'] :
            raise serializers.ValidationError("Subject need to Capitalize")
        return data        
```


## ModelSerializers
ModelSerializer與Serializer類相同，除了：
<ul>
    <li>根據model自動生成fields</li>
    <li>它將自動為序列化器生成驗證器，例如unique_together驗證器。</li>
    <li>自動實現create()和update()</li>
</ul>

```python 
class TopicSerializer(serializers.ModelSerializer):  
    days_since_create = serializers.SerializerMethodField()
    subject = ToCapitalizeCaseCharField()
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts'] 
```




