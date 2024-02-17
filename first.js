alert("Wellcome in my website.");
console.log("Hello gyes!");
fullName="Vikas kumar";
console.log(fullName);
age=19;
console.log(age);
var video = document.getElementById("song");

        video.addEventListener("ended", function() {
            video.currentTime = 0; // Resetting the currentTime to restart playback
            video.play(); // Start playing again
        }
        );