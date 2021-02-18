# Relationships
 

## StringRelatedField
­×§ïTopicSerializer

```
class TopicSerializer(serializers.ModelSerializer):
    #posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```

¨Ã­×§ïmodels Post __str__

```
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.message
```



## PrimaryKeyRelatedField
```
posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```

## HyperlinkedRelatedField
```   
posts = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='post-detail')    
```    