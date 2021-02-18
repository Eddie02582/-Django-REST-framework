# Relationships
 
```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']
        #fields = ['id', 'message', 'topic']

    def __str__(self):
        return self.message
        
class TopicSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```



## StringRelatedField
�ק�TopicSerializer,�ۭqposts��X�榡

```python
class TopicSerializer(serializers.ModelSerializer):    
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```


���G�i�bcmd �U
```
http http://127.0.0.1:80/topic/1
```

�Ϊ̪����s�����s��http://127.0.0.1:80/topic/1<br>

�ϥ�StringRelatedField,�|�H__str__?��X

```python
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

```python
posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```

�ϥ�PrimaryKeyRelatedField,�ҥHposts �|���PrimaryKey����

```python
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
```python
posts = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='post-detail')    
```    

HyperlinkedRelatedField,�ҥHposts ��X�|�O�s��

```python
{
    "id": 1,
    "subject": "test_new",
    "last_updated": "2021-02-17T08:12:20.154735Z",
    "starter": 1,
    "views": 0,
    "posts": [
        "http://127.0.0.1/post/1/",
        "http://127.0.0.1/post/2/"
    ]
}
```  

## Nested
```python
    posts = PostSerializer(many=True, read_only=True)   
```

�ϥ�PostSerializer�|�N�쥻������|�N�i��
data �榡�p�U
```python
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
```















