import streamlit as st

def taylorTest():
    st.image("images/taylor1.jpg", width=200)
    points = {
        "Red": 0,
        "1989": 0,
        "Lover":0,
        "TTPD": 0
    }
    
    st.title("What Taylor Swift Album Should You Listen To?")
    st.write("Answer the questions to see what Taylor album fits you best!")
    
    genre = st.radio( #NEW
        "**What is your favorite genre of music?**",
        ["Country", "Pop", "Alternative",]
        )

    if genre == "Country":
        points["Red"] +=1
    elif genre == "Alternative":
        points["TTPD"] += 1
    else:
        points["Lover"] += 1
        points["1989"] +=1



    lyricism = st.slider ("**How much do you value lyricism (0 is not at all and 5 is very much**)?",
        min_value=0, #NEW
        max_value=5,
        value=2
    )
    st.write(f"**On a scale of 0 to 5, you value lyricism a {lyricism}**") #NEW

    if lyricism >=4:
        points["TTPD"] +=1
    elif lyricism == 3: 
        points["Red"] +=1
    elif lyricism == 2:
        points["Lover"] +=1
    else:
        points["1989"] +=1

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("images/red.jpg", width=300)
    with col2:
        st.image("images/pink1.jpg", width=300)
    with col3:
        st.image("images/lightblue.jpg", width=300)
    with col4:
        st.image("images/gray.jpg", width=300)

    color= st.selectbox(
        "**What is your favorite color?**",
        ("Red", "Blue", "Pink", "Grey")
    )
    #NEW

    if color == "Red":
        points["Red"] +=1
    elif color == "Blue":
        points["1989"] +=1
    elif color == "Pink":
        points["Lover"] +=1
    else:
        points["TTPD"] +=1

    
    songs= st.multiselect( #NEW
        "**Which Taylor songs have you heard?**",
        ["All Too Well", "New Romantics", "Afterglow", "loml"]
    )

    if "All Too Well" in songs:
        points["Red"] +=1
    elif "New Romantics" in songs:
        points["1989"] +=1
    elif "Afterglow" in songs:
        points["Lover"] +=1
    else:
        points["TTPD"] +=1
    
    albums = st.number_input( #NEW
        "**How many Taylor Swift albums do you own?",
        min_value=0,
        max_value=15,
        step=1
    )

    if albums >= 6:
        points["TTPD"] +=1
    elif albums >= 3:
        points["Lover"] +=1
    elif albums >= 2:
        points["Red"] +=1
    else: 
        points["1989"] +=1
    winner= max(points, key=points.get)

    if st.button ("See Album!"):
        st.write("---")
        st.subheader(" Your Next Taylor Album ")
        st.write(f"Based on your responses, your perfect album is **{winner}**!!")
        albumPics = {
            "Red":"https://i.pinimg.com/1200x/ea/ae/95/eaae9592214366f5b28da3bb4800d0e2.jpg",
            "1989":"https://i.pinimg.com/1200x/8a/72/55/8a72552b934f80fc990d45887cf71db7.jpg",
            "Lover":"https://i.pinimg.com/1200x/a0/89/72/a08972f11ad0daed9a74d7058c730c26.jpg",
            "TTPD":"https://i.pinimg.com/736x/01/da/31/01da31ac870bd92d72c167db63ae4736.jpg"
        }
        st.image(albumPics[winner], caption=winner) #NEW
        st.balloons() #NEW
taylorTest()
