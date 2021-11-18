import { showSection } from './dom.js';
import { showCatalogPage } from './vies/catalog.js';
import { showHomePage } from './vies/home.js';
import { showCreatePage } from './vies/create.js';
import { showLoginPage } from './vies/login.js';
import { showRegisterPage } from './vies/register.js';
import { logout } from '../api/api.js';

const links = {
    'homeLink': 'home',
    'getStartedLink': 'home',
    'catalogLink': 'catalog',
    'loginLink': 'login',
    'registerLink': 'register',
    'createLink': 'create',

}

const views = {
    'home': showHomePage,
    'catalog': showCatalogPage,
    'login': showLoginPage,
    'register': showRegisterPage,
    'create': showCreatePage,
    'details': showDetailsPage
};

const nav = document.querySelector('nav');
nav.addEventListener('click', onNavigate);
document.getElementById('logoutBtn').addEventListener('click', async (ev) => {
    ev.preventDefault();
    await logout();
    updateNav();
    goTo('home');
});

const ctx = {
    goTo,
    showSection,
    updateNav
}

goTo('home');

function onNavigate(event) {
    const name = links[event.target.id];
    if (name) {
        event.preventDefault();
        goTo(name);
    }
}

function goTo(name, ...params) {
    const view = views[name];
    if (typeof view == 'function') {
        view(ctx, ...params);
    }
}

function updateNav() {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData != null) {
        [...nav.querySelectorAll('.user')].forEach(l => l.getElementsByClassName.display = 'block');
        [...nav.querySelectorAll('.guest')].forEach(l => l.getElementsByClassName.display = 'none');
    } else {
        [...nav.querySelectorAll('.user')].forEach(l => l.getElementsByClassName.display = 'none');
        [...nav.querySelectorAll('.guest')].forEach(l => l.getElementsByClassName.display = 'block');
    }
}