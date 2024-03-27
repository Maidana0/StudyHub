// SEARCH IN NAVBAR
document.addEventListener('DOMContentLoaded', () => {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const inputSearch = document.getElementById("search")
    const dropdowMenu = document.getElementById("dropdown")
    inputSearch.addEventListener('input', async () => {
        try {
            let query = inputSearch.value.trim()
            if (query.length < 2) return dropdowMenu.style.display = 'none'

            dropdowMenu.innerHTML = ''

            const res = await fetch('/search/publications/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken,
                },
                body: 'query=' + encodeURIComponent(query),
            })
            const data = await res.json()


            data && (dropdowMenu.style.display = 'block')
            data.publications.length > 0
                ? data.publications.forEach(publication => {
                    const liContainer = document.createElement('li')
                    liContainer.innerHTML =
                        `<a class="d-flex justify-content-evenly dropdown-item p-2 w-100"
                            href="/apuntes/${publication.subject}/${publication.subject_id}/publicacion/${publication.id}">
                            <strong class="text-truncate">
                            ${publication.title}
                            </strong>
                            <small class="fw-lighter text-truncate">${publication.subject}</small>
                        </a>`
                    dropdowMenu.prepend(liContainer)

                })
                : dropdowMenu.innerHTML = `<li class="p-1 text-wrap small text-secondary-emphasis fw-lighter text-center">No se encontraron resultados para "${query}"</li>`

        } catch (error) {
            dropdowMenu.innerHTML = 'Ocurrio un error, intentelo más tarde.'
            console.log('Ocurrio un Error: ', error);
        }
    })
})

