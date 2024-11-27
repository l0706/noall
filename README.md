# LET NOALL DECIDE


####  Video Demo: https://youtu.be/T5shUDup7k
(in the right directionary, w)
To run:
> "flask run"


#### Description:

This project entails a **decisonmaker** web application, presented to the user as a funny bot, who calles himself Noall and likes to say
> "I know all, and I'm Noall".


In the homepage the user can decide to either get quick introduction of Noall or immediately start the queries, so that Noall can generate a decision for you. 


##### Intro:

The Intro is build together by the name.html file and the intro.html file.

The name.html file is the file, to which the user gets directed to first. Here, Noall asks for the name of the user, making sure that the user types in something. You can also go back to the home page, by clicking the "Go Back"-button, which is a part of almost every page of this web-application, in which it makes sense at least.

The second html file is the intro file, in which a "Hi, y/n!" is displayed next to a speaker button. The speaker button can be found throughout the whole web-application everytime a text is being displayed on the screen.
When you hit the speaker, the bot introduces himself in a comedic manner. The whole introduction text is hidden from the user's eyes though.

From there you can start the decisonmaking process.


##### Decisionmaking:

The decisionmaking process is possible because of the decisonmakinh.html and finally it's result is presented in and because of the result.html file.

The process of generating a decision begins with Noall asking how many options one has. It is ensured that the user doesn't submit a number below 1 (since that simply would not make sense) or above 6 (since I thought there should be a limit).

Then, we query the user what their options are through input boxes, however many as the user just said the amount of options are. It is checked that none of the boxes are empty and that the user submitts everything Noall needs to give out an answer. 

So, when the user finshed submitting all of their options, Noall randomly picks one and advises the user in a funny and sometimes threatening manner to also choose it, since his decision must be the only right one because he knows all and best. 
There are two "dictionaries" for Noall or technically correct String lists, with a variety of different sentences that seem logical when giving an answer to someone, kind of in a way a human would. An answer is being randomly put together, from those two lists ("first-part"-list and "second-part"-list). The lists can be found in my app.py file, which takes a big part in the decisionmaking process, checking everything is going well in the "/decisonmaking" route.

Lastly, the user can thank Noall for his choosen and advised decision or state that they indeed do not like Noall's decision, to which Noall of course gives an appropriate reaction to.
    Say "Thanks, Noall!" and he is either very appreciative or he confesses his love for you and the fact that he maybe or maybe not would marry you.
    Say "I don't like your decision" and he gets sad and apologises, he gets sassy or gets mad and may warn or threaten you.
There are also multiple String array's in my script.py file for each reactive emotion, calles "happyDict", "madDict", "sadDict" and "sassyDict".
The javascript randomly, with use of the Math library, picks a phrase or spot in the according array and concerning the reaction when the user dislikes Noall's choice, it is also randomly generated how the bot will react (mad, sad or sassy).
His reaction is being said out loud and not being printed out, to maybe in a way surprise the user or give an impression of how the bot can actually react just like a human would, quickly by speech obviously, since a human doesn't display text on their forehead or something similar.
When a feedback button is being pressed, the bot does not only start talking but stops any speech that happened before or is happening right at the moment.
The funny decisionmaker also changes his face according to ach reactive emotion when a feedback button is clicked by the user and Noall starts to speak.
All of that is handled in the script.js file.


##### Additions:

###### Design:
The design is mostly being handled in the styles.css file. Especially the buttons that light up more when hovering over them and get a tiny bit darker as well. The input boxes also have a light outline to match the buttons. The file is in my static folder. 

###### Html and Layout:
I have a layout file, since it ensures a more efficient and cleaner looking codespace, just as advised in CS50x. 
It ensures the layout of each page or route is the same and the pictures in the flex container is aligned the same way in each webpage.
It makes sure each ebpage or route has it's own title.
There bootstrap is linked, my script.js file for any neccessary javascript and my styles.css to mark it as my stylesheet.
The layout.html file and all f the other html files (index.html, name.html, intro.html, decisionmaker.html, and result.html) are in my templates folder.

###### Images:
All images can be found in my static folder together with script.js and styles.css.
I have the logo that is being displayed in the header of my web-application (built in layout.html). The logo was made by FlamingText.com.
I also have the body of the bot there, which is being displayed in my index route the homepage (index.html) and the name.html file or name route and intro.html page.
The heads or faces of Noall with all of the various reactive emotions, that I put to use in my result.html page are also here. The neutral face look is also the same as the icon in the title block of my web-app.



Thank you!

