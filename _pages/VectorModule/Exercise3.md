---
layout: exercise_pyodide
permalink: "VectorModule/Exercise3"
title: "CS 477: Vector Module: High Dimensional Vectors And Numpy"
excerpt: "CS 477: Vector Module: High Dimensional Vectors And Numpy"
canvasasmtid: "129630"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video3"
  next: "./Video4"
  points: 1.5
  instructions: "<p>The purpose of this exercise is to get you coding with high dimensional vectors in numpy.  Fill in the code below to return a 0 if a particular vector <b>v</b> is closer to the vector <b>a</b> or a 1 if it is closer to vector <b>b</b>.  The distance between two vectors can be computed as the magnitude of the vector subtraction between the two.</p>"
  packages: "numpy"
  goals:
    - Implement vector operations on high dimensional vectors in numpy
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue(pyodide.globals.res);
  correctcheck: |
    pyodide.globals.res == "1.1.1.1.0.0.1.0.1.0"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.res == "0.0.0.0.1.1.0.1.0.1"
      feedback: "Try again.  You're close!  You just have your answer flipped"
    - incorrectcheck: |
        pyodide.globals.res == "0.0.0.0.0.0.0.0.0.0"
      feedback: "Try again.  It looks like you're always saying a is closer each time, but check b as well, because sometimes b is closer"

files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
          import numpy as np

          def get_closer(v, a, b):
              """
              Compute whether 

              Parameters
              ----------
              v: ndarray(d)
                Vector to test
              a: ndarray(d)
                Vector a
              b: ndarray(d)
                Vector b
              
              Return
              ------
              0 if v is closer to a and 1 if vector is closer to b
              """
              res = 0
              ## TODO: Fill this in
              return res



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        res = ""
        d = 100
        for i in range(10):
          v = np.random.randn(d)
          a = np.random.randn(d)
          b = np.random.randn(d)
          res = "{}{}.".format(res, get_closer(v, a, b))
        res = res[0:-1]
---
