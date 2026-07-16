import { courses } from "./data.js";


courses.forEach(course => {

    const { name, credits } = course;

    console.log(`${name} - ${credits} Credits`);

});



const formattedCourses = courses.map(course =>
    `${course.code} - ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);



const creditCourses = courses.filter(course => course.credits >= 4);

console.log("Courses with >=4 credits:", creditCourses.length);



const totalCredits = courses.reduce(
    (sum, course) => sum + course.credits,
    0
);

console.log("Total Credits:", totalCredits);


const grid = document.querySelector(".course-grid");

const totalCreditsText = document.querySelector("#total-credits");

const selectedCourse = document.querySelector("#selected-course");

const searchInput = document.querySelector("#search-courses");

const sortBtn = document.querySelector("#sort-btn");


function renderCourses(courseList){

    grid.innerHTML = "";

    courseList.forEach(course=>{

        const card = document.createElement("article");

        card.className = "course-card";

        card.dataset.id = course.id;

        card.innerHTML = `

            <h3>${course.name}</h3>

            <p><strong>Code:</strong> ${course.code}</p>

            <p><strong>Credits:</strong> ${course.credits}</p>

            <span>Grade : ${course.grade}</span>

        `;

        grid.appendChild(card);

    });

}


renderCourses(courses);

totalCreditsText.textContent =
`Total Credits Enrolled : ${totalCredits}`;


searchInput.addEventListener("input",()=>{

    const search = searchInput.value.toLowerCase();

    const filteredCourses = courses.filter(course =>

        course.name.toLowerCase().includes(search)

    );

    renderCourses(filteredCourses);

});


sortBtn.addEventListener("click",()=>{

    const sortedCourses = [...courses];

    sortedCourses.sort((a,b)=>b.credits-a.credits);

    renderCourses(sortedCourses);

});

/* ==========================
   EVENT DELEGATION
========================== */

grid.addEventListener("click",(event)=>{

    const card = event.target.closest(".course-card");

    if(!card) return;

    const courseId = Number(card.dataset.id);

    const course = courses.find(c=>c.id===courseId);

    selectedCourse.innerHTML = `

        <h3>${course.name}</h3>

        <p><strong>Course Code:</strong> ${course.code}</p>

        <p><strong>Credits:</strong> ${course.credits}</p>

        <p><strong>Grade:</strong> ${course.grade}</p>

    `;

});