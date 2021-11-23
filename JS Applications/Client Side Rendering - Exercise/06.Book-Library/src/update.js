import { html } from './utility.js';


const updateTemplate = (onSuccess) => html`
<form @submit=${ev => onSubmit(ev, onSuccess)} id="edit-form">
    <input type="hidden" name="id">
    <h3>Edit book</h3>
    <label>TITLE</label>
    <input type="text" name="title" placeholder="Title...">
    <label>AUTHOR</label>
    <input type="text" name="author" placeholder="Author...">
    <input type="submit" value="Save">
</form>`;

export function showUpdate(ctx) {
	return updateTemplate(ctx.update());
}

async function onSubmit(event, onSuccess) {
	event.preventDefault();
	const formData = new FormData(event.target);

	const id = formData.get('id');
	const title = formData.get('title').trim();
	const title = formData.get('title').trim();

	await updateBook(id, { title, author });

	event.target.reset();
	onSuccess();

}