import apiClient from "./apiClient";

export const getAllCourses = () => {

    return apiClient.get("/posts");

};

export const getCourseById = (id) => {

    return apiClient.get(`/posts/${id}`);

};

export const enrollStudent = (course) => {

    return apiClient.post("/posts", course);

};