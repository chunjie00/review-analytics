data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print('共有', len(data), '笔留言')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均长度为', sum_len/len(data), '字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔留言小于100')
print(new[0])

good = []
for d in data:
	if "good" in d:
		good.append(d)
print('一共有', len(good), '笔留言提到good')

bad = [d for d in data if 'bad' in d]
print('一共有', len(bad), '笔留言提到bad')