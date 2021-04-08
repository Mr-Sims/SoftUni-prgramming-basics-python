##sol 1

import unittest

from project.student import Student


class StudentTests(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student("TestName", {})

    def test_student_init__when_courses_are_none__expect_courses_to_be_dict(self):
        self.assertEqual({}, self.student.courses)

    def test_enroll__when_adding_an_already_existing_in_courses(self):
        self.student = Student("TestName", {"Python": ["asd"], "JS": ["asd"]})
        course_name = "Python"
        notes = ["test_note", "test_note"]
        add_course_notes = ""
        self.student.enroll(course_name, notes, add_course_notes)
        expected = {"Python": ["asd", "test_note", "test_note"], "JS":["asd"]}
        actual = self.student.courses
        self.assertEqual(expected, actual)

    def test_enroll__when_adding_an_already_existing_in_courses__expect_msg(self):
        self.student = Student("TestName", {"Python": ["asd"], "JS": ["asd"]})
        course_name = "Python"
        notes = ["test_note", "test_note"]
        add_course_notes = ""
        expected_msg = "Course already added. Notes have been updated."
        actual_msg = f"{self.student.enroll(course_name, notes, add_course_notes)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_enroll__when_course_not_existing_in_courses(self):
        self.student = Student("TestName", {"JS": ["asd"]})
        course_name = "Python"
        notes = ["test_note", "test_note"]
        add_course_notes = ""
        self.student.enroll(course_name, notes, add_course_notes)
        expected = {"Python": ["test_note", "test_note"], "JS": ["asd"]}
        actual = self.student.courses
        self.assertEqual(expected, actual)

    def test_enroll__when_course_not_existing_in_courses_with_Y(self):
        self.student = Student("TestName", {"JS": ["asd"]})
        course_name = "Python"
        notes = ["test_note", "test_note"]
        add_course_notes = "Y"
        self.student.enroll(course_name, notes, add_course_notes)
        expected = {"Python": ["test_note", "test_note"], "JS": ["asd"]}
        actual = self.student.courses
        self.assertEqual(expected, actual)

    def test_enroll__when_course_not_existing_in_courses__expect_msg(self):
        self.student = Student("TestName", {"JS": ["asd"]})
        course_name = "Python"
        notes = []
        add_course_notes = "N"
        expected_msg = "Course has been added."
        actual_msg = f"{self.student.enroll(course_name, notes, add_course_notes)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_enroll__when_course_not_existing_in_courses__expect_msg_1(self):
        self.student = Student("TestName", {"JS": ["asd"]})
        course_name = "Python"
        notes = []
        add_course_notes = ""
        expected_msg = "Course and course notes have been added."
        actual_msg = f"{self.student.enroll(course_name, notes, add_course_notes)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_add_notes__when_course_in_courses__return_msg(self):
        self.student = Student("TestName", {"Python": ["asd"], "JS": ["asd"]})
        course_name = "Python"
        notes = ["test_note", "test_note"]
        # self.student.add_notes(course_name, notes)
        expected_msg = "Notes have been updated"
        actual_msg = f"{self.student.add_notes(course_name, notes)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_add_notes__when_course_not_in_courses__expect_exception(self):
        self.student = Student("TestName", {"Python": ["asd"], "JS": ["asd"]})
        course_name = "Java"
        notes = ["test_note", "test_note"]
        with self.assertRaises(Exception) as context:
            self.student.add_notes(course_name, notes)
        expected_msg = "Cannot add notes. Course not found."
        self.assertEqual(expected_msg, str(context.exception))

    def test_leave_course__when_course_in_courses__return_msg(self):
        self.student = Student("TestName", {"Python": ["asd"], "JS": ["asd"]})
        course_name = "Python"
        expected_msg = "Course has been removed"
        actual_msg = f"{self.student.leave_course(course_name)}"
        self.assertEqual(expected_msg, actual_msg)

    def test_leave_course__when_course_not_in_courses__expect_exception(self):
        self.student = Student("TestName", {"Python": ["asd"], "JS": ["asd"]})
        course_name = "Java"
        with self.assertRaises(Exception) as context:
            self.student.leave_course(course_name)
        expected_msg = "Cannot remove course. Course not found."
        self.assertEqual(expected_msg, str(context.exception))

if __name__ == "__main__":
    unittest.main()


##sol 2
#
# import unittest
# from project.student import Student
#
#
# class TestStudent(unittest.TestCase):
#     name = "Test"
#     courses = None
#
#     def setUp(self):
#         self.student = Student(self.name, self.courses)
#
#     def test_student_init__when_courses_are_none__expect_courses_to_be_dict(self):
#         self.assertEqual({}, self.student.courses)
#
#     def test_student_enroll__when_course_is_already_added__expect_to_change_notes(self):
#         self.student.courses["test"] = ["test_notes"]
#         self.assertEqual("Course already added. Notes have been updated.", self.student.enroll("test", ["test_notes2"]))
#         self.assertEqual(["test_notes", "test_notes2"], self.student.courses["test"])
#
#     def test_student_enroll__when_course_is_not_added_and_add_notes_is_empty__expect_add_course_with_notes(self):
#         self.assertEqual("Course and course notes have been added.", self.student.enroll("test", ["test_note"]))
#         self.assertEqual(["test_note"], self.student.courses["test"])
#
#     def test_student_enroll__when_course_is_not_added_and_add_notes_is_Y__expect_add_course_with_notes(self):
#         self.assertEqual("Course and course notes have been added.", self.student.enroll("test", ["test_note"], "Y"))
#         self.assertEqual(["test_note"], self.student.courses["test"])
#
#     def test_student_enroll__when_add_notes_is_not_empty_or_Y__expect_course_to_be_added_with_empty_list(self):
#         self.assertEqual("Course has been added.", self.student.enroll("test", ["test"], "N"))
#         self.assertEqual([], self.student.courses["test"])
#
#     def test_student_add_notes__when_course_is_not_in_courses__expect_exception(self):
#         with self.assertRaises(Exception) as context:
#             self.student.add_notes("test", ["test"])
#
#         self.assertEqual("Cannot add notes. Course not found.", str(context.exception))
#
#     def test_student_add_notes__when_course_is_in_courses__expect_to_update_notes(self):
#         self.student.courses["test"] = ["test1"]
#         self.assertEqual("Notes have been updated", self.student.add_notes("test", "test2"))
#         self.assertEqual(["test1", "test2"], self.student.courses["test"])
#
#     def test_student_leave_course__when_course_is_not_in_courses__expect_exception(self):
#         with self.assertRaises(Exception) as context:
#             self.student.leave_course("test")
#
#         self.assertEqual("Cannot remove course. Course not found.", str(context.exception))
#
#     def test_student_leave_course__when_course_is_in_courses__expect_course_to_be_removed(self):
#         self.student.courses["test"] = ["test"]
#         self.assertEqual("Course has been removed", self.student.leave_course("test"))
#         self.assertEqual({}, self.student.courses)
#
#
# if __name__ == '__main__':
#     unittest.main()