안녕하세요 발표자 신민호입니다.

저번 시간에 말씀해주신 피드백을 토대로 다시한번 앱구성을 디테일하게 해보았습니다.

 발표는 근무자어플리케이션 > 관리자 어플리케이션 순으로 하겠습니다.

근무자 어플리케이션입니다.

근무자는 앱을 활용하여 두가지의 행동이 가능합니다.

첫번째는 체크시트 작성, 두번째는 인수인계입니다.

체크시트 작성은 기존의 앱에서 작성하시던 시트를 그대로 가져오되,  지난 점검자의 위치와 현재 작성하는 점검자의 현재위치를 표시하는 기능을 추가했습니다.  작성중에는 현재위치가 보이지 않다가 

작성을 다하고 마지막에 업로드 버튼을 누르면 모달이 뜨고 그 모달에는 현재 연결된 비콘을 나타내주며 사용자가 현재 위치의 비콘을 선택함으로써 현재위치를 넣는 식입니다.



다음은 인수인계입니다.

인수인계는 설비에 특이사항을 후번 근무자나 접근한 다른 관리자에게 알려주기위한 기능입니다.  근무자가 특이사항을 발견하고 이를 전파하고 싶다면,  인수인계를 클릭하고 스캔된 비콘을 클릭하여 메시지를 기입하고 서버로 보내면 다음 근무자에게 푸쉬알람으로 메시지를 띄어주는 기능입니다. 

모니터링에서 필요한 것

request  :

​	 get( "monitoring/beacon/" ) 



response.data : 

 [

beacon 1  = {

beacon_Id == 0, beacon_Name = '' , beacon_moisture = 0% , beacon_temperatiure= 0℃ , beacon_workerList = list , 추후 비콘 배터리 = 0  

}





제이쿼리는 프로미스를 사용할 수 있게 **Deferred**라는 객체를 제공합니다. 이 객체를 사용하면 일반 코드도 프로미스처럼 사용할 수 있습니다.

```js
this.ele = document.getElementById('myViewElement');
this.$ele = $('#myViewElement');

$('#myViewElement') == $(this.ele);
```

**$el**`view.$el`
A cached jQuery object for the view's element. A handy reference instead of re-wrapping the DOM element all the time.

```
view.$el.show();

listView.$el.append(itemView.el);
```

**setElement**`view.setElement(element)`
If you'd like to apply a Backbone view to a different DOM element, use **setElement**, which will also create the cached `$el` reference and move the view's delegated events from the old element to the new one.

Access-Control-Allow-Origin:*