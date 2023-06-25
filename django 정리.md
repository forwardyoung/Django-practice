> 인프런 작정하고 장고 강의를 들으면서 궁금한 키워드를 정리



`context_object_name` 

: Generic views를 사용할 때 사용되는 매개변수

일반적으로, Django의 Generic views는 모델에서 가져온 데이터를 템플릿에 전달하기 위해 `object_list`라는 변수 이름을 사용한다. 그러나 `context_object_name` 매개변수를 사용하여 이 변수 이름을 변경할 수 있다.



`reverse_lazy` : 클래스 기반 뷰의 `success_url` 속성에서 사용될 수 있는 함수

⚠️`reverse` 함수는 즉시 URL을 생성하여 반환하는 반면, `reverse_lazy`는 URL이 실제로 필요한 시점까지 평가를 지연시킨다.

```python
class ProfileUpdateView(Updateview):
    model = Profile
    ...
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
```





`super()` : 파이썬의 내장 함수로, 부모 클래스의 메서드를 호출하는 데 사용된다.



**`Mixin`**

Create View ➡️ No object

Detail View ➡️ No Form

- FormMixin - 다중상



`include	` : 만들고 있는 html 파일에 조그만 조각들을 가져와서 템플릿에 박아 넣는 방식

```html
{% include 'template_name.html' with variable_name=value %}
```

`template_name.html` : 포함시킬 템플의 경로

`variable_name` : 포함된 템플릿으로 전달될 변수의 이름

`value` : 해당 변수의 값

`{% include 'commentapp/create.html' with article=target_aritcle %}`



**Transaction**

좋아요의 경우 다음 두 가지가 모두 작동해야 다.

1️⃣ Create LikeRecord

2️⃣ Article like += 1



Transaction with Django decorator

`@transaction.atomic`을 통해 '하나라도 실패하면 모두 실패, 모두 성공해야 성공적 반영'하는 atomic 작업을 수행할 수 있다.



