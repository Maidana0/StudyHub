document.addEventListener('DOMContentLoaded', () => {
    const toggle_hidden_courses = document.getElementById('toggle-hidden-courses');
    const courses = document.querySelectorAll('.course');

    const icons = toggle_hidden_courses.querySelectorAll(".bi");
    const span = toggle_hidden_courses.lastElementChild;

    // --------------

    const toggle__all_visibility = document.getElementById('see-all-courses');
    const course_visibility_icons = document.querySelectorAll('.course-visibility');
    const course_handlers_icons = document.querySelectorAll('.course-handler');


    toggle_hidden_courses.addEventListener('click', () => {

        icons.forEach((icon) => {
            icon.classList.toggle('d-none')
        })

        span.textContent = span.textContent === 'Ver' ? 'Ocultar' : 'Ver';

        courses.forEach((hidden_course) => {
            if (hidden_course.classList.contains('d-none')) {
                hidden_course.hasAttribute("style")
                    ? hidden_course.attributes.removeNamedItem("style")
                    : hidden_course.style = "display: table-row!important"
            }
        })
    })


    toggle__all_visibility.addEventListener('click', () => {
        toggle__all_visibility.textContent = toggle__all_visibility.textContent === 'Organizar' ? 'Cancelar' : 'Organizar';

        course_visibility_icons.forEach((visivility_icon) => {
            visivility_icon.classList.toggle('d-none')
        });
        course_handlers_icons.forEach((handler_icons) => {
            handler_icons.classList.toggle('d-none')
        })
    });


})