import { e } from '../dom.js';


const section = document.getElementById('homePage');
Selection.remove();

export async function showHomePage(ctx) {
    ctx.showSection(section);
}