import { html } from './utility.js';

const catalogTemplate = (books) => html`
<table>
    <thead>
    <tr>
        <th>Title</th>
        <th>Author</th>
        <th>Action</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Harry Potter</td>
        <td>J. K. Rowling</td>
        <td>
            <button class="edit">Edit</button>
            <button class="delete">Delete</button>
        </td>
    </tr>
    <tr>
        <td>Game of Thrones</td>
        <td>George R. R. Martin</td>
        <td>
            <button>Edit</button>
            <button>Delete</button>
        </td>
    </tr>
    </tbody>
</table>`;