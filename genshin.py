import tkinter as tk

baseMatrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
flag = False
result = []

warning2 = "Paimon's getting impatient!"
warning = "Why are you spamming all the time >_<"
moaning = "The answer is down here, traveller"
food = "Paimon is not food, traveller!"
jerk = "You're such a jerk"

# Generator
def checkMagicSqr(mat, size):
    sum = size*(size**2+1)/2
    flag = False
    diagVal_1 = 0
    diagVal_2 = 0
    for i in range(3):
        if (mat[i][0] + mat[i][1] + mat[i][2] == sum and mat[0][i] + mat[1][i] + mat[2][i] == sum):
            flag = True
        else:
            return False
        diagVal_1 += mat[i][i]
        diagVal_2 += mat[i][2-i]
    if (diagVal_1 == sum and diagVal_2 == sum):
        return flag
    else:
        return False

def genMatrix(mat, ind):
    if (ind == len(mat) - 1):
        finalMat = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(mat[j + 3*i])
            finalMat.append(temp)
        if checkMagicSqr(finalMat, 3):
            print(finalMat)
            result.append(finalMat)     
    else:
        for i in range(ind, len(mat)):
            mat[i], mat[ind] = mat[ind], mat[i]
            genMatrix(mat, ind+1)
            mat[i], mat[ind] = mat[ind], mat[i]
# GUI 
def getEntry():
    if (sqrSize.get() == "3"):
        print(sqrSize.get())
    else:
        print("\"You're such a jerk\" - said Paimon")
    
def clickNumber():
    global count
    global paimonSaid
    
    if (count < 3):
        if (sqrSize.get() == "3"):  
            if count == 0:
                paimonSaid = tk.Label(text = moaning)
            else:
                paimonSaid.pack_forget()
                paimonSaid = tk.Label(text = moaning)
        else:
            if count == 0:
                paimonSaid = tk.Label(text = jerk)
            else:
                paimonSaid.pack_forget()
                paimonSaid = tk.Label(text = jerk)
        paimonSaid.pack() 
        count += 1   
    

    else:
        if (sqrSize.get() == "3"):  
            paimonSaid.pack_forget()
            paimonSaid = tk.Label(text = warning)
        else:
            paimonSaid.pack_forget()
            paimonSaid = tk.Label(text = warning2)
        paimonSaid.pack() 
        count += 1
        count += 1

    numberEntry.delete(0, tk.END)

genMatrix(baseMatrix, 0)

screen = tk.Tk()
screen.geometry("600x600+200+100")
screen.title("Inazuma's quest")

sqrSize = tk.StringVar(value="")

title = tk.Label(text="Hello Traveller", font=("Calibri", 28))
subLabel = tk.Label(
    text="It's 3x3 so don't even think about entering a different thing\n (Please, just put 3 in the box below here)")
numberEntry = tk.Entry(screen, textvariable = sqrSize, width=30)
submitBtn = tk.Button(screen, text="Submit", command = lambda:[clickNumber(), getEntry()])

title.pack()
subLabel.pack()
numberEntry.pack()
submitBtn.pack()

screen.mainloop()