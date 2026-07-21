import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { getAllCourses } from "../../api/courseApi";

// ==========================
// Async Thunk
// ==========================

export const fetchCourses = createAsyncThunk(
    "courses/fetchCourses",
    async (_, { rejectWithValue }) => {
        try {
            const data = await getAllCourses();

            // Using first 10 posts as sample courses
            return data.slice(0, 10);

        } catch (error) {

            return rejectWithValue(error.message);

        }
    }
);

// ==========================
// Initial State
// ==========================

const initialState = {

    courses: [],

    loading: false,

    error: null

};

// ==========================
// Slice
// ==========================

const coursesSlice = createSlice({

    name: "courses",

    initialState,

    reducers: {

        clearError: (state) => {

            state.error = null;

        }

    },

    extraReducers: (builder) => {

        builder

            .addCase(fetchCourses.pending, (state) => {

                state.loading = true;

                state.error = null;

            })

            .addCase(fetchCourses.fulfilled, (state, action) => {

                state.loading = false;

                state.courses = action.payload;

            })

            .addCase(fetchCourses.rejected, (state, action) => {

                state.loading = false;

                state.error = action.payload;

            });

    }

});

export const { clearError } = coursesSlice.actions;

export default coursesSlice.reducer;