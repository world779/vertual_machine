# https://repl.it/join/nokbkffy-shotakitazawa

asm = input()
asm_list = asm.split(" ")
##print(asm_list)
m = int(asm_list[-1])
as_list = asm_list[0:-1]

mylist = []

for i in as_list:
  a = int(i.split(":")[0])
  s = i.split(":")[1]
  mylist.append([a, s])

result = []
for j in mylist:
  a = j[0]

  if m % a == 0:
    result.append(j)

#素数判定関数
def is_prime(num):
  if num<=1:
    return False
  for i in range(2, num):  # 第二引数は sqrt(num)+1 でも良い
    if num % i == 0:
      return False

  return True

# mを割り切るa[i]がない場合
if len(result) == 0:
  # mの素数判定
  if is_prime(m):
    print("prime")
  else:
    print(m)
else:
  result.sort(key=lambda x: x[0])
  # print(result)
  for a,s in result:
    print(s ,end ="")
  print()

# https://note.nkmk.me/python-list-2d-sort/
# 引数keyに無名関数（ラムダ式）を指定
