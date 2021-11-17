import { showSection } from './dom.js';
import { showCatalogPage } from './vies/catalog.js';
import { showHomePage } from './vies/home.js';
import { showCreatePage } from './vies/create.js';
import { showLoginPage } from './vies/login.js';
import { showRegisterPage } from './vies/register.js';

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

function onNavigate(event) {
    const name = links[event.target.id];
    if (name) {
        event.preventDefault();
        goTo(name);
    }
}

function goTo(name) {
    const view = views[name];
    if (typeof view == 'function') {
        view(ctx);
    }
}