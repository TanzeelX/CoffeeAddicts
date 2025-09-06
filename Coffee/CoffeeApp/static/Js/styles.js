// Wait for the document to be fully loaded before adding the event listener
document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('theme-toggle-button')
  toggleButton.addEventListener('click', function () {
    document.body.classList.toggle('dark-mode')
  })
})

// var typed = new Typed(".typing", {
//   strings:["","Welcome To<br>Coffee Addicts"],
//   backSpeed:100,
//   typeSpeed:100,
//   loop:true
// })
