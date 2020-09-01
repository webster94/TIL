def lotto(request):
    this_week = [1,9,11,14,26,28]
    this_week_bonus = 19

    result = {
      '1등': 0,
      '2등': 0,
      '3등': 0,
      '4등': 0,
      '5등': 0,
      '꽝': 0
    }

    for _ in range(1000):
      my_lottos = random.sample(range(1,46),6)

      for my_lotto in my_lottos:
        if my_lotto in this_week:
          count +=1

      if count ==5:
        if this_week_bonus in my_lottos:
            result = ['2등'] +=1

        else:
          result['3등'] +=1
      
      if count == 6:
        result['1등'] +=1
      
      if count == 5:
        result['4등'] +=1
      if count ==3:
        result['5등'] +=1
      if count < 3:
        result[꽝] +=1
  return render(request, 'lotto.html', result)