from flask import Blueprint, jsonify, request # pyright: ignore[reportMissingImports]

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = []


def find_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return course
    return None


@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    required = ["id", "name", "code", "credits"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    courses.append(data)

    return jsonify(data), 201


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):

    course = find_course(course_id)

    if course:
        return jsonify(course)

    return jsonify({"error": "Course not found"}), 404


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    course = find_course(course_id)

    if not course:
        return jsonify({"error": "Course not found"}), 404

    data = request.get_json()

    course.update(data)

    return jsonify(course)


@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    course = find_course(course_id)

    if not course:
        return jsonify({"error": "Course not found"}), 404

    courses.remove(course)

    return jsonify({"message": "Course deleted"})