---
layout: exercise_python
permalink: "Module18/Exercise2"
title: "CS 472: Module 18: SPTQ"
excerpt: "CS 472: Module 18: SPTQ"
canvasasmtid: "117562"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  points: 1.5
  instructions: "Please fill out your SPTQ for the course.  To certify that you have finished, change the method <code>finished_sptq()</code> to return True"
  goals:
    - Practice giving constructive feedback.  If it's positive, say why specifically and what I should keep doing.  If it's negative, say why specifically and what I might do differently.
    
processor:  
  correctfeedback: "Thank you!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
        pos.includes("Finished")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("Whoops")
      feedback: "Please finish your SPTQ and return True from the method once you have done so"
files:
  - filename: "SPTQ Code"
    ismain: false
    name: sptq
    isreadonly: false
    isvisible: true
    height: 100
    code: |
        def finished_sptq():
            # Change this to return True to certify
            # that you have finished your SPTQ
            return False

  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        if finished_sptq():
            print("Finished")
        else:
            print("Whoops")

---
