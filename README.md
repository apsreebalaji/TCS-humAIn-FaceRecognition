# Automatic Attendance and Mood detection

This is the project for face recognition based attendence system. I implemented this system first using only OpenCV, doing everything and then using dlib for face detection and OpenCV for face recognition and the accuracy when we implemented both of them was a bit higher than expected.

I then tried using OpenFace but since neural networks require high graphic support and we were trying to do this project without any server support for later general use, so we did not went that way.

Later, I used dlib for face detection and microsoft's vision cognitive api for face recognition and got a accuracy of 99% in a classroom of 55 students.This is the first phase to the full project where the student are detected from a CCTV camera and detected and marked attendance. The next phase that im implementing is the mood detection of every student and surveying all classes for the students mood and afer successfull mood detection, based on the n umber of students that are unhappy with the ongoing class, the faculties will be notified.

