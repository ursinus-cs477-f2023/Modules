---
layout: exercise_pyodide
permalink: "VectorModule/Exercise4"
title: "CS 477: Vector Module: High Dimensional Dot Products in Numpy"
excerpt: "CS 477: Vector Module: High Dimensional Dot Products in Numpy"
canvasasmtid: "188337"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video4"
  next: "./Video5"
  points: 1.5
  instructions: "<p>Fill in the code below to compute the dot product between two vectors in arbitrary dimensions.</p>"
  packages: "numpy"
  goals:
    - Implement vector operations on high dimensional vectors in numpy
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue(pyodide.globals.get("res"));
  correctcheck: |
    pyodide.globals.get("res") == "1214.0_1237.0_1020.0_507.0_-247.0_392.0_1278.0_665.0_-71.0_-1515.0"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == "0_0_0_0_0_0_0_0_0_0"
      feedback: "Try again.  It looks like you're always returning 0 for the dot product, but this is only true if the vectors are orthogonal."
    - incorrectcheck: |
        pyodide.globals.get("res") == "348.0_352.0_319.0_225.0_nan_198.0_357.0_258.0_nan_nan"
      feedback: "Try again.  Careful!  It looks like you're taking the square root of the dot product, but you don't need to do that."

files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
          import numpy as np

          def get_dotproduct(a, b):
              """
              Compute the dot product between two high dimensional vectors

              Parameters
              ----------
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
          a = np.random.randn(d)
          b = np.random.randn(d)
          res = "{}{}_".format(res, np.round(100*get_dotproduct(a, b)))
        res = res[0:-1]
---
