const toggleButton = document.querySelector('#dark-mode-toggle');
const body = document.body;


function toggleDarkMode() {
body.classList.toggle('dark-mode');


const isDarkModeEnabled = body.classList.contains('dark-mode');
localStorage.setItem('modo-oscuro', isDarkModeEnabled);
}


toggleButton.addEventListener('click', toggleDarkMode);


const isDarkModeEnabled = localStorage.getItem('modo-oscuro') === 'true';
if (isDarkModeEnabled) {
body.classList.add('dark-mode');
}


