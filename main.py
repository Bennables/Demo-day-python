import time
import webbrowser
import tkinter as tk
from tkinter import simpledialog

#  coststr = StringVar()
root = tk.Tk() 
root.wait_visibility(root)
root.attributes('-alpha', 0.1)
root.configure(bg="black")
#root.geometry("300x200") 
money = 19032
donors = 14032
payout = 0
x=True

while x:
  choice = tk.simpledialog.askstring(title="Test", parent = root, prompt= "Would you like to 1) Take the test, or 2) Donate?")
  if choice == "1" or choice.lower().startswith("y"):
    first=[]
    last_questions_answers = []

    q1 = simpledialog.askstring(title="Test",
    prompt="Do you have a cough? (yes/no)")

    q2 = simpledialog.askstring(title="Test",
    prompt="Have you had shortness of breath or difficulty breathing? (yes/no")
    q3 = simpledialog.askstring(title="Test",
    prompt="Have you had a fever or chills? (yes/no)")


    first.append(q1)
    first.append(q2)
    first.append(q3)

    for i in range(len(first)):
      if first[i].lower().startswith("y"):
        first[i] = 1
      elif first[i].lower().startswith("n"):
        first[i] = 2

    risk = None
    if first[0] == 1 and first[1] == 1 and first[2] == 1:
      risk = "high_risk"

    elif first[0] == 2 and first[1] == 2 and first[2] == 2:
      risk = "barely"
      payout += 0.05
      money -= 0.05

    else: 
      risk = "maybe"

    if risk == "high_risk":
          next = True
    elif risk == "maybe":
      try:
        qa = simpledialog.askstring(title="Test",
        prompt="You are showing a syptom or two, would you like to take more test to help comfirm your status? (yes,no)")
        if qa.lower().startswith("y"):
          next = True
        elif qa.lower().startswith("n"):
          next = False
          payout += 0.05
          money -= 0.05 
      except Exception:
        pass
    elif risk =="barely":
      print("You aren't showing the main symptoms of the virus! Keep on doing what you're doing and stay safe!")

    if next == True:
      q4 = simpledialog.askstring(title="Test",
      prompt="Have you had any fatigue today? (yes/no)")
      q5 = simpledialog.askstring(title="Test",
      prompt="Have you had any muscle or body aches in the past 24 hours? (yes/no)")
      q6 = simpledialog.askstring(title="Test",
      prompt="Have you had any headaches today? (yes/no)")
      q7 = simpledialog.askstring(title="Test",
      prompt="Have you recently lost your sense of taste or smell? (yes/no)")
      q8 = simpledialog.askstring(title="Test",
      prompt="Have you been experiencing a sore throat lately? (yes/no)")
      q9 = simpledialog.askstring(title="Test",
      prompt="Do you have congestion or a runny nose? (yes/no)")
      q10 = simpledialog.askstring(title="Test",
      prompt="Have you had nausea today? (yes/no)")
      q11 = simpledialog.askstring(title="Test",
      prompt="Have you been vomitting today? (yes/no)")
      q12 = simpledialog.askstring(title="Test",
      prompt="Did you have diarrhea (yes/no)")
    
      last_questions_answers.append(q4)
      last_questions_answers.append(q5)
      last_questions_answers.append(q6)
      last_questions_answers.append(q7)
      last_questions_answers.append(q8)
      last_questions_answers.append(q9)
      last_questions_answers.append(q10)
      last_questions_answers.append(q11)
      last_questions_answers.append(q12)

    else:
      print("Thanks for taking this checkup today, come back tomorrow to check again!")


    counter = 0

    for i in range(len(last_questions_answers)):
      if last_questions_answers[i].lower().startswith("y"):
        counter += 1
      elif last_questions_answers[i].lower().startswith("n"):
        counter += 0

    if counter >= 5:
      print("We're almost certain that you have the virus. Please call a health professional to learn more.")
      time.sleep(2)
      print("Here are a couple things you can do to protect others around you.\n -Stay home except to get medical care.\n-Monitor your symptoms carefully. If your symptoms get worse, call your healthcare provider immediately.\n-Get rest and stay hydrated. Take over-the-counter medicines, such as acetaminophen, to help you feel better.\n-If you have a medical appointment, notify your healthcare provider ahead of time that you have or may have COVID-19.\n-Stay in a specific room and away from other people in your home. If possible, use a separate bathroom. If you must be around others, wear a mask.")
      webbrowser.open('https://www.cdc.gov/coronavirus/2019-ncov/if-you-are-sick/steps-when-sick.html')
      x = False
    elif 2<counter<5:
      print("You could possible have the virus, contact a health professional to learn more")
      time.sleep(2)
      print("Here are a couple things you can do to protect others around you.\n -Stay home except to get medical care.\n-Monitor your symptoms carefully. If your symptoms get worse, call your healthcare provider immediately.\n-Get rest and stay hydrated. Take over-the-counter medicines, such as acetaminophen, to help you feel better.\n-If you have a medical appointment, notify your healthcare provider ahead of time that you have or may have COVID-19.\n-Stay in a specific room and away from other people in your home. If possible, use a separate bathroom. If you must be around others, wear a mask.")
      webbrowser.open('https://www.cdc.gov/coronavirus/2019-ncov/if-you-are-sick/steps-when-sick.html')
      x = False
    elif 2<counter<5 and risk == "high":
      print("You probably have the virus, to confirm your status, contact a health professional.")
      time.sleep(2)
      print("Here are a couple things you can do to protect others around you.\n -Stay home except to get medical care.\n-Monitor your symptoms carefully. If your symptoms get worse, call your healthcare provider immediately.\n-Get rest and stay hydrated. Take over-the-counter medicines, such as acetaminophen, to help you feel better.\n-If you have a medical appointment, notify your healthcare provider ahead of time that you have or may have COVID-19.\n-Stay in a specific room and away from other people in your home. If possible, use a separate bathroom. If you must be around others, wear a mask.")
      webbrowser.open('https://www.cdc.gov/coronavirus/2019-ncov/if-you-are-sick/steps-when-sick.html')
      x = False

    elif counter == 1 or counter == 2 :
      print("It is possible that you have the virus. We recommend you quarantine yourself, and if possible, get tested.")
      time.sleep(2)
      print("Here are a couple things you can do to protect others around you.\n -Stay home except to get medical care.\n-Monitor your symptoms carefully. If your symptoms get worse, call your healthcare provider immediately.\n-Get rest and stay hydrated. Take over-the-counter medicines, such as acetaminophen, to help you feel better.\n-If you have a medical appointment, notify your healthcare provider ahead of time that you have or may have COVID-19.\n-Stay in a specific room and away from other people in your home. If possible, use a separate bathroom. If you must be around others, wear a mask.")
      webbrowser.open('https://www.cdc.gov/coronavirus/2019-ncov/if-you-are-sick/steps-when-sick.html')
      x = False


  elif choice == "2":
    add = simpledialog.askstring(title= "Survey",
    prompt= "How much would you like to donate")
    money += add
    donors +=1
    print(f'We thank you for your donation! Thanks to you and {donors} other donors, we have raised {money} dollars')
    
root.mainloop()






