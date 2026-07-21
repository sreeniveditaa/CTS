import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { fetchCourses } from "../features/courses/coursesSlice";

import {
  selectCourses,
  selectLoading,
  selectError,
} from "../features/courses/selectors";

import "./CoursePages.css";

const CoursesPage = () => {
  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);
  const loading = useSelector(selectLoading);
  const error = useSelector(selectError);

  const [search, setSearch] = useState("");

  useEffect(() => {
    dispatch(fetchCourses());
  }, [dispatch]);

  const filteredCourses = courses.filter((course) =>
    course.title.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <header className="navbar">
        <h2>🎓 Student Portal</h2>

        <nav>
          <a href="#">Home</a>
          <a href="#">Courses</a>
          <a href="#">Profile</a>
          <a href="#">Logout</a>
        </nav>
      </header>

      <section className="hero">
        <h1>Welcome to Student Portal</h1>

        <p>Learn Anytime. Grow Every Day.</p>

        <input
          type="text"
          placeholder="Search Courses..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </section>

      {loading && (
        <div className="loading">
          Loading Courses...
        </div>
      )}

      {error && (
        <div className="error">
          Error : {error}
        </div>
      )}

      <div className="course-grid">
        {filteredCourses.map((course) => (
          <div className="course-card" key={course.id}>
            <h3>{course.title}</h3>

            <p>{course.body}</p>

            <button>Enroll</button>
          </div>
        ))}
      </div>

      <footer>
        © 2026 Student Portal | Hands-On 10
      </footer>
    </>
  );
};

export default CoursesPage;