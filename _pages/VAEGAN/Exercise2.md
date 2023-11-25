---
layout: exercise_pyodide
permalink: "VAEGAN/Exercise2"
title: "CS 477: Re-Parameterization Trick"
excerpt: "CS 477: Re-Parameterization Trick"
canvasasmtid: "190576"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  next: "./Video3"
  points: 1.5
  instructions: "<p></p>"
  packages: "numpy"
  goals:
    - Use the re-parameterization trick to sample from an arbitrary Gaussian distribution
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue(pyodide.globals.get("res"));
  correctcheck: |
    pyodide.globals.get("res") == "2.729_1.177_0.367_0.196_0.796_2.500_1.397_0.464_-1.861_3.201"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == "0.400_1.334_-0.151_-0.506_0.122_0.579_-0.205_0.377_0.654_1.514"
      feedback: "Try again.  It looks like you're still returning samples from N(0, 1)"

files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
          import numpy as np

          def get_sample(mu, sigma):
              """
              Sample from the Gaussian N(mu, sigma) using the 
              re-parameterization trick

              Parameters
              ----------
              mu: float
                Mean of distribution
              sigma: float
                Standard deviation of distribution
              
              Return
              ------
              float: Sample
              """
              ## Step 1: Sample from N(0, 1)
              z = np.random.randn()
              ## TODO: Use the re-paramterization trick
              return z


  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        res = ""
        for i in range(10):
          mu = np.random.randn()
          sigma = np.random.rand()*4
          res = "{}_{:.3f}".format(res, get_sample(mu, sigma))
        res = res[1::]
---
