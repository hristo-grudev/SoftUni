window.addEventListener('load', solve);

function solve() {
    const fields = Array.from(document.querySelectorAll('form input'));
    const addBtn = document.querySelector('#add-btn');
    const colectionOfSongs = document.querySelector('#all-hits div');
    const savedSong = document.querySelector('#saved-hits div');
    const totalLikes = document.querySelector('#total-likes div p');

    addBtn.addEventListener('click', addSong);

    function addSong(event) {
        event.preventDefault();

        const [genre, name, author, date] = fields.map(f => f);

        if (fields.map(f => f.value.trim()).some(v => v == '')) {
            return;
        }

        const saveBtn = e('button', {}, 'Save song');
        saveBtn.classList.add("save-btn");
        const likeBtn = e('button', {}, 'Like song');
        likeBtn.classList.add("like-btn");
        const deleteBtn = e('button', {}, 'Delete');
        deleteBtn.classList.add("delete-btn");

        const song = e('div', {},
            e('img', {src: "./static/img/img.png"}, ''),
            e('h2', {}, `Genre: ${genre.value.trim()}`),
            e('h2', {}, `Name: ${name.value.trim()}`),
            e('h2', {}, `Author: ${author.value.trim()}`),
            e('h3', {}, `Date: ${date.value.trim()}`),
            saveBtn,
            likeBtn,
            deleteBtn
        );
        song.classList.add("hits-info");

        saveBtn.addEventListener('click', saveSong);
        likeBtn.addEventListener('click', likeSong);
        deleteBtn.addEventListener('click', deleteSong);

        colectionOfSongs.appendChild(song);

        genre.value = '';
        name.value = '';
        author.value = '';
        date.value = '';

        console.log(genre);

        function saveSong(event) {
            savedSong.appendChild(event.target.parentElement)
            saveBtn.remove();
            likeBtn.remove();
            
        }
        function likeSong() {
            likes = Number(totalLikes.innerHTML.split(':')[1].trim()) + 1;
            totalLikes.innerHTML = `Total Likes: ${likes}`
            likeBtn.disabled = true;
        }
        function deleteSong() {
            song.remove();
        }
    }



    function e(type, attr, ...content) {
        const element = document.createElement(type);

        for (let prop in attr) {
            element[prop] = attr[prop];
        }

        for (let item of content) {
            if (typeof item == 'string' || typeof item == 'numer') {
                item = document.createTextNode(item);
            }
            element.appendChild(item);
        }
        return element;
    }
}