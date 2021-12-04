import { logout } from './api/api.js';
import { page, render } from './lib.js';
import { getUserData } from './util.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { searchPage } from './views/search.js';


const root = document.getElementById('main-content');

page(decorateContext);
page('/', homePage);
page('/catalog', catalogPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details/:id', detailsPage);
page('/edit/:id', editPage);
page('/search', searchPage);

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
		[...document.getElementsByClassName('user')].forEach((e) => e.style.display = 'inline-block');
		[...document.getElementsByClassName('guest')].forEach((e) => e.style.display = 'none');
	} else{
		[...document.getElementsByClassName('user')].forEach((e) => e.style.display = 'none');
		[...document.getElementsByClassName('guest')].forEach((e) => e.style.display = 'inline-block');
	}
}