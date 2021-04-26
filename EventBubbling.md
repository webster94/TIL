오늘 공부한 내용



- StopPropagation
- PreventDefault
- Event Bubbling

StopPropagation , preventDefault의 차이

StopProPagation은 

브라우저의 이벤트 전달방식이 하위요소에서 상위요소로 이벤트를 전달하는 방식을 갖고 있는데 여기에서 이벤트 전달을 원하지 않고 해당 요소에서만 이벤트를 발생시키도록 하기 위해 사용하는 함수

- 여기에 왜 이벤트는 하위요소에서 상위요소로 이벤트를 전달 시킬까?
  - 브라우저는 이벤트 버블링이라는 이벤트 전달방식을 갖고 있고 하위요소 이벤트를 상위요소로 전달하기 때문임. 이와 반대되는 개념이 이벤트 capture임.



PreventDefault는 form에서 Input이나 어떤 도구들이 이벤트를 자동으로 이벤트를 막기위해 설정하는 함수 