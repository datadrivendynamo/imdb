import streamlit as st
import pandas as pd

def gap(n):
    i = 0
    while i<n:
        st.markdown('')   
        i = i+1

st.markdown("<h3 style = 'text-align: center ; color: #F3CE13;'>Welcome to Imdb</h3", unsafe_allow_html = True)
st.markdown("<h5 style = 'text-align: center ; color: #F3CE13;'>The essential resource for entertainment industry!</h5", unsafe_allow_html = True)
c1,c2,c3 = st.columns([2,4,1])

with c1:
    st.markdown('')
    st.image('/Users/himanshutipirneni/Downloads/imdb1.png',width = 150)

with c2:    
    home = st.selectbox('',['Home','Upcoming releases','Top 100 movies on IMDB','Movies by certificate','Movies by years','Action movies','Adventure movies','Comedy movies','Drama movies','Sci-Fi movies',"'A' Certificate movies",'IMDB Privacy Notice'])
    data = '/Users/himanshutipirneni/Documents/imdb_top_1000.csv'
    df = pd.read_csv(data)
    df = pd.DataFrame(df)
    del df['Poster_Link']
    df = df[df['Released_Year'] != 'PG']
    df['Released_Year'] = df['Released_Year'].astype(int)
    df['Released_Year'].unique()
    df = df.sort_values(by='Released_Year', ascending= False)
    df = df.reset_index(drop= True)

with c3:
    st.markdown('')

    st.markdown(
    "<button style='height: 60px; background-color: #F3CE13; border: none; border-radius: 4px; color: black; font-weight: bold ; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 20px; margin: 4px 2px; cursor: pointer;'><u>Sign In</u></button>",
    unsafe_allow_html=True)

st.markdown('---')

with st.sidebar:
            st.image('/Users/himanshutipirneni/Downloads/imdb1.png', width=80)
            gap(3)
            st.markdown("<h3 style = 'text-align: left ; color: #F3CE13;'><b><u>About Us</u></b></h3>", unsafe_allow_html = True)
            st.write("""Launched online in 1990 and a subsidiary of Amazon.com since 1998, IMDb is the world's most popular and authoritative source for movie, TV and celebrity content, designed to help fans explore the world of movies and shows and decide what to watch.
                     \n\nOur searchable database includes millions of movies, TV and entertainment programs and cast and crew members. """)
            gap(3)
            st.markdown("<h3 style = 'text-align: left ; color: #F3CE13;'><b><u>Contact Us</u></b></h3>", unsafe_allow_html = True)
            st.write("Phone: 1 (800) 432-1000         \n Email: support@imdb.com")

