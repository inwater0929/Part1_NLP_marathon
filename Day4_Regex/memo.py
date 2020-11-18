# %%
###使用前章節的電子郵件配對為例###
import re
# 欲配對文本
# 這裡我們新增一個email address
txt = "SaveTheWorld@hotmail.com \n foobar@gmail.com \n zzzGroup@yahoo.com"
pattern = r".*@(?!gmail)\w+\.com"  # 這裡使用原始字串作為配對
print('\n----re.compile----')
# 建立模式對象
pattern_obj = re.compile(pattern=r"(.*)@(?!gmail)\w+\.com")
# 進行配對(請注意這裡是使用pattern.search配對)
x1 = pattern_obj.search(txt)
print(x1.group())
# 進行配對
print('\n----re.search----')
match = re.search(pattern, txt)
print(type(match))  # 顯示為re.Match 物件實例
print(match)
# 使用.start(), .end()返回配對的起點與終點
print(f'Match start: {match.start()}; Match end: {match.end()}')
print(f'Match text: {match.group()}')  # 使用.group() or .group(0)返回配對的字串
# 可以由返回的結果發現, re.search()只返回第一個配對的對象, 最後一個email address也符合配對但沒有返回
# 若開頭無法配對成功，即返回None
print('\n----re.match----')
match = re.match(pattern, txt)
print(match)
print('\n----re.findall----')
match = re.findall(pattern, txt)
print(type(match))  # list 物件實力
print(match)
###使用前章節的電子郵件配對為例###
# 進行配對
print('\n----re.sub----')
match = re.sub(pattern, 'REPLACE', txt, count=0)
print(match)  # 配對到的email都修改為REPLACE
# %%
