import { e } from '../dom.js';


const section = document.getElementById('registerPage');
Selection.remove();

export async function showRegisterPage(ctx) {
    ctx.showSection(section);
}