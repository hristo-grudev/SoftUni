import { render } from "./lib.js";
import { page } from "./lib.js";
import { getUserData } from "./util.js";
import { catalogPage } from "../views/catalog.js";
import { detailsPage } from "../views/details.js";
import { createPage } from "../views/create.js";
import { editPage } from "../views/edit.js";
import { loginPage } from "../views/login.js";
import { registerPage } from "../views/register.js";
import { logout } from "./api.js";

// import * as api from './api/data.js'


const root = document.querySelector('div.container');



page(decorateContext);
page('/', catalogPage);
page('/details/:id', detailsPage);
page('/create', createPage);
page('/edit/:id',editPage);
page('/login', loginPage);
page('/register', registerPage);
page('/my-furniture', catalogPage);


updateUserNav()
page.start();
document.getElementById('logoutBtn').addEventListener('click', onLogout);

function decorateContext(ctx, next) {
	ctx.render = (content) => render(content, root);
	ctx.updateUserNav = updateUserNav;

	next();
}

function updateUserNav() {
	const userData = getUserData();
	if (userData) {
		document.getElementById('user').style.display = 'inline-block';
		document.getElementById('guest').style.display = 'none';
	} else {
		document.getElementById('user').style.display = 'none';
		document.getElementById('guest').style.display = 'inline-block';
	}
}

async function onLogout() {
	await logout();
	updateUserNav()
	page.redirect('/');
}