1. - False Mounted hook이다.
   - True
   - False  브라우저 내부에서 돌아가고있다.
2. Vue Router에서 설정하는 history 

3. created, mounted만 발생
4. undated는 ?가 없어서 발생하지않는다.

11일 전날 홈워크

computed와 watch 의 차이

​	computed는 어떤 값을 구하기 위해

​	watch는 data를 감시해서 변경되면 어떤행동을 하기위해 작성.



12일짜 홈워크

1 .  F (부모에서 자식)으로 단방향이다.

2. 반대 데이터와 이벤트가 반대로됐다.



2. 

### [단방향 데이터 흐름](https://kr.vuejs.org/v2/guide/components.html#단방향-데이터-흐름)

모든 props는 하위 속성과 상위 속성 사이의 **단방향** 바인딩을 형성합니다. 상위 속성이 업데이트되면 하위로 흐르게 되지만 그 반대는 안됩니다. 이렇게하면 하위 컴포넌트가 실수로 부모의 상태를 변경하여 앱의 데이터 흐름을 추론하기 더 어렵게 만드는 것을 **방지할 수** 있습니다.

일반적으로 prop을 변경시키고 싶은 유혹을 불러 일으킬 수있는 두 가지 경우가 있습니다.

1. 이 prop는 초기 값을 전달 하는데만 사용되며 하위 컴포넌트는 이후에 이를 로컬 데이터 속성으로 사용하기만 합니다.
2. prop는 변경되어야 할 원시 값으로 전달됩니다.

3.

  this.$emit

@addTodo=onAddTodo

onAddTodo(text){

console.log(text)

}

iframe을 videodetail에다가

리스트중에서 선택한 video가 밑에 떠야합니다.

추가데이터 설정

selectedVideo : 

videoItem이 클릭되면

최종적으로 선택해달라고 요청!(이벤트를 전파)

 클릭되면! selectedVideo가 설정된다.





videoItem : 클릭되면

1. videoList에 이벤트 전달하면서 어떤 video선택했는지 알려줌
2. videoList는 전달받은 video정보를 App에 이벤트 전파하면서 알려줌
3. APP은 이벤트 전달받으면 해당 video를 selectedVideo에 할당
4. selectedVideo가 VideoDetail로 감
5. VideoDetail에서는 받은 selected Video를 활용해서 iframe 만들어줌!
6. 





LIFE CYCLE HOOKS

맨 처음에 고양이가 나오게하려면?

사용한다/



크게 4가지가 있다.