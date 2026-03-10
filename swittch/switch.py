mode=input("enter phone mode (silent/vibrate/loud/do not distrub) ")
match mode:
    case "silent":
        print("notification")
        
    case "vibrate":
        print("sound")
    case "loud":
        print("speed")
         