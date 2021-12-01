
import { page, render } from './lib.js';
import * as api from './api/data.js'
import { homePage } from './views/home.js';
import { catalogPage } from './views/catalog.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { logout } from './api/api.js';
import { getUserData } from './util.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { profilePage } from './views/profile.js';

const root = document.querySelector('main');

page(decorateContext);
page('/', homePage);
page('/memes', catalogPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details', detailsPage);
page('/edit/:id', editPage);
page('/profile', profilePage);

updateUserNav();
page.start();
document.getElementById('logoutBtn').addEventListener('click', onLogout);

function decorateContext(ctx, next) {
	ctx.render = (content) => render(content, root);
	ctx.updateUserNav = updateUserNav;

	next();
}

function onLogout() {
	logout();
	updateUserNav();
	page.redirect('/');
}

function updateUserNav() {
	const userData = getUserData();

	if (userData) {
		document.getElementsByClassName('user').style.block = 'block';
		document.getElementsByClassName('guest').style.block = 'none';
		document.querySelector('.user span').textContent = `Welcome, ${userData.email}`;
	} else{
		document.getElementsByClassName('user').style.block = 'none';
		document.getElementsByClassName('guest').style.block = 'block';
	}
}