// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

var random_images_array = ['cute-dark.jpg','cute-force.jpg','cute-std.jpg','regular-dark.jpg','regular-force.jpg', 'regular-std.jpg'] 
function getRandomImage(imgAr) {
    var babyAr = imgAr.slice(0,3)
    var forceAr = []
    var forceDarkAr = ['cute-dark.jpg', 'regular-dark.jpg']
    for (i = 0; i < imgAr.length; i++) {
        if (imgAr[i].includes("force")) {
            forceAr.push(imgAr[i])
        }
    }

    var num = Math.floor( Math.random() * imgAr.length );
    var img = imgAr[ num ];
    if (document.getElementById("myText").value.includes("cute") || document.getElementById("myText").value.includes("baby")) {
        var num = Math.floor( Math.random() * babyAr.length );
        img = babyAr[num];
    }
    else if (document.getElementById("myText").value.includes("force") && document.getElementById("myText").value.includes("dark") ) {
        var num = Math.floor( Math.random() * forceDarkAr.length );
        img = forceDarkAr[num];
    }
    else if (document.getElementById("myText").value.includes("force")) {
        var num = Math.floor( Math.random() * forceAr.length );
        img = forceAr[num];
    }
    return 'img/'+img
}

function respond() {
    // Your Code Here
    console.log("Hello World!");
    console.log(document.getElementById("par"));
    img = getRandomImage(random_images_array)
    document.getElementById("photo").src= img;
    quote = ""
    if (img.includes("baby") || img.includes("cute")) {
        hm = "h".concat("m".repeat(Math.floor(Math.random()*15)));
        quote = "Yes, ".concat(hm)
    }
    else {
        quote = std_quotes[Math.floor(Math.random() * std_quotes.length)];
    }

    console.log(quote)
    document.getElementById("par").innerHTML = quote;    
}

var input = document.getElementById('myText')
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById("responseButton").click();
    }
});
