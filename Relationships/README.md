# Relationships
 




## StringRelatedField
�ק�TopicSerializer

```
class TopicSerializer(serializers.ModelSerializer):    
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```

�íק�models Post __str__

```
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.message
```

���G�i�bcmd �U
```
http http://127.0.0.1:80/topic/1
```

�Ϊ̪����s�����s��http://127.0.0.1:80/topic/1<br>

�ϥ�StringRelatedField,�|�H__str__?��X

```
{
    "id": 1,
    "subject": "test_new",
    "last_updated": "2021-02-17T08:12:20.154735Z",
    "starter": 1,
    "views": 0,
    "posts": [
        "123",
        "777"
    ]
}
```


## PrimaryKeyRelatedField
```
posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```
�o��ϥ�PrimaryKeyRelatedField,�ҥHposts �|���PrimaryKey����
```
{
    "id": 1,
    "subject": "test_new",
    "last_updated": "2021-02-17T08:12:20.154735Z",
    "starter": 1,
    "views": 0,
    "posts": [
        1,
        2
    ]
}
```

## HyperlinkedRelatedField
```   
posts = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='post-detail')    
```    



## Nested
```
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']
        #fields = ['id', 'message', 'topic']


class TopicSerializer(serializers.ModelSerializer):    
    posts = PostSerializer(many=True, read_only=True)   

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```


data �榡�p�U
```
[
    {
        "id": 1,
        "last_updated": "2021-02-17T08:12:20.154735Z",
        "posts": [
            {
                "id": 1,
                "message": "123",
                "topic": 1
            },
            {
                "id": 2,
                "message": "777",
                "topic": 1
            }
        ],
        "starter": 1,
        "subject": "test_new",
        "views": 0
    },
]















