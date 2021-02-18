# Custom Field
這邊講如何自訂Field,主要分成有沒有關連性需分


 
```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']        

    def __str__(self):
        return self.message
        
class TopicSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```


## Commom

### SerializerMethodField



```python 
class TopicSerializer(serializers.ModelSerializer):     
    days_since_create = serializers.SerializerMethodField()
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts','days_since_create']
    def get_days_since_create(self, obj):
        return (now() - obj.last_updated).days
```

使用SerializerMethodField可以自訂Serializer的欄位

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
    ],
    "days_since_create": 0
}
```

### Using Extra class

有時候會需要自定義序列化，舉個例子，這邊不希望又多一個 property 回傳，所以這時候我們就必須自定義序列化，也就是


```
class ToCapitalizeCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.capitalize()

class TopicSerializer(serializers.ModelSerializer):       
    days_since_create = serializers.SerializerMethodField()
    subject = ToUpperCaseCharField()
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts','days_since_create']

    def get_days_since_create(self, obj):
        return (now() - obj.last_updated).days
```

與SerializerMethodField方法不同,並沒有新增Field
```
{
    "id": 1,
    "subject": "Test_new",
    "last_updated": "2021-02-17T08:12:20.154735Z",
    "starter": 1,
    "views": 0,
    "posts": [
        1,
        2
    ],
    "days_since_create": 0
}
```



## Relationships
 
```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']        

    def __str__(self):
        return self.message
        
class TopicSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```



### StringRelatedField
修改TopicSerializer,自訂posts輸出格式

```python
class TopicSerializer(serializers.ModelSerializer):    
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']
```


結果可在cmd 下
```
http http://127.0.0.1:80/topic/1
```

或者直接瀏覽器連結http://127.0.0.1:80/topic/1<br>

使用StringRelatedField,會以__str__?輸出

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


### PrimaryKeyRelatedField

```python
posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```

使用PrimaryKeyRelatedField,所以posts 會顯示PrimaryKey的值

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

### HyperlinkedRelatedField
```python
posts = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='post-detail')    
```    

HyperlinkedRelatedField,所以posts 輸出會是連結

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

### Nested
```python
    posts = PostSerializer(many=True, read_only=True)   
```

使用PostSerializer會將原本的欄位疊代進來
data 格式如下
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













