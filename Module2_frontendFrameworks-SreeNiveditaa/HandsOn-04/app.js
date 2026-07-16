import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");
const notificationGrid = document.querySelector(".notification-grid");
const totalCredits = document.querySelector("#total-credits");
const selectedCourse = document.querySelector("#selected-course");
const searchInput = document.querySelector("#search-courses");
const sortBtn = document.querySelector("#sort-btn");

const loading = document.querySelector("#loading");
const errorMessage = document.querySelector("#error-message");
const retryBtn = document.querySelector("#retry-btn");


courses.forEach(course => {

    const { name, credits } = course;

    console.log(`${name} - ${credits} Credits`);

});


const formattedCourses = courses.map(course =>
`${course.code} - ${course.name} (${course.credits} Credits)`);

console.log(formattedCourses);


const filtered = courses.filter(course => course.credits >= 4);

console.log("Courses >=4 Credits:", filtered.length);


const total = courses.reduce((sum, course) =>
sum + course.credits, 0);

totalCredits.textContent = `Total Credits : ${total}`;


function renderCourses(courseList){

    courseGrid.innerHTML = "";

    courseList.forEach(course=>{

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `

            <h3>${course.name}</h3>

            <p><strong>Code :</strong> ${course.code}</p>

            <p><strong>Credits :</strong> ${course.credits}</p>

            <span>Grade : ${course.grade}</span>

        `;

        courseGrid.appendChild(article);

    });

}

renderCourses(courses);


searchInput.addEventListener("input",()=>{

    const search = searchInput.value.toLowerCase();

    const result = courses.filter(course=>

        course.name.toLowerCase().includes(search)

    );

    renderCourses(result);

});


sortBtn.addEventListener("click",()=>{

    const sorted = [...courses];

    sorted.sort((a,b)=>b.credits-a.credits);

    renderCourses(sorted);

});


courseGrid.addEventListener("click",(event)=>{

    const card = event.target.closest(".course-card");

    if(!card) return;

    const id = Number(card.dataset.id);

    const course = courses.find(c=>c.id===id);

    selectedCourse.innerHTML = `

        <h3>${course.name}</h3>

        <p>Course Code : ${course.code}</p>

        <p>Credits : ${course.credits}</p>

        <p>Grade : ${course.grade}</p>

    `;

});


function fetchUser(id){

    fetch(`https://jsonplaceholder.typicode.com/users/${id}`)

    .then(response=>response.json())

    .then(data=>{

        console.log("User Name:",data.name);

    });

}

fetchUser(1);


async function fetchUserAsync(id){

    try{

        const response = await fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`);

        const data = await response.json();

        console.log("Async User:",data.name);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(2);


function fetchAllCourses(){

    loading.textContent="Loading Courses...";

    return new Promise(resolve=>{

        setTimeout(()=>{

            resolve(courses);

        },1000);

    });

}

fetchAllCourses().then(data=>{

    renderCourses(data);

    loading.textContent="";

});



Promise.all([

    fetch("https://jsonplaceholder.typicode.com/users/1")
    .then(res=>res.json()),

    fetch("https://jsonplaceholder.typicode.com/users/2")
    .then(res=>res.json())

]).then(users=>{

    console.log(users[0].name);

    console.log(users[1].name);

});


async function apiFetch(url){

    const response = await fetch(url);

    if(!response.ok){

        throw new Error("Unable to fetch data");

    }

    return response.json();

}



async function loadNotifications(){

    loading.style.display="block";

    retryBtn.style.display="none";

    errorMessage.textContent="";

    notificationGrid.innerHTML="";

    try{

        const posts = await apiFetch(

"https://jsonplaceholder.typicode.com/posts?_limit=6"

        );

        loading.style.display="none";

        posts.forEach(post=>{

            const card=document.createElement("div");

            card.className="notification-card";

            card.innerHTML=`

                <h3>${post.title}</h3>

                <p>${post.body}</p>

            `;

            notificationGrid.appendChild(card);

        });

    }

    catch(error){

        loading.style.display="none";

        errorMessage.textContent="Failed to load notifications.";

        retryBtn.style.display="block";

    }

}

loadNotifications();


retryBtn.addEventListener("click",()=>{

    loadNotifications();

});


axios.interceptors.request.use(config=>{

    console.log("API Call Started:",config.url);

    return config;

});

async function axiosPosts(){

    try{

        const response = await axios.get(

"https://jsonplaceholder.typicode.com/posts",

        {

            params:{

                userId:1

            }

        });

        console.log("Axios Posts",response.data);

    }

    catch(error){

        console.log(error);

    }

}

axiosPosts();

