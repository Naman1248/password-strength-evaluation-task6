from zxcvbn import zxcvbn

passwords = [
    "password",
    "123456",
    "admin",
    "qwerty",
    "welcome",
    "abc123",
    "password1",
    "letmein",
    "monkey",
    "dragon",
    "master",
    "sunshine",
    "MyDog2019!",
    "Coffee#Morning",
    "Summer2024",
    "Basketball99",
    "Pizza4Life!",
    "RedCar123",
    "Music@Home",
    "Winter2023!",
    "Soccer#Fan",
    "Beach4Fun",
    "Happy@Day",
    "School2024",
    "K9$mR7#nQ2@vL8pX",
    "Tr0ub4dor&3Moon!",
    "9Zx#mK8$nP2@qR5v",
    "My1stC@r!Was4BlueToyota",
    "P@ssw0rd!sN0t1234",
    "7mQ#nR9$kL2@pX5v",
    "B3st!P@ssw0rd#Ev3r",
    "X8@mK5$nQ7#pR2v",
    "Th3$un!sY3ll0w@nd8r1ght",
    "5nQ#mR8$kL9@pX3v",
    "N3v3r!G0nn@G1v3Y0uUp",
    "4mK#nQ7$pR5@vL2x",
    "correct-horse-battery-staple-47!",
    "purple-elephant-dancing-moonlight-92#",
    "coffee-mountain-bicycle-thunder-38@",
    "ocean-wizard-keyboard-rainbow-65$",
    "rocket-pizza-guitar-butterfly-19!",
    "dragon-library-sandwich-volcano-84#",
    "telescope-garden-penguin-lightning-27@",
    "castle-robot-waterfall-diamond-53$",
    "tornado-chocolate-spaceship-forest-76!",
    "phoenix-laptop-meadow-crystal-41#",
    "submarine-pancake-tornado-galaxy-98@",
    "unicorn-keyboard-sunset-adventure-15$"
]

with open("strength_results.csv","w",encoding="utf-8") as f:
    f.write("password_masked,length,score,crack_time_display,feedback\n")
    for p in passwords:
        r = zxcvbn(p)
        score = r['score']   # 0-4
        crack = r['crack_times_display'].get('offline_slow_hashing_1e4_per_second')  # example
        # mask password for CSV
        masked = p[0] + "*"*(len(p)-2) + p[-1] if len(p)>2 else "*"*len(p)
        feedback = "; ".join(r.get('feedback',{}).get('suggestions',[]) or [])
        f.write(f"{masked},{len(p)},{score},{crack},{feedback}\n")
        print(masked, score, crack, feedback)
