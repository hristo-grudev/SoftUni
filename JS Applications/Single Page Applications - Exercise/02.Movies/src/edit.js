import { showView } from "./dom.js";
import { showHome } from "./home.js";

const section = document.getElementById('edit-movie');
const form = section.querySelector('form');
form.addEventListener('submit', onEdit);


section.remove();

export function showEdit(movie) {
    showView(section);
    const title = form.querySelector('#title');  
    const description = section.querySelector('#description');  
    const img = section.querySelector('#imageUrl');  

    title.value = movie.title;
    description.value = movie.description;
    img.value = movie.img;
}

async function onEdit(event) {
    event.preventDefault();
    const movieData = JSON.parse(sessionStorage.getItem('movie'));
    sessionStorage.removeItem('movie');
    const formData = new FormData(form);

    const title = formData.get('title').trim();
    const description = formData.get('description').trim();
    const img = formData.get('imageUrl').trim();

    const userData = JSON.parse(sessionStorage.getItem('userData'));
    

    try {
        const res = await fetch('http://localhost:3030/data/movies/' + movieData.movie._id, {
            method: 'put',
            headers: {
                'Content-type': 'application/json',
                'X-Authorization': userData.token
            },
            body: JSON.stringify({ title, description, img})
        });

        if (res.ok == false) {
            const error = await res.json();
            throw new Error(error.message);
        }

        const data = await res.json();

        form.reset();
        showHome();
    } catch (err) {
        alert(err.message);
    }
}