import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

export async function getAllBooks() {
    return api.get('/data/books?sortBy=_createdOn%20desc');
}

export async function getBookById(id) {
    return api.get('/data/books/' + id);
}

export async function getMyBooks(userId) {
    return api.get(`/data/books?where=_ownerId%3D%22${userId}%22&amp;sortBy=_createdOn%20desc`);
}

export async function createBook(meme) {
    return api.post('/data/books', meme);
}

export async function editBook(id, meme) {
    return api.put('/data/books/' + id, meme);
}

export async function deleteBook(id) {
    return api.del('/data/books/' + id);
}

export async function likeBook(bookId) {
    return api.post('/data/likes', {
        bookId
    });
}

export async function likeBook(bookId) {
    return api.get(`/data/likes?where=bookId%3D%22${bookId}%22&amp;distinct=_ownerId&amp;count`);
}

export async function getMyLikeByBookId(bookId, userId) {
    return api.get(`/data/likes?where=bookId%3D%22${bookId}%22%20and%20_ownerId%3D%22${userId}%22&amp;count`);
}

export async function searchBooks(query) {
    return api.get('/data/books?where=' + encodeURIComponent(`title LIKE "${query}"`));
}
