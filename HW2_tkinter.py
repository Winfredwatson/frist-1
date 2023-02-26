from sympy.solvers import solve
from tkinter import *

# 啟動視窗系統
root = Tk()

def run():
    equations_clean=[]
    expr1 = text1.get("1.0","end")
    equations = expr1.split('\n')
    if len(equations)>0:
        for i in range(len(equations)):
            if equations[i] == '':
                continue
#             print(equations[i])
            arr = equations[i].split('=')
            if len(arr) == 2:
                equations[i] = arr[0] + '-(' + arr[1] + ')'
            equations_clean.append(equations[i])
        print(equations_clean)
        answer1.set(solve(equations_clean))        

# 畫面設計
answer1 = StringVar() 
Label(root, text="請輸入方程式：(2x 需輸入 2*x)", height=1, font='Helvetic 18 bold').pack(fill=X)
text1 = Text(root, height=5, width=30, font='Helvetic 18 bold')
text1.pack()
Button(root, text="求解", font='Helvetic 36 bold', command=run).pack(fill=X)
Label(root, text="", height=1, font='Helvetic 18 bold', textvariable=answer1).pack(fill=X)


# 監聽事件
root.mainloop()