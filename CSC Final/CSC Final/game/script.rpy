# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bg schoolentrance = "TheSchool.jpg"
image bg cafeteriafront = "cafeteriafront.jpg"
image bg bedroom = "bedroom.jpg"
image bg mall = "mall.jpg"
image bg dresses = "dressshop.jpg"
image bg japaneseroom = "japaneseroom.jpg"
image bg calculusroom = "calculusroom.jpg"
image bg clownroom = "clownroom.jpg"
image bg stairs = "stairs.jpg"
image bg artroom = "artroom.png"
image bg party = "party.jpg"

# Declare characters used by this game.
define ash = Character('Ashley', color="#ffffff")
define jul = Character('Julia', color="#9900cc")
define dyl = Character('Dylan', color="#336600")
define ken = Character('Kendra', color="#cc0066")
define nat = Character('Natalya', color="#800000")
define har = Character('Haruka', color="#0033cc")


# The game starts here.
label start:

    $ route_points = 0

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
            $ route_points -= 1
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

    nat "These are comrades-"
    "???" "I can introduce myself! I’m Julia."
    dyl "I-"
    jul "And this is my boyfriend, Dylan."
    jul "Aren’t you that girl that was hitting on my boyfriend?"
    ash "Uh...No, no, it was nothing like that."
    "???" "I’m Kendra, by the way."
    jul "No one cares, Kendra!"
    "Everyone" "…"
    ash "(Maybe I should introduce myself?)"

    menu:
        ash "(Maybe I should introduce myself?)"
        
        "Introduce yourself.":
            $ route_points += 1
            ash "Well, I’m Ashley!"
            jul "You’re going to fit in just great!"
            ash "Thanks, Julia…"
        "Don’t introduce yourself.":
            "Everyone" "..."
            "Everyone" "... ... "
            "Everyone" "... ... ..."
            dyl "Her name is Ashley."
            ken "Neato."
            "Everyone" "..."
            "Everyone" "... ..."
            "Everyone" "... ... ..."

    jul "Alright, Dylan, let’s go!"
    dyl "Oka-"
    ken "So, Ashley, do you want to join us for shopping later today?"
    har "Please join us, senpai!"
    nat "Yes, comrade. Join the revolution."
    ash "What."
    nat "I mean, join us shopping…"
    nat "Comrade."
    ash "Sure…"
    ken "Sounds great!"

