function darkmode(){
    console.log('Dark mode')
    const body = document.body
    const wasDarkmode = localStorage.getItem("darkmode") == "true"
    if (localStorage.getItem("darkmode") == "true"){
    document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-sun')
    document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-moon')
    }else{
    document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-moon')
    document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-sun')
    }

    localStorage.setItem("darkmode", !wasDarkmode)
    body.classList.toggle('dark-mode', !wasDarkmode)
}

if ((window.location.href.split('/')[3] + window.location.href.split('/')[4]) === "settings?setting=appearance") {
    document.querySelector('.swap-theme').addEventListener('click', darkmode)
    }


function onload(){
if (localStorage.getItem("darkmode") == "true"){
    if ((window.location.href.split('/')[3] + window.location.href.split('/')[4]) === "settings?setting=appearance") {
        document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-sun')
        document.getElementsByClassName("swap-theme")[0].children[0].classList.toggle('fa-moon')
        }
    }
    document.body.classList.toggle('dark-mode', localStorage.getItem('darkmode') == 'true')
}
document.addEventListener('DOMContentLoaded', onload)


function onload_without_button(){
    document.body.classList.toggle('dark-mode', localStorage.getItem('darkmode') == 'true')
}
document.addEventListener('DOMContentLoaded', onload)