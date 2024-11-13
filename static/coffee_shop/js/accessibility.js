document.addEventListener('DOMContentLoaded', function() {
    const synth = window.speechSynthesis;

    // Function to speak text
    function speak(text) {
        if (synth.speaking) {
            synth.cancel();
        }
        const utterance = new SpeechSynthesisUtterance(text);
        synth.speak(utterance);
    }

    // Read elements with speech-enabled class
    document.querySelectorAll('.speech-enabled').forEach(element => {
        element.addEventListener('mouseover', function() {
            speak(this.textContent);
        });

        element.addEventListener('focus', function() {
            speak(this.textContent);
        });
    });

    // Auto-read menu items for visually impaired users
    if (window.location.pathname.includes('/menu')) {
        const menuItems = document.querySelectorAll('.coffee-card');
        let menuText = "Our available coffee selections are: ";

        menuItems.forEach(item => {
            const title = item.querySelector('.card-title').textContent;
            const description = item.querySelector('.card-text').textContent;
            menuText += `${title}. ${description}. `;
        });

        speak(menuText);
    }
})