label shopping:

    show bg bedroom
    with dissolve

    ash "Boy oh boy, it sure is a nice Monday evening. Here in Lubbock, Texas."
    "???" "Honk honk."
    "???" "Get in loser, we’re going shopping!"
    ash "(Haven’t I heard that before?)"
    ash "(I mean what.)"

    har "Honk honk, senpai!"
    nat "Honk honk… comrade."
    ken "Uh… honk honk."
    jul "Just get in the car already."
    ash "What."
    ash "I mean, okay."
    "Everyone" "..."
    jul "Come on, let’s go already!"

    show bg mall
    with dissolve

    jul "Okay, girls, let’s go!"
    nat "Where to first, comrade?"
    ken "Why not Victoria’s Secret?"
    "Everyone" "No."
    har "Why not the anime store?"
    "Everyone" "No!"
    nat "Why not officially sanctioned firearms manufacturer?"
    "Everyone" "NO!"
    ash "Let’s go check out the dresses."
    jul "Slay, girl. Slay."
    ash "…"
    ash "Is that a good thing?"
    jul "Duh."
    nat "Da."

    show bg dresses
    with dissolve

    jul "Isn’t this dress I got, like, great?!"
    ken "Sure."
    har "No."
    jul "..."
    har "I mean… "
    har "Of course, senpai!"
    nat "Nice catch."
    jul "Oh em gee, this dress is so fetch!"
    har "..."
    har "Senpai,  that’s just an octopus."
    jul "I know, right?"
    "Everyone" "…"
    ash "(Should I compliment her dress?)"

    menu:
            ash "Compliment her dress?"

            "Sure.":
                $ route_points += 1
                ash "I think it’s a great looking dress!"
                jul "Thank you so much, girl!"
                jul "See, everyone? That’s a real friend, right there. Take notes."
                ash "(Why is she wearing an octopus??)"
            "No!":
                $ route_points -= 1
                ash "I think that’s a pretty stupid looking dress."
                jul "What!?"
                ash "Like. It’s an octopus."
                jul "…"
                ash "You are literally wearing an octopus."
                ash "Like, it’s a living octopus."
                "Octopus" "Squish squish."
                jul "Am I the only one here who understands true fashion?"

    har "Well, as long as you don’t wear that to your party."
    ash "Party?"
    jul "Oh, Haruka!"
    jul "Well, it was supposed to be a secret, but I guess I’ll tell you."
    jul "I’m having a party on Friday night."

    if route_points == 2:
        jul "You should come! It’ll be a lot of fun!"
        ash "Oh my gosh, thank you so much!"
        jul "Anytime!"

    if route_points == 1:
        jul "You seem like a cool person, but I don’t know you that well…"
        jul "If you can prove you’re worthy during this week, then you can come!"
        ash "Uh...okay!"
        ash "(What exactly does she mean by 'worthy'?)"

    if route_points == 0:
        jul "I don’t know if we’re really that close, though. Maybe you shouldn’t come."
        ash "Oh. Fair enough."
        jul "But hey, shopping!"

    if route_points == -1:
        jul "But after spending just one day with you, I have to say…"
        jul "You’re the worst friend I’ve ever had!"
        ash "Oh…"
        nat "Comrade, please don’t be so rude…"
        jul "No! I’ve had it with this girl! She’s so arrogant!"
        ash "Well, I mean, at least I’m not wearing an octopus…"
        jul "Ugh!"
        nat "Well, I guess this is farewell comrade."
        har "Bye-bye, senpai!"
        ken "Uh… Bye."
        ash "..."
        ash "Welp. That happened."

    if route_points == -2:
        jul "Too bad you won’t be alive to make it."
        ash "What??"
        ash "OH GOD WHAT."
        play sound "gunshot.mp3"
        har "SENPAIIIII!!!"
        nat "COMRAAAAADE!!!"
        jul "Good riddance."
        ken "..."
        ken "Oh."
        ken "Bye then."
        jump end

label classes:

    show bg japaneseroom
    with dissolve

    "Neko-sensei" "Good morning, nyan. Welcome to Japanese History."
    ash "What."
    "Neko-sensei" "I said, WELCOME TO JAPANESE HISTORY."
    ash "Why are we learning this?"
    nat "Comrade, we must learn about beautiful relationship between Russia and Japan."
    nat "Like where glorious Russian Empire destroyed the Imperial Japanese forces in 1904."
    har "What about the Russo-Japanese war-"
    nat "Anyways, comrade! Understanding the history of different cultures is important!"
    ash "But why is our teacher a cat?"
    har "Senpai! That’s racist!"
    ash "(What is this place…)"

    show bg calculusroom
    with dissolve

    "Tako-sensei" "Good morning, squish squish. Welcome to Calculus 30!"
    ash "WHY IS OUR TEACHER AN OCTOPUS."
    ken "I dunno."
    jul "DON’T QUESTION THE GREAT TAKO-SENSEI."
    ash "I hate this school."

    show bg clownroom
    with dissolve

    ash "Oh, thank God. We finally have a human teacher."
    "Sensei-sensei" "Hello, class! Welcome to Advanced Clown Car Repair!"
    ash "WHY ARE WE LEARNING THIS?"
    dyl "What if your clown car breaks down?"
    ash "WHY WOULD I HAVE A CLOWN CAR?"
    dyl "Why wouldn’t you have one?"
    ash "WHAT THE-"
    ash "WHY."
    ash "JUST WHY."
    "Sensei-sensei" "And this is your typical clown car."
    ash "WHY?"
    "Sensei-sensei" "Now, if your clown car breaks down, you’re going to need to know exactly what to do."
    "Sensei-sensei" "So listen carefully! There will be a test on this next Monday."
    ash "WHAT?"
    "Sensei-sensei" "The first step is to open up the hood here…"
    ash "(Ugh………)"

    show bg cafeteriafront
    with dissolve

    nat "COMRADE! COME AND DRINK VODKA WITH US."
    ash "WHY. IS THERE VODKA. AT A HIGH SCHOOL"
    nat "Comrade. You have been yelling for the last three periods."
    ash "WHAT THE FRICKEDY FRACK IS THIS SCHOOL."
    har "Senpai… please stop. You are doing me a frighten."
    ash "..."
    jul "Ashley, you need to, like, chill out."
    "Everyone" "…"
    nat "I am going to step out for a second."
    har "Wait for me, senpai!"
    "Everyone" "..."
    "Everyone" "... ..."
    "Everyone" "... ... ..."
    ash "(This is boring…)"
    jul "So, nice weather we’re having...?"
    jul "Am I right, ladies?"
    "Everyone" "..."
    "Everyone" "... ..."
    "Everyone" "... ... ..."

