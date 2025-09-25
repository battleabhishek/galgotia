import re

text = "are you there"
ans=re.match(r"are", text)
print(ans)
ans2=re.match(r"you", text)
print(ans2)
ans3=re.search(r"there", text)
print(ans3)

#use search and match using text "its a good day" abd pattern1 "good" 
# pattern 2 "there"
# pattern 3 "it"
text2 = "its a good day"
ans4=re.search(r"good", text2)
print(ans4)
ans5=re.search(r"there", text2)
print(ans5)
ans6=re.match(r"it", text2)
print(ans6)
ans7=re.match(r"good", text2)
print(ans7)
ans8=re.match(r"its", text2)
print(ans8)
ans9=re.search(r"its", text2)
print(ans9)
