---
layout: exercise_pyodide
permalink: "/Softmax/Exercise1"
title: "CS 477: Softmax Implementation"
excerpt: "CS 477: Softmax Implementation"
canvasasmtid: "189351"
canvaspoints: "2"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  points: 2
  instructions: "<p>Implement the softmax method that turns multiple neuron outputs into probabilities</p>"
  packages: "numpy"
  goals:
    - Implement the softmax method in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ref = "0.182_0.046_0.083_0.293_0.202_0.012_0.081_0.027_0.028_0.047";
  correctcheck: |
    pyodide.globals.get("res") == ref
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == 0
      feedback: "Try again.  It looks like you're still returning 0" 

files:

  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 600
    code: | 
        import numpy as np

        def softmax(u):
            """
            Implement the softmax method

            Parameters
            ----------
            u: ndarray(N)
              Input to softmax
              
            Returns
            -------
            ndarray
                Result of softmax
            """
            ret = np.zeros(len(u))
            ## TODO: Fill this in
            return ret



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        u = np.random.randn(10)
        res = "_".join(["{:.3f}".format(x) for x in softmax(u)])

        
        
---