if home == 'Home': 
    
    st.video('/Users/himanshutipirneni/Downloads/imdb.mp4')
    st.markdown("<h40 style = 'text-align: left;'>Credit - IMDB  -  ' https://www.youtube.com/watch?v=QgokG1rBZU4 '</h40>", unsafe_allow_html = True)
    st.markdown('---')
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Movies list on IMDB</h5", unsafe_allow_html = True)
    
    df = df[df['Released_Year'] != 'PG']
    
    df['Released_Year'] = df['Released_Year'].astype(int)
    
    df['Released_Year'].unique()

    ## IMDB TABLES----------------------------------------------------------
    
    df = df.reset_index(drop= True)
    st.dataframe(df)
    gap(4)
    st.markdown("<h4 style = 'text-align: left ; color: #F3CE13;'><u>Reviews</u></h4", unsafe_allow_html = True)

    ## JUSTICE LEAGUE
    
    st.markdown(f"<h3 style='text-align: left; color: white;'><b>Justice League</b></h3>", unsafe_allow_html=True)
    st.video('/Users/himanshutipirneni/Downloads/JL.mp4')

    ###################################################
    st.markdown("<h40 style = 'text-align: right ;'>Credit - Flashback FM  -  ' https://www.youtube.com/watch?v=uC9qU3X1JgM&t=10s '</h40>", unsafe_allow_html = True)
    st.markdown(f"<h5 style='text-align: left; color: white;'><b>Absolutely loved it. Don't listen to what the critics are saying!!</b></h5>", unsafe_allow_html=True)
    st.markdown('<span style="color:gold">&#9733;&#9733;&#9733;&#9733;&#9733;</span>', unsafe_allow_html=True)

    st.write("""If you want a story-deep movie with complex story arcs and Academy award-type acting then of course this movie won't deliver nor should any super hero film, but if you're after some fun, action-filled excitement then this movie for me was exactly what it should be. A blast! \n\n I thoroughly enjoyed it. Absolutely loved it. Of course it is CGI-heavy as all super hero movies are but all the characters gelled well and it flowed fine. There is a lot of action scenes which was great so there are no boring moments. \n\n I suggest you go see it and give the film the Justice it deserves.""")
    st.markdown(f"<h5 style='text-align: right; color: white;'>- @deadpoolbatman</h5>", unsafe_allow_html=True)
    st.markdown('---')

    ## REAL STEEL

    st.markdown(f"<h3 style='text-align: left; color: white;'><b>Real Steel</b></h3>", unsafe_allow_html=True)
    st.video('/Users/himanshutipirneni/Downloads/RS.mp4')
    st.markdown("<h40 style = 'text-align: right ;'>Credit - IGN  -  ' https://www.youtube.com/watch?v=SwfmV3nn6QA&t=9s '</h40>", unsafe_allow_html = True)
    st.markdown(f"<h5 style='text-align: left; color: white;'><b>People's champion? Sounds pretty good to me!!</b></h5>", unsafe_allow_html=True)
    st.markdown('<span style="color:gold">&#9733;&#9733;&#9733;&#9733;&#9733;</span>', unsafe_allow_html=True)
    st.write("""It's always funny watching old movies that depict the future with all this brand new tech, like 90's sci-fi's thinking we'd have flying cars, or in this case Real Steel thinking we'd have robot boxing fights for entertainment in 2020. I remember loving this when I first watched it over a decade ago and after a recent run of disappointing movies I wanted to see something I knew or thought I'd love so I went with this.\n\nStraight off the bat, I noticed how much more believable cgi and vfx used to look in the 2010's and you can see that with other movies like iron man or transformers, while new movies now just look like video games more often than not. I loved how even though it's set in the 'future', the surroundings felt relatable, not all super shiny, slick new tech, adds to the plausibility of it all even though it's scifi.\n\nIt's not complex plot or avant-garde script because it's made just for fun. Has everything you'd want in a feel good action flick; it has flare, blood pumping fights, great soundtrack, story, carnage, an underdog to root for and it even has heart as we get to see a father and son bond together. The movie is sweet and heartfelt at it's core behind all the metal bashing. One thing that stood apart for me about the movie is the end, it ends at the perfect moment, most movies would want a moment of reflection or something after an epic finale like that but Real Steel leaves you while your adrenaline's still pumping. If you haven't watched it, go watch it, and if you have, rewatch.""")


if home == 'Upcoming releases':
    trailers = ["/Users/himanshutipirneni/Downloads/KFP4.mp4", "/Users/himanshutipirneni/Downloads/MW.mp4", "/Users/himanshutipirneni/Downloads/D2.mp4"]
    titles = ['Kung Fu Panda 4', 'Madame Web', 'Dune Part II']
    r_dates = ['March, 2024', 'February, 2024', 'March, 2024']
    st.markdown("<h4 style='text-align: left; color: #F3CE13;'><u><b>Coming soon to theatres :</b></u></h4>", unsafe_allow_html=True)

    for title, video, r_date in zip(titles, trailers, r_dates):
        
        st.markdown(f"<h3 style='text-align: left; color: white;'><u><b>{title}</u></b></h3>", unsafe_allow_html=True)
        st.markdown(f"<h7 style='text-align: left; color: white;'> In theatres {r_date}</h7>", unsafe_allow_html=True)
        st.video(video)
        if title == 'Kung Fu Panda 4':
            st.markdown("<h40 style = 'text-align: right ;'>Credit - Screen Culture  -  ' https://www.youtube.com/watch?v=hEwD1h6VwiY '</h40>", unsafe_allow_html = True)
        elif title == 'Madame Web':
            st.markdown("<h40 style = 'text-align: right ;'>Credit - Sony Pictures Entertainment  -  ' https://www.youtube.com/watch?v=s_76M4c4LTo '</h40>", unsafe_allow_html = True)
        else:
            st.markdown("<h40 style = 'text-align: right ;'>Credit - Warner Bros. Pictures  -  ' https://www.youtube.com/watch?v=U2Qp5pL3ovA '</h40>", unsafe_allow_html = True)
        st.markdown('---s')
    gap(3)

