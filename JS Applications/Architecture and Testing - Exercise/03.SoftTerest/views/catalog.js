import { e } from '../dom.js';


const section = document.getElementById('dashboard-holder');
Selection.remove();

export async function showCatalogPage(ctx) {
    ctx.showSection(section);
}