const careers = document.querySelectorAll('[id^="career-"]')

careers && careers.forEach(contain => {
    let subjects = document.getElementById(contain.id.replace("career", "subjects"))
    let image = contain.querySelector("img")

    contain.addEventListener('click', (e) => {
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


    // BUTTONS FOR FORM TASK
    const btn_open_form = subjects.querySelector('button')
    const formContain = subjects.getElementsByClassName('form_container')[0]
    const btn_close_form = formContain.getElementsByClassName('btn_close_form_subject')[0]

    const section = formContain.getElementsByTagName('select')[0]
    section.value = contain.id.split("-")[1]


    btn_open_form.addEventListener('click', (e) => {
        e.preventDefault()
        if (formContain.hasAttribute("hidden")) {

            formContain.removeAttribute("hidden")
            btn_open_form.setAttribute("hidden", "")
            formContain.scrollIntoView({ block: "center" })
        }
    })

    btn_close_form.addEventListener('click', (e) => {
        e.preventDefault()
        if (!formContain.hasAttribute("hidden")) {
            formContain.setAttribute("hidden", "")
            btn_open_form.removeAttribute("hidden")
        }
    })

})







//MODAL FORM CAREER
const modalContainer_careerForm = document.getElementById("backdrop_form")
const showModal = document.getElementById("open_modal")
const closeModal = document.getElementById("close_modal")

showModal.addEventListener('click', (e) => modalContainer_careerForm.classList.replace("modal_hidden", "modal_active"))

closeModal.addEventListener('click', (e) => modalContainer_careerForm.classList.replace("modal_active", "modal_hidden"))

modalContainer_careerForm.addEventListener('keydown', (e) => {
    if (modalContainer_careerForm.classList.value.includes("modal_hidden")) e.key == "Tab" && e.preventDefault()
    e.key == "Escape" ? modalContainer_careerForm.classList.replace("modal_active", "modal_hidden") : ''
})

