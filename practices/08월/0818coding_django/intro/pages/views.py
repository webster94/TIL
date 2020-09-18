from django.shortcuts import render
import random
import requests
# Create your views here.
def dinner(request,menu,number):
    context = {
        'menu' : menu,
        'number' : number,

    }
    
    return render(request,'dinner.html', context)

def lotto(request):
    lotto_dict = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=903').json()
    this_week = []
    this_week.append(lotto_dict['drwtNo1'])
    this_week.append(lotto_dict['drwtNo2'])
    this_week.append(lotto_dict['drwtNo3'])
    this_week.append(lotto_dict['drwtNo4'])
    this_week.append(lotto_dict['drwtNo5'])
    this_week.append(lotto_dict['drwtNo6'])

    this_week_bonus = lotto_dict['bnusNo']
   
    numbers = range(1,46)
    key = random.sample(numbers,6)
    bonus = random.choice(numbers)
    score = [1,9,11,14,26,28]
    result2 = []
    sec = 0
    thr = 0
    for k in range(1000):
        key = random.sample(numbers,7)
        count = 0
        for j in key:
            if j in score:
                count +=1
        result2.append(count)
    fir = result2.count(6)   
    if result2.count(5) and bonus == 19:
        sec = count + 1
    elif result2.count(5) and bonus !=19:
        thr = count +1 
    fou = result2.count(4)   
    fif = result2.count(3)   
    fail = result2.count(1) + result2.count(0) + result2.count(2)   
            
             


    context = {
        'numbers' : numbers,
        'key' : key,
        'bonus' : bonus,
        'fir' : fir,
        'sec' : sec,
        'thr' : thr,
        'fir' : fir,
        'fou' : fou,
        'fif' : fif,
        'fail' : fail,
        'this_week' : this_week,
        'this_week_bonus' : this_week_bonus,
    }
    return render(request,'lotto.html',context)