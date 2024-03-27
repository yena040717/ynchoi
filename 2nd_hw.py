def exchange(amount):
    coin_500=amount//500
    remain_amount=amount%500
    coin_100=remain_amount//100
    remain_amount%=100
    coin_50=remain_amount//50
    remain_amount%=50
    coin_10=remain_amount//10
    print('500원 동전의 개수:', coin_500, '개')
    print('100원 동전의 개수:', coin_100, '개')
    print('50원 동전의 개수:', coin_50, '개')
    print('10원 동전의 개수:', coin_10, '개')

    
def get_integer(prompt):
    return int(input(prompt))

amount=get_integer('동전으로 교환하고자 하는 금액은? ');exchange(amount)
