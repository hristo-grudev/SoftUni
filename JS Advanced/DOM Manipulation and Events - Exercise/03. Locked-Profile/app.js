function lockedProfile() {
    Array.from(document.querySelectorAll('.profile button')).forEach(b => b.addEventListener('click', onToggle));

    function onToggle(e) {
        const profile = e.target.parentElement;
        const isActive = profile.querySelector('input[type="radio"][value="unlock"]').checked;

        if (isActive) {
            const infoDIf = profile.querySelector('div');
            // const infoDif = Array
            // .from(e.target.parentElement.querySelectorAll('div'))
            // .find(d => d.id.includes('HiddenFields'));

            if (e.target.textContent == 'Show more') {
                infoDIf.style.display = 'block';
                e.target.textContent = 'Hide it';
            } else {
                infoDIf.style.display = '';
                e.target.textContent = 'Show more';
            }
        }
    }
}