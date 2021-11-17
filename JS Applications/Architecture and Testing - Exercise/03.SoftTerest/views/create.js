import { e } from '../dom.js';


const section = document.getElementById('createPage');
Selection.remove();

export async function showCreatePage(ctx) {
    ctx.showSection(section);
}