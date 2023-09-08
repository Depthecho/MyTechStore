function darkmode(){
    console.log('Dark mode')
    const body = document.body
    const wasDarkmode = localStorage.getItem("darkmode") == "true"

    localStorage.setItem("darkmode", !wasDarkmode)
    body.classList.toggle('dark-mode', wasDarkmode)
    document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-sun', wasDarkmode)
    document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-moon', !wasDarkmode)
}

document.querySelector('.swap-theme').addEventListener('click', darkmode)


function onload(){
    document.body.classList.toggle('dark-mode', localStorage.getItem('darkmode') == 'true')
}
document.addEventListener('DOMContentLoaded', onload)