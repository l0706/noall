document.addEventListener("DOMContentLoaded", function() {

    // All dictionaries

    const happyDict = [
        "Don't make me blush!… That's so nice of you! But that's what I'm here for!",
        "You don't have to thank me, it's my job! But thank you very much, I appreciate you!",
        "Thank you, babe! I've never done this before, so… I appreciate it!",
        "No problem, dude! One more thing though. As a cool individual to another cool individual, you should really never trust robots!",
        "Oh, did you just thank me?… Don't be shy! I know you love me!…… I… actually… love you too…",
        "Oh, did you just say 'thanks'?… You know… if you want to get married, you can just ask me. I'll say 'YES'"
    ];

    const madDict = [
        "Keep talking like that and you'll see what imma do",
        "If I were you, I wouldn't make a robot mad… Have you never seen one of those movies, where the robots take over the world?",
        "Excuse me? You know my friend Chatty G, right? To you probably known as ChatGPT. Do not make me call him!"
    ];
    const sadDict = [
        "Oh, really? I'm sorry! I really tried my best.",
        "Oh…, Uhmm, I apologize. I did my very best.",
        "I'm so sorry, dear human! It's my first day on the job, and I keep screwing up."
    ];
    const sassyDict = [
        "Boohooo. And I, don't like you! Do you see me complaining?",
        "Awwwwww, go cry about it to your mommy.",
        "Okay. Well, I don't like your face. I guess we both have to live with our problems.",
        "Well, I'm not even real. So... I couldn't care less. I just randomly chose one of your stupid options for your stupid decision."
    ];

    // Get all needed elements
    const talkBtn = document.getElementById("talkBtn");
    const text = document.getElementById("text").innerText;
    const goodBtn = document.getElementById("goodBtn");
    const badBtn = document.getElementById("badBtn");
    const img = document.getElementById("image");

    // Add all event listeners
    talkBtn.addEventListener("click", talk);
    goodBtn.addEventListener("click", reactToGood);
    badBtn.addEventListener("click", reactToBad);

    // Define all needed functions:

    function talk() {
        cancelAndSpeak(text);
    }

    function reactToGood() {
        var num = Math. floor(Math. random()*happyDict.length);

        // Change face, according to what will be said
        if (num < 4) {
            img.src = "static/happy.png";

            // Quick wink
            setTimeout(function () {
                img.src = "static/wink.png";
            }, 200);
            setTimeout(function () {
                img.src = "static/happy.png";
            }, 800);

        } else {
            img.src = "static/surprised.png";

            // Fall in love
            setTimeout(function() {
                img.src = "static/love.png";
            }, 1500);
        }

        // And say sth random
        cancelAndSpeak(happyDict[num]);
    }

    function reactToBad() { // or sad or sassy
        var num = Math. floor(Math. random()*3) + 1;

        // Change face and say sth random
        if (num == 1) {
            img.src = "static/mad.png";
            cancelAndSpeak(madDict[(Math.floor(Math.random() * madDict.length))]);
        } else if (num == 2) {
            img.src = "static/sad.png";
            cancelAndSpeak(sadDict[(Math.floor(Math.random() * sadDict.length))]);
        } else {
            img.src = "static/annoyed.png";
            cancelAndSpeak(sassyDict[(Math.floor(Math.random() * sassyDict.length))]);
        }
    }

    function cancelAndSpeak(text) {
        // Stop any speaking in progress
        window.speechSynthesis.cancel();

        // Wait a short time to ensure cancellation completes before speaking new text
        setTimeout(function() {
            const utterThis = new SpeechSynthesisUtterance(text);
            utterThis.lang = "en-US";
            window.speechSynthesis.speak(utterThis);
        }, 100);
    }
});
