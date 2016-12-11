from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
from tkinter import *
from tkinter import ttk

yourAPI = ""  #请在bosonnlp上注册账号，并将API秘钥填入这里

#点击myself按钮后执行以下功能
def calculate_myself(*args):
	target = usermeg.get()
	nlp = BosonNLP(yourAPI)
	res = nlp.sentiment(target,model='weibo')
	if res[0][1] > 0.5:  #消极
		sug = "---别太紧张啦，给你讲个笑话吧~\n" + "我问洗衣店老板：我的衣服什么时候能洗好？ \n老板说：3天后。\n我又问：你们不是说24小时就可以了吗？\n老板笑道：我们每天只工作8小时。^-^\n \n"
		sug += "---或许这些歌能帮助你放松~\n" + "*Run away with me\n" + "*Coming Home\n" + "*梦\n \n"
		sug += "---你的朋友小明最近在约人一起玩，或许你可以找他玩玩~"
	else:
		sug = "感觉你最近很开心呀，有什么想分享的吗？\n"
	suggest.set(sug)

#点击friend按钮后执行以下功能
def calculate_friend(*args):
	target = usermeg.get()
	nlp = BosonNLP('EXx08-nK.11068.bvMiPcp2W1jl')
	res = nlp.sentiment(target,model='weibo') 
	target = nlp.extract_keywords(target, top_k=5)
	keyword = ""
	for weight, kw in target:
		keyword = keyword + kw + "   "
	if res[0][1] > 0.5: #消极
		sug = "好友状态：\n" + str(keyword) + "\n \ntip:你的朋友最近或许有些不开心，你可以去安慰一下他嘛？\n"
	else:
		sug = "好友状态：\n" + str(keyword) + "\n \ntip:你的朋友最近有些开心事，快去问问他发生了什么吧？"
	suggest.set(sug)


#GUI设计   
root = Tk()
root.title("feeler")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

usermeg = StringVar()
suggest = StringVar()

#添加label
ttk.Label(mainframe, text="用户状态：").grid(column=1, row=1, sticky=W)
#添加输入框（单行）
feet_entry = ttk.Entry(mainframe, width=50, textvariable=usermeg)
feet_entry.grid(column=1, row=2, sticky=(W, E))

#添加label及button
ttk.Label(mainframe, text="推荐或建议").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, textvariable=suggest).grid(column=1, row=4, sticky=(W, E))
ttk.Button(mainframe, text="myself", command=calculate_myself).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text="friend", command=calculate_friend).grid(column=1, row=6, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate_myself)
root.bind('<Return>', calculate_friend)
root.mainloop()


#以下为输入示例
'''
早上起来就想掉眼泪，是真得了。
心好凉真的。自己都不知道，算算已经持续将近半年了。
我真心不想妈妈看到我这个样子！
对不起！控制不了自己的时候，真心觉得想去。。。

'''

'''
我发现我每天的心情真像一颗洋葱，一层层的剥开，
才发现里面是黑暗的，我真心的郁闷，没觉得哪里让我开心过，
我是悲哀的，悲观的，可能是我自己想不开，可不知道为什么想不开。
也只有自己知道每天的笑都是伪装的。
'''