label painting:

    ash "I’m gonna head to class now."
    jul "Bye, girlfriend!"
    ken "Uh... bye."

    show bg stairs
    with dissolve

    nat "Oh my goodness, you are so beautiful."
    nat "Beautiful like glorious Russian battle tank."
    nat "But Japanese girl."
    har "T-thank you, senpai."
    ash "(Is that...Natalya and Haruka?)"
    nat "A little bit to the left...Yes, that is perfect!"
    ash "(Oh god what could they be doing?)"
    ash "Peeeeeek."

    show bg artroom
    with dissolve

    ash "Oh. You guys are just painting."
    nat "Comrade! You should not be here!"
    ash "Why? You guys are just painting!"
    nat "It is dishonourable for soldier to paint in homeland!"
    nat "You must not tell anyone! Especially not Comrade Putin!"
    ash "It’s not that bad… It’s not like you were making out or anything."
    nat "No, no. We finished that fifteen minutes ago."
    ash "What."
    har "S-senpai!"
    nat "Oh yes. She is girlfriend."
    ash "What."
    nat "What."
    har "What."
    ash "I’m so done with this school."
    "Everyone" "..."
    har "You won’t tell anyone, will you senpai?"
    ash "Uuuuhhhhh... no?"
    nat "Good, good."
    har "You’re the best, senpai!"
    nat "Now, if you will excuse, I get on with painting."

    menu:
        "Skip to Thursday.":
            "On we go!"
        "Don’t.":
            "Too bad."

label thursday:

    show bg cafeteriafront
    with dissolve

    ash "Wow. I can’t believe it’s Thursday already. It felt like time instantaneously jumped from Monday’s lunch to now."
    ash" Huh."
    jul "What were Natalya and Haruka doing!?"
    ash "Whatdya mean?"
    jul "I know you caught them doing something, what were they doing?"

    menu:
        "Tell the truth.":
            ash "They were painting."
            nat "WHAT."
            ash "How did you get here so suddenly?"
            nat "Glorious Russian battle tactics!"
            nat "Now face full power of Russian Federation!"
            ash "WHAT IS THIS PLACE?"
            play sound "gunshot.mp3"
            "Bang."
            jump end
        "Don’t tell.":
            ash "Nothing happened."
            jul "Lol ok."

label party:

    show bg party
    with dissolve

    ash "How did I get here."
    ash "How lazy are the writers?"
    dyl "Wut."
    jul "Woo party!"
    har "Party, senpai!"
    nat "We must party like is 1917."
    ash "That’s a nice boyfriend ya got there."
    ash "Would be a shame if something were to happen to him."
    jul "Wut."
    ash "I’m stealing your boyfriend."
    jul "stabby stab"
    ash "Oh noes I is a ded."
    jump end

label end:

    "Oh no, it looks like you died."
    "Maybe you could try something else and not die?"
    "Who knows?"


return
