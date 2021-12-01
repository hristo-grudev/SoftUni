import { page, render } from './lib.js';
import { getUserData } from './util.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { myBooksPage } from './views/my-books.js';
import { registerPage } from './views/register.js';


const root = document.getElementById('site-content');

page(decorateContext);
page('/', homePage);
page('/my-books', myBooksPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details', detailsPage);
page('/edit/:id', editPage);

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
		document.getElementById('user').style.block = 'inline-block';
		document.getElementById('guest').style.block = 'none';
		document.querySelector('#user span').textContent = `Welcome, ${userData.email}`;
	} else{
		document.getElementById('user').style.block = 'none';
		document.getElementById('guest').style.block = 'inline-block';
	}
}