if home == "'A' Certificate movies":
    ## A CERTIFICATE MOVIES----------------------------------------------------------
    
    st.subheader('Movies restricted to adult audience only.')
    
    c = st.checkbox('I am 18 and older')
    
    btn = st.button('Submit')
    
    if c:
        if btn:
            adult = df[df['Certificate']=='A']
            st.dataframe(adult)              

if home == 'Movies by certificate':

    # TABS----------------------------------------------------------
    x,y,z = st.tabs(['U','UA','A'])
    a = df[df['Certificate']=='U']
    b = df[df['Certificate']=='UA']
    c = df[df['Certificate']=='A']

    with x:
        st.subheader('Unrestricted public exhibition')
        a = a.reset_index(drop= True)
        st.dataframe(a)
    with y:
        st.subheader('Unrestricted public exhibition subject to parental guidance for children below the age of 12')
        b = b.reset_index(drop= True)
        st.dataframe(b)
    with z:
        st.subheader('Restricted to adult audience')
        c = c.reset_index(drop= True)
        st.dataframe(c)    

if home == 'Movies by years':
    choice2 = st.selectbox('Select to display all the shows released in those years',['Please select an option','1920-1950', '1950-1980', '1980-2010', '2010-Present'])

    if choice2 == '1920-1950':
        d2 = df[(df['Released_Year'] >= 1920) & (df['Released_Year'] <= 1950)]
        st.write('List of shows released between 1920-1950')
        d2 = d2.reset_index(drop= True)
        st.dataframe(d2)
    
    if choice2 == '1950-1980':
        d3 = df[(df['Released_Year'] >= 1950) & (df['Released_Year'] <= 1980)]
        st.write('List of shows released between 1950-1980')
        d3 = d3.reset_index(drop= True)
        st.dataframe(d3)
    
    if choice2 == '1980-2010':
        d4 = df[(df['Released_Year'] >= 1980) & (df['Released_Year'] <= 2010)]
        st.write('List of shows released between 1980-2010')
        d4 = d4.reset_index(drop= True)
        st.dataframe(d4)

    if choice2 == '2010-Present':
        current_year = 2024
        d5 = df[(df['Released_Year'] >= 2010) & (df['Released_Year'] <= current_year)]
        st.subheader('List of shows released between 1950-1960')
        d5 = d5.reset_index(drop= True)
        st.dataframe(d5)

if home == 'Top 100 movies on IMDB':
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Top 100 movies</h5", unsafe_allow_html = True)
    df1 = df.sort_values(by = 'IMDB_Rating',ascending= False).head(100)
    df1 = df1.reset_index(drop = True)
    st.dataframe(df1)

if home == 'Action movies':
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Action movies</h5", unsafe_allow_html = True)
    df1 = df[df['Genre'].str.contains('Action')]
    df1 = df1.reset_index(drop = True)
    st.dataframe(df1)

if home == 'Adventure movies':
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Adventure movies</h5", unsafe_allow_html = True)
    df1 = df[df['Genre'].str.contains('Adventure')]
    df1 = df1.reset_index(drop = True)
    st.dataframe(df1)

if home == 'Comedy movies':
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Comedy movies</h5", unsafe_allow_html = True)
    df1 = df[df['Genre'].str.contains('Comedy')]
    df1 = df1.reset_index(drop = True)
    st.dataframe(df1)

if home == 'Drama movies':
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Drama movies</h5", unsafe_allow_html = True)
    df1 = df[df['Genre'].str.contains('Drama')]
    df1 = df1.reset_index(drop = True)
    st.dataframe(df1)

if home == 'Sci-Fi movies':
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Sci-Fi movies</h5", unsafe_allow_html = True)
    df1 = df[df['Genre'].str.contains('Sci-Fi')]
    df1 = df1.reset_index(drop = True)
    st.dataframe(df1)

