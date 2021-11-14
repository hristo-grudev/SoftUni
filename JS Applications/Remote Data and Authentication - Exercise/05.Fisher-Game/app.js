let userData = null;


window.addEventListener('DOMContentLoaded', () => { 
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    if (userData != null) {
        document.getElementById('guest').style.display = 'none';
        document.querySelector('#addForm .add').disabled = false;
    } else {
        document.getElementById('user').style.display = 'none';

    }
    document.querySelector('.load').addEventListener('click', loadData);

    document.getElementById('addForm').addEventListener('click', onCreateSubmit);
    document.getElementById('catches').addEventListener('click', onFishClick);

    document.getElementById('logout').addEventListener('click', onLogout);
});

async function onCreateSubmit(event) {
    event.preventDefault();
    if (!userData) {
        window.location = '/login.html';
        return;
    }
    const formData = new FormData(event.target);

    const data = [...formData.entries()].reduce((a, [k, v]) => Object.assign(a, {[k]: v}), {});

    console.log(userData);
    try {
        if (Object.values(data).some(x => x == '')) {
            throw new Error('All fields are required!');
        }
        const res = await fetch('http://localhost:3030/data/catches', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': userData.token
            },
            body: JSON.stringify(data)
        });

        if (res.ok != true) {
            const error = await res.json();
            throw new Error(error.message);
        }
        
        event.target.reset();
        loadData();
    } catch (err) {
        alert(err.message);
    }
}

async function loadData() {
    const res = await fetch('http://localhost:3030/data/catches');
    const data = await res.json();

    document.getElementById('catches').replaceChildren(...data.map(createPreview));
}

function createPreview(item) {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const isOwner = (userData && item._ownerId == userData.id);

    const element = document.createElement('div');
    element.className = 'catch';
    element.innerHTML = `
<label>Angler</label>
<input type="text" class="angler" value="${item.angler}" ${!isOwner ? "disabled": ""}>
<label>Weight</label>
<input type="text" class="weight" value="${item.weight}" ${!isOwner ? "disabled": ""}>
<label>Species</label>
<input type="text" class="species" value="${item.species}" ${!isOwner ? "disabled": ""}>
<label>Location</label>
<input type="text" class="location" value="${item.location}" ${!isOwner ? "disabled": ""}>
<label>Bait</label>
<input type="text" class="bait" value="${item.bait}" ${!isOwner ? "disabled": ""}>
<label>Capture Time</label>
<input type="number" class="captureTime" value="${item.captureTime}" ${!isOwner ? "disabled": ""}>
<button class="update" data-id="${item.id} ${!isOwner ? "disabled": ""}">Update</button>
<button class="delete" data-id="${item.id} ${!isOwner ? "disabled": ""}">Delete</button>`
    return element;
}


async function onLogout() {
    console.log('logout');
    const result = await fetch('http://localhost:3030/users/login');
    sessionStorage.clear();
    window.location = './index.html';
    return result;
}

async function createFish(fish) {
    const result = await request("http://localhost:3030/data/catches", {
        method: 'post',

        body: JSON.stringify(fish)
    });
    return result
}

async function updateFish(id, fish) {
    const result = await request("http://localhost:3030/data/catches/" + id, {
        method: 'put',

        body: JSON.stringify(fish)
    });
    return result
}

function onFishClick(event) {
    if (event.target.className == 'delete') {
        onDelete(event.target);
    } else if (event.target.className == 'update') {
        onUpdate(event.target);
    }
}

async function onDelete(button) {
    const id = button.dataset.id;
    await deleteFish(id);
    button.parentElement.remove();
}

async function deleteFish(id) {
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const response = await fetch("http://localhost:3030/data/catches/" + id, {
        method: 'delete',
        headers: {
            'Content-Type': 'application/json',
            'X-Authorization': userData.token
        }
    });

    if (response.ok != true) {
        const error = await response.json();
        alert(error.message);
        throw new Error(error.message);
    }

    const result = await response.json();

    return result;
}