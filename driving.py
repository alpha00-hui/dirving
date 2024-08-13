driving = input ('請輸入有沒有開過車:')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise systemexit
age = input('請問你的年齡:')
age =int(age)
if driving =='有':
	if age >= 18:
		print('開車好玩嗎？')
	else:
		print('不會想體驗開車的經歷嗎？')
elif driving == '沒有':
	if age >= 18:
		print('考照年齡已達，怎麼不去考駕照呢？')
	else:
		print('加油，再過幾年即可考照囉！')