if home == 'IMDB Privacy Notice':
    st.markdown("<h3 style = 'text-align: center ; color: #F3CE13;'><b><u>IMDB Privacy Notice</u></b></h3", unsafe_allow_html = True)
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>Last Updated, June 30, 2023.</h5", unsafe_allow_html = True)
    st.write(""" We know that you care how information about you is used and shared, and we appreciate your trust that we will do so carefully and sensibly. This Privacy Notice describes how IMDb, IMDbPro, and Box Office Mojo (collectively "IMDb") collect and process your personal information through IMDb websites, services, and applications that reference this Privacy Notice (together the "IMDb Services"). By using the IMDb Services, you are consenting to the practices described in this Privacy Notice.""")

    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>What personal information about users does IMDB Collect?</h5", unsafe_allow_html = True)
    st.write("""We collect your personal information in order to provide and continually improve our services and your experience at IMDb.

Here are the types of personal information we collect:""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Information you give us:</h6", unsafe_allow_html = True)
    st.write("""We receive and store any information you provide in relation to IMDb Services. You can choose not to provide certain information, but then you might not be able to take advantage of many of our IMDb Services. See examples of what provided information we collect.""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Automatic Information:</h6", unsafe_allow_html = True)
    st.write("""We automatically collect and store certain types of information about your use of IMDb Services, including information about your interaction with content and services available through IMDb Services. Like many websites, we use "cookies" and other unique identifiers, and we obtain certain types of information when your web browser or device accesses IMDb Services and other content served by or on behalf of IMDb on other websites. See examples of what information we automatically collect and store.""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Information from Other Sources:</h6", unsafe_allow_html = True)    
    st.write("""We might receive information about you from other sources, such as your name and email address when you sign in to IMDb using a third-party login service. See additional examples of the information we receive from other sources.""")
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>For What Purposes Does IMDb Use Your Personal Information?</h5", unsafe_allow_html = True)
    st.write("""We use your personal information to operate, provide, develop, and improve the products and services that we offer our customers. These purposes include:""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Provide, troubleshoot, and improve IMDb Services.</h6", unsafe_allow_html = True)   
    st.write("""We use your personal information to provide the IMDb Services, process payments, enhance functionality, analyze performance, fix errors, and improve the usability and effectiveness of the IMDb Services.""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Recommendations and personalization.</h6", unsafe_allow_html = True)   
    st.write("""We use your personal information to recommend features, content, products, and services that might be of interest to you, identify your preferences, and personalize your experience with IMDb Services.""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Comply with legal obligations.</h6", unsafe_allow_html = True)   
    st.write("""In certain cases, we collect and use your personal information to comply with laws.""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Communicate with you.</h6", unsafe_allow_html = True)  
    st.write(""" We use your personal information to communicate with you in relation to IMDb Services via different channels (e.g., e-mail or on-site forums).""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Advertising.</h6", unsafe_allow_html = True)   
    st.write("""We use your personal information to display interest-based ads for features, products, and services that might be of interest to you. We do not use information that personally identifies you to display interest-based ads. To learn more, please see What About Advertising?.""")
    st.markdown("<h6 style = 'text-align: left ; color: #F3CE13;'> - Fraud Prevention.</h6", unsafe_allow_html = True)   
    st.write("""We use personal information to prevent and detect fraud and abuse in order to protect the security of our customers, IMDb, and others.""")
    st.markdown("<h5 style = 'text-align: left ; color: #F3CE13;'>What About Cookies and Other Identifiers?</h5", unsafe_allow_html = True)
    st.write("""We use cookies, pixels, and other technologies (collectively "cookies") to recognize your browser or device, learn more about your interests, and provide you with essential features and services and for additional purposes, including:

- Recognizing you when you sign-in to our services. This allows us to provide you with content recommendations, display personalized content, and provide other customized features and services.
- Keeping track of your specified preferences. This allows us to honor your preferences, such as whether or not you would like to see interest-based ads. You may set your preferences for interest-based ads here and other preferences in your user account settings.
- Conducting research and diagnostics to improve IMDb's content and services.
- Preventing fraudulent activity.
- Improving security.
- Delivering content, including ads.
- Reporting. This allows us to measure and analyze the performance of our services.

IMDb's cookies allow you to take advantage of some of IMDb's essential features. For instance, if you block or otherwise reject our cookies, you will not be able to contribute content, review films, add items to your Watchlist, or use any IMDb Services that require you to sign in.

Approved third parties may also set cookies when you interact with IMDb Services. Third parties include providers of measurement and analytics services, social media networks, ad networks, ad serving companies, and advertising companies. Third parties use cookies in the process of delivering content, including ads relevant to your interests, to measure the effectiveness of their ads, and to perform services on behalf of IMDb. They may automatically receive an IP address when this happens. 

You can manage browser cookies through your browser settings. The 'Help' feature on most browsers will tell you how to prevent your browser from accepting new cookies, how to have the browser notify you when you receive a new cookie, how to block cookies, and when cookies will expire. If you block all cookies on your browser, neither we nor third parties will transfer cookies to your browser. If you do this, however, you may have to manually adjust some preferences every time you visit a site and some features and services may not work.""")
    


