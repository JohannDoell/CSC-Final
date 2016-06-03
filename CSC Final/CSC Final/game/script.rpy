# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bg schoolentrance = "TheSchool.jpg"
image bg cafeteriafront = "cafeteriafront.jpg"

# Declare characters used by this game.
define ash = Character('Ashley', color="#ffffff")
define jul = Character('Julia', color="#9900cc")
define dyl = Character('Dylan', color="#336600")
define ken = Character('Kendra', color="#cc0066")
define nat = Character('Natalya', color="#800000")
define har = Character('Haruka', color="#0033cc")


# The game starts here.
label start:

    show bg schoolentrance
    with dissolve

    ash "Oh boy. It's a beautiful day here at Harriet Tubman Academy in Lubbock Texas!"
    ash "..."
    ash "Why am I being so oddly specific? Oh, well."
    ash "Ahh, listen to the birds chirp. Look at the sun shine. Smell the beautiful roses."
    ash "Hey! I don’t even have a nose! Who drew me?"
    ash "Ahh... That's better."
    
    ash "Oh. That boy looks pretty cute."
    
    "Cute Boy" "..."
    
    ash "(Oops, did I say that out loud?)"
    
    menu:
        ash "(What do I do?)"
        
        "Flirt":
            ash "Oh, hi there! I'm Ashley. What's your name?"
            
            "Cute Boy" "Uh..."
            "Cute Boy" "I'm Dylan."
            
            ash "Oh, Dylan! That's a cute name!"
            
            dyl "All right. If you say so..."
            
            "???" "Hey! Get away from my boyfriend!"
            
            ash "(Boyfriend? Uh oh.)"
            
            "Girl" "Who do you think you are?"
            "Girl" "It took me half of grade eleven to get Dylan to ask me out!"
                                                                                
            ash "Oh, I'm sorry. I didn't mean-"
            
            "Girl" "Come on, Dylan! Let's go inside!"
        "Play it off cool":
            ash "Uh! I have a medical condition in which things I say are mistaken for... uh... compliments."
            "Cute Boy" "..."
            "Cute Boy" "So does that mean I don't take it as a compliment?"
            ash "Umm..."
            ash "No?"
            "Cute Boy" "No, what?"
            ash "Uh. No. You shouldn't not take it as not a non-compliment."
            "Cute Boy" "Uh..."
            "Girl" "Dylan!"
            "Girl" "There you are! I've been looking for you!"
            dyl "I should go..."
            dyl "Before I go... What's your name?"
            ash "Oh. I'm... Ashley."
            dyl "Nice to meet you."
            ash "Okay. Bye!"
    
    ash "(I didn't know he had a girlfriend.)"
    ash "(That girl seems cool, though. Maybe she can be my first friend here at Harriet Tubman Academy in Lubbock, Texas.)"
    ash "(...)"
    ash "(I should stop.)"
                 
    show bg cafeteriafront
    with dissolve

    ash "Hey, this place looks pretty white for Harriet Tubman Academy in Lubbock, Texas."
    ash "…"
    ash "Oh well, at least they sell burgers."
    "???" "Ohayou!"
    ash "What."
    "???" "Konichiwa! I’d like to get the special!"
    "Lunch Lady" "Comin’ right up, sweetie."
    "???" "Arigato!"
    ash "Hey, I thought this was an American school."
    "???" "Eeeehhhh? But it is, senpai!"
    "???" "It’s an American and Japanese school!"
    ash "What."
    "???" "Haruka, why are you annoying our new comrade?"
    har "S-senpai! Gomenasai!"
    ash "…"
    ash "WHAT."
    "???" "I apologize for my… friend’s behaviour, comrade."
    "???" "I am Lieutenant Natalya Ivanovich."
    ash "…"
    ash "HOW?"
    nat "I see you are experiencing breakdown, comrade."
    nat "Come, sit with us at table."
    ash "Uh… Alright."

                 
                 
                 
                 
                 
    return
