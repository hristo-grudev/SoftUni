import { e } from '../dom.js';


const section = document.getElementById('detailsPage');
Selection.remove();

export async function showDetailsPage(ctx) {
    ctx.showSection(section);
}