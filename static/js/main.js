const nav_btn = document.getElementById('hm-btn');
const mob_menu = document.getElementById('mb-nav');
const show = document.querySelector('#show');
const close = document.querySelector('.auth #close');
const auth = document.querySelector('.auth');
const trust = document.querySelector('#tr');
const trans = document.querySelector('#ts');
const time = document.querySelector('#tm');


var h1 = "Trust"
var p1 = "We ensure that all data of projects must safe and secure. we takes all important steps to protect our client data."
var h2 = "Transparency"
var p2 = "We believe transparency at work will not only help us improve efficiency but also serve as an effective, transparent way for investors to evaluate potential projects."
var h3 = "Timeliness"
var p3 = "We always focus on timeline for end goal so that our client meet their important milestones, with every session focused on each project"


if (nav_btn) {
    nav_btn.addEventListener('click', () => {
        mob_menu.classList.toggle('is-active');
    });
}

if (show) {
    show.addEventListener('click', () => {
        auth.style.display = 'flex';
    });
}

if (close) {
    close.addEventListener('click', () => {
        auth.style.display = 'none';
    });
}

if (trust) {
    trust.addEventListener('click', () => {
        document.getElementById('h').innerHTML = h1;
        document.getElementById('p').innerHTML = p1;
    });
}

if (trans) {
    trans.addEventListener('click', () => {
        document.getElementById('h').innerHTML = h2;
        document.getElementById('p').innerHTML = p2;
    });
}

if (time) {
    time.addEventListener('click', () => {
        document.getElementById('h').innerHTML = h3;
        document.getElementById('p').innerHTML = p3;
    });
}