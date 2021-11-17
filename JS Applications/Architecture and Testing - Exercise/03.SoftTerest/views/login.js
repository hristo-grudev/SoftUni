import { e } from '../dom.js';


const section = document.getElementById('loginPage');
Selection.remove();

export async function showLoginPage(ctx) {
    ctx.showSection(section);
}