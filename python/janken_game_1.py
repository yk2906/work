import random
hand = ["グー", "チョキ", "パー"]
print("コンピュータとじゃんけんをします。")

for i in range(3):
    print("\n", i+1, "回目のじゃんけん")
    your_action = input("あなたは何を出す？ \n0=グー \n1=チョキ \n2=パー ")
    your_action = int(your_action)
    computer_action = random.randint(0, 2)
    print("コンピュータの手は"+hand[computer_action])
    if your_action == computer_action:
        print("あいこです")
    if your_action == 0:
        if computer_action == 1:
            print("あなたの勝ち")
        if computer_action == 2:
            print("コンピュータの勝ち")
    if your_action == 1:
        if computer_action == 0:
            print("コンピュータの勝ち")
        if computer_action == 2:
            print("あなたの勝ち")
    if your_action == 2:
        if computer_action == 0:
            print("あなたの勝ち")
        if computer_action == 1:
            print("コンピュータの勝ち")
