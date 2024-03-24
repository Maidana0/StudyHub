const modalConfirm = document.getElementById("modal_confirm")
modalConfirm && (modalConfirm.style.display = "none")

const divModalDelete = (name, id, type, extraText) => ` <div class="d-flex align-items-center" style="height:100%"> 
    <div class="m-auto py-4 w-75 text-center shadow-lg rounded bg-light"">
        <h3 class="p-1"> ¿Seguro que desea eliminar la siguiente ${type}?</h3>
        <h5 class="p-1 text-uppercase text-danger my-2">${name}</h5>
        <p class="small text-secondary p-2">${extraText}</p>
        <div class="container"> 
            <button id="close_modal_delete" class="btn btn-dark m-2"> Cancelar </button>
            <button id="delete_${id}" class="btn btn-danger m-2"> Eliminar </button>
        </div>
    </div>
</div>`

const careers = document.querySelectorAll('[id^="career-"]')

careers && careers.forEach(contain => {
    let subjects = document.getElementById(contain.id.replace("career", "subjects"))
    let image = contain.querySelector("img")

    contain.addEventListener('click', e => {
        e.preventDefault()
        if (subjects.hasAttribute("hidden")) {
            contain.scrollIntoView({ block: "center" })

            subjects.removeAttribute("hidden")
            image && image.setAttribute("src", "/static/images/expand_less.svg")
            return
        }
        subjects.setAttribute("hidden", "")
        image && image.setAttribute("src", "/static/images/expand_more.svg")
    })
    // -----------------------------




    // BUTTONS FOR FORM SUBJECT
    const btn_open_form = subjects.getElementsByClassName("btn_add_subject")[0]
    if (btn_open_form) {

        const formContain = subjects.getElementsByClassName('form_container')[0]
        const btn_close_form = formContain.getElementsByClassName('btn_close_form_subject')[0]

        const section = formContain.getElementsByTagName('select')[0]
        section.value = contain.id.split("-")[1]


        btn_open_form.addEventListener('click', e => {
            e.preventDefault()
            if (formContain.hasAttribute("hidden")) {
                formContain.removeAttribute("hidden")
                btn_open_form.setAttribute("hidden", "")
                formContain.scrollIntoView({ block: "center" })
            }
        })

        btn_close_form.addEventListener('click', e => {
            e.preventDefault()
            if (!formContain.hasAttribute("hidden")) {
                formContain.setAttribute("hidden", "")
                btn_open_form.removeAttribute("hidden")
            }
        })
    }

    // MODAL CONFIRM DELETE CAREER (ONLY FOR ADMIN)
    const careerId = contain.id.split("-")[1]
    const deleteCareerBtn = document.getElementById("delete_career_" + careerId)
    if (deleteCareerBtn) {
        deleteCareerBtn.addEventListener("click", (e) => {
            const career = contain.querySelector("h2").textContent
            modalConfirm.innerHTML = divModalDelete(career, careerId, "carrera", "Eliminar la carrera también eliminará todas sus materias, incluyendo sus publicaciones.")
            modalConfirm.style.display = "block"

            const closeModalDeleteBtn = document.getElementById("close_modal_delete")
            const deleteCareer = document.getElementById(`delete_${careerId}`)
            deleteCareer.addEventListener("click", () => window.location.href = `/apuntes/career/delete/${careerId}`)
            closeModalDeleteBtn.addEventListener("click", () => { modalConfirm.style.display = "none", modalConfirm.innerHTML = "" })

        })
    }
})

// MODAL CONFIRM DELETE SUBJECT (ONLY FOR ADMIN)
const subjectsBtnDelete = document.querySelectorAll('[id^="delete_subject_"]')
if (subjectsBtnDelete) {
    subjectsBtnDelete.forEach(btn => {
        const subjectId = btn.id.split("_")[2]
        const subject = btn.ariaRoleDescription
        const [career, careerId] = btn.ariaLabel.split("-")

        btn.addEventListener("click", e => {
            modalConfirm.innerHTML = divModalDelete(
                `<strong>${subject}</strong><br> <small class="fw-light">Carrera: ${career}</small>`,
                subjectId, "materia", "Al eliminar esta materia se eliminarán todas sus publicaciones.")
            modalConfirm.style.display = "block"

            const closeModalDeleteBtn = document.getElementById("close_modal_delete")
            closeModalDeleteBtn.addEventListener("click", () => { modalConfirm.style.display = "none", modalConfirm.innerHTML = "" })

            const deleteSubject = document.getElementById(`delete_${subjectId}`)
            deleteSubject.addEventListener("click", () => window.location.href = `/apuntes/${careerId}/${subject}/delete/${subjectId}`)
        })
    })
}
// -----------------------------



//MODAL FORM CAREER
const modalContainer_careerForm = document.getElementById("backdrop_form")
if (modalContainer_careerForm) {
    const showModal = document.getElementById("open_modal")
    const closeModal = document.getElementById("close_modal")

    showModal.addEventListener('click', (e) => modalContainer_careerForm.classList.replace("modal_hidden", "modal_active"))

    closeModal.addEventListener('click', (e) => modalContainer_careerForm.classList.replace("modal_active", "modal_hidden"))

    modalContainer_careerForm.addEventListener('keydown', (e) => {
        if (modalContainer_careerForm.classList.value.includes("modal_hidden")) e.key == "Tab" && e.preventDefault()
        e.key == "Escape" ? modalContainer_careerForm.classList.replace("modal_active", "modal_hidden") : ''
    